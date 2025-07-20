import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from fpdf2 import FPDF, XPos # CAMBIO: Importar FPDF y XPos desde fpdf2
from pathlib import Path
from typing import Dict, List, Any, Optional

# Se asume que este import funciona y trae el diccionario de traducciones
from utils.lang.textos_pdf import TRADUCCIONES

# --- MEJORA: Constantes para el diseño del PDF ---
# Facilita el ajuste del layout sin buscar "números mágicos" en el código.
METRICS_TABLE_CONFIG = {
    "col_widths": (60, 30, 30, 25, 25),
    "col_names": ("modelo", "mae", "mse", "r2", "tiempo") # 'r2' es la clave de traducción para R²
}

DM_TABLE_CONFIG = {
    "col_widths": (80, 45, 45),
    "col_names": ("comparacion", "estadistico_dm", "valor_p")
}

TABLE_HEADER_COLOR = (230, 230, 250)
FONT_NAME = "DejaVu"


class PDF(FPDF):
    """
    Clase FPDF personalizada para registrar fuentes y definir header/footer.
    """
    def __init__(self, font_path: Path):
        super().__init__()
        # --- MEJORA: Uso de pathlib y manejo de errores más claro ---
        if font_path.exists():
            self.add_font(FONT_NAME, "", font_path, uni=True)
            self.add_font(FONT_NAME, "B", font_path, uni=True)
            self.add_font(FONT_NAME, "I", font_path, uni=True)
            self.add_font(FONT_NAME, "BI", font_path, uni=True)
            self.set_font(FONT_NAME, "", 12)
        else:
            # Si la fuente personalizada no existe, usa una por defecto y advierte.
            print(f"Advertencia: Fuente no encontrada en {font_path}. Usando 'Helvetica'.")
            self.set_font("Helvetica", "", 12)
        self.set_auto_page_break(auto=True, margin=15)

    def header(self):
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font(self.font_family, "I", 8)
        self.cell(0, 10, f"{self.page_no()}", 0, 0, "C")


class PDFReportGenerator:
    """
    Genera un reporte comparativo en PDF para resultados de modelos de ML.
    """
    # --- MEJORA: Nombres canónicos para columnas de DataFrames ---
    # Estos son los nombres internos que usaremos después de estandarizar.
    CANONICAL_METRICS_COLS = {
        "modelo": "model_name", "mae": "mae_value", "mse": "mse_value", "r2": "r2_value"
    }
    CANONICAL_DM_COLS = {
        "comparacion": "comparison", "estadistico_dm": "dm_statistic", "valor_p": "p_value"
    }

    def __init__(
        self,
        df_metricas: pd.DataFrame,
        theil_values: Dict[str, float],
        df_dm: pd.DataFrame,
        y_test: np.ndarray,
        predictions: Dict[str, np.ndarray],
        model_names: List[str],
        best_model: str,
        training_times: Dict[str, float],
        machine_specs: Dict[str, Any],
        eda_images: Dict[str, str],
        lang: str = "es",
        font_dir: str = "utils/fonts",
        img_dir: str = "img",
        report_dir: str = "reporte"
    ):
        """
        Inicializa el generador de reportes.
        """
        self.y_test = y_test
        self.predictions = predictions
        self.model_names = model_names
        self.best_model = best_model
        self.training_times = training_times
        self.theil_values = theil_values
        self.machine_specs = machine_specs
        self.eda_images = eda_images
        self.lang = lang
        
        # --- MEJORA: Rutas manejadas con pathlib ---
        self.base_path = Path.cwd()
        self.img_path = self.base_path / img_dir
        self.report_path = self.base_path / report_dir
        self.font_path = self.base_path / font_dir / "DejaVuSans.ttf"

        self.img_path.mkdir(exist_ok=True)
        self.report_path.mkdir(exist_ok=True)

        self.t = TRADUCCIONES.get(lang, TRADUCCIONES["es"])
        self.pdf = PDF(self.font_path)

        # --- MEJORA: Lógica de estandarización centralizada ---
        self.df_metricas = self._standardize_dataframe(df_metricas, self.CANONICAL_METRICS_COLS)
        self.df_dm = self._standardize_dataframe(df_dm, self.CANONICAL_DM_COLS)

    def _tr(self, key: str) -> str:
        """Función helper para obtener traducciones."""
        return self.t.get(key, key)

    def _create_reverse_translation_map(self, canonical_map: Dict[str, str]) -> Dict[str, str]:
        """
        Crea un mapa inverso desde cualquier texto traducido o nombre de columna común
        al nombre de columna canónico.
        """
        reverse_map = {}
        for original_key_in_map, canonical_name in canonical_map.items():
            # 1. Mapear la clave original del canonical_map (ej: "r2" -> "r2_value")
            reverse_map[original_key_in_map] = canonical_name

            # 2. Mapear todas las traducciones de esa clave en todos los idiomas
            for lang_code, lang_dict in TRADUCCIONES.items():
                if original_key_in_map in lang_dict:
                    translated_key = lang_dict[original_key_in_map]
                    reverse_map[translated_key] = canonical_name
            
            # 3. Manejo especial para "R2" y "R²" si la clave canónica es "r2_value"
            if canonical_name == "r2_value":
                reverse_map["R2"] = "r2_value" # Para la columna "R2" que viene del Streamlit app
                reverse_map["R²"] = "r2_value" # Para la traducción "R²"

        # 4. Añadir fallbacks para nombres comunes que puedan venir directamente en el DataFrame
        # Estos son para columnas que no necesariamente tienen una clave en TRADUCCIONES
        # pero que podrían ser nombres de columna de entrada.
        if "Modelo" not in reverse_map and "model_name" in canonical_map.values():
            reverse_map["Modelo"] = "model_name"
        if "Comparación" not in reverse_map and "comparison" in canonical_map.values():
            reverse_map["Comparación"] = "comparison"
        if "Estadístico DM" not in reverse_map and "dm_statistic" in canonical_map.values():
            reverse_map["Estadístico DM"] = "dm_statistic"
        if "Valor p" not in reverse_map and "p_value" in canonical_map.values():
            reverse_map["Valor p"] = "p_value"

        return reverse_map

    def _standardize_dataframe(self, df: pd.DataFrame, canonical_map: Dict[str, str]) -> pd.DataFrame:
        """
        Renombra las columnas del DataFrame a nombres canónicos internos,
        independientemente del idioma de las columnas originales.
        """
        df = df.copy()
        reverse_map = self._create_reverse_translation_map(canonical_map)
        
        # Crea el mapa de renombrado solo para las columnas que existen en el df
        # y que tienen una entrada en el reverse_map
        rename_map = {col: reverse_map[col] for col in df.columns if col in reverse_map}
        df = df.rename(columns=rename_map)

        # Verifica si todas las columnas canónicas requeridas están presentes
        missing_cols = set(canonical_map.values()) - set(df.columns)
        if missing_cols:
            raise ValueError(f"Columnas canónicas faltantes en el DataFrame: {missing_cols}. "
                             f"Columnas disponibles: {df.columns.tolist()}")
        return df

    def _add_title_and_intro(self):
        self.pdf.add_page()
        self.pdf.set_font(FONT_NAME, "B", 16)
        self.pdf.cell(0, 10, self._tr("titulo"), ln=1, align="C")
        self.pdf.set_font(FONT_NAME, "", 12)
        self.pdf.multi_cell(0, 8, self._tr("intro")) # Eliminado ln=1
        self.pdf.ln(5)

    def _add_machine_specs(self):
        self.pdf.set_font(FONT_NAME, "B", 13)
        self.pdf.cell(0, 10, self._tr("detalles_maquina"), ln=1)
        self.pdf.set_font(FONT_NAME, "", 11)
        for key, value in self.machine_specs.items():
            if isinstance(value, list):
                self.pdf.multi_cell(0, 7, f"{key}:") # Eliminado ln=1
                for item in value:
                    self.pdf.multi_cell(0, 6, f"  - {item}") # Eliminado ln=1
            else:
                self.pdf.multi_cell(0, 7, f"{key}: {value}") # Eliminado ln=1
        self.pdf.ln(5)

    def _add_eda_visuals(self):
        self.pdf.add_page()
        self.pdf.set_font(FONT_NAME, "B", 13)
        self.pdf.cell(0, 10, self._tr("visualizaciones"), ln=1)
        for title, path_str in self.eda_images.items():
            img_path = Path(path_str)
            if img_path.exists():
                self.pdf.set_font(FONT_NAME, "I", 10)
                self.pdf.cell(0, 7, title, ln=1, align="C")
                # Se calcula la posición x para centrar la imagen manualmente
                img_width = 160
                x_center = (self.pdf.w - img_width) / 2
                self.pdf.image(str(img_path), x=x_center, w=img_width) 
                self.pdf.ln(5)
            else:
                print(f"Advertencia: No se encontró la imagen EDA: {img_path}")
        self.pdf.ln(5)

    def _add_preprocessing_section(self):
        self.pdf.set_font(FONT_NAME, "B", 13)
        self.pdf.cell(0, 10, self._tr("preprocesamiento"), ln=1)
        self.pdf.set_font(FONT_NAME, "", 11)
        self.pdf.multi_cell(0, 8, self._tr("descripcion_preprocesamiento")) # Eliminado ln=1
        self.pdf.ln(5)

    def _add_metrics_table(self):
        self.pdf.add_page()
        self.pdf.set_font(FONT_NAME, "B", 13)
        self.pdf.cell(0, 10, self._tr("metricas"), ln=1)
        
        # Cabecera de la tabla
        self.pdf.set_font(FONT_NAME, "B", 9)
        self.pdf.set_fill_color(*TABLE_HEADER_COLOR)
        for width, name_key in zip(METRICS_TABLE_CONFIG["col_widths"], METRICS_TABLE_CONFIG["col_names"]):
            self.pdf.cell(width, 8, self._tr(name_key), 1, 0, "C", 1)
        self.pdf.ln()

        # Filas de la tabla
        self.pdf.set_font(FONT_NAME, "", 9)
        for model_name in self.model_names:
            # Asegurarse de que 'model_name' es el nombre de la columna canónica
            row = self.df_metricas[self.df_metricas["model_name"] == model_name].iloc[0]
            tiempo = self.training_times.get(model_name, "N/A")
            
            self.pdf.cell(METRICS_TABLE_CONFIG["col_widths"][0], 8, model_name[:35], 1)
            self.pdf.cell(METRICS_TABLE_CONFIG["col_widths"][1], 8, f"{row['mae_value']:.3f}", 1, 0, "C")
            self.pdf.cell(METRICS_TABLE_CONFIG["col_widths"][2], 8, f"{row['mse_value']:.3f}", 1, 0, "C")
            self.pdf.cell(METRICS_TABLE_CONFIG["col_widths"][3], 8, f"{row['r2_value']:.3f}", 1, 0, "C")
            self.pdf.cell(METRICS_TABLE_CONFIG["col_widths"][4], 8, f"{tiempo:.2f}" if isinstance(tiempo, float) else str(tiempo), 1, 1, "C")
        self.pdf.ln(5)
        
    def _add_pred_vs_real_plots(self):
        self.pdf.set_font(FONT_NAME, "B", 13)
        self.pdf.cell(0, 10, self._tr("graficos_pred_vs_real"), ln=1)

        for name, pred in self.predictions.items():
            safe_name = name.replace(" ", "_").lower()
            img_file = self.img_path / f"pred_vs_real_{safe_name}.png"
            
            plt.figure(figsize=(6, 4))
            plt.scatter(self.y_test, pred, alpha=0.6, edgecolors='k', s=20)
            plt.plot([self.y_test.min(), self.y_test.max()], [self.y_test.min(), self.y_test.max()], color='red', linestyle='--')
            plt.xlabel(self._tr("valor_real"))
            plt.ylabel(self._tr("valor_predicho"))
            plt.title(f"{self._tr('pred_vs_real_titulo')} - {name}")
            plt.tight_layout()
            plt.savefig(img_file)
            plt.close()

            if img_file.exists():
                self.pdf.set_font(FONT_NAME, "I", 10)
                self.pdf.cell(0, 7, name, ln=1, align="C")
                # Se calcula la posición x para centrar la imagen manualmente
                img_width = 160
                x_center = (self.pdf.w - img_width) / 2
                self.pdf.image(str(img_file), x=x_center, w=img_width) 
                self.pdf.ln(3)

    def _add_theil_u_section(self):
        self.pdf.add_page()
        self.pdf.set_font(FONT_NAME, "B", 13)
        self.pdf.cell(0, 10, self._tr("theil"), ln=1)
        self.pdf.set_font(FONT_NAME, "", 11)
        for model, u_val in self.theil_values.items():
            self.pdf.cell(0, 8, f"{model}: U = {u_val:.4f}", ln=1)
        self.pdf.ln(5)

    def _add_dm_test_table(self):
        self.pdf.set_font(FONT_NAME, "B", 13)
        self.pdf.cell(0, 10, self._tr("diebold"), ln=1)

        # Cabecera
        self.pdf.set_font(FONT_NAME, "B", 9)
        self.pdf.set_fill_color(*TABLE_HEADER_COLOR)
        for width, name_key in zip(DM_TABLE_CONFIG["col_widths"], DM_TABLE_CONFIG["col_names"]):
            self.pdf.cell(width, 8, self._tr(name_key), 1, 0, "C", 1)
        self.pdf.ln()

        # Filas
        self.pdf.set_font(FONT_NAME, "", 9)
        for _, row in self.df_dm.iterrows():
            stat_val = row['dm_statistic']
            pval_val = row['p_value']
            stat_str = f"{stat_val:.3f}" if pd.notna(stat_val) else "N/A"
            pval_str = f"{pval_val:.3f}" if pd.notna(pval_val) else "N/A"
            
            self.pdf.cell(DM_TABLE_CONFIG["col_widths"][0], 8, str(row["comparison"]), 1)
            self.pdf.cell(DM_TABLE_CONFIG["col_widths"][1], 8, stat_str, 1, 0, "C")
            self.pdf.cell(DM_TABLE_CONFIG["col_widths"][2], 8, pval_str, 1, 1, "C")
        self.pdf.ln(5)

    def _add_conclusion(self):
        self.pdf.set_font(FONT_NAME, "B", 13)
        self.pdf.cell(0, 10, self._tr("conclusion"), ln=1)
        self.pdf.set_font(FONT_NAME, "", 11)
        conclusion_text = self._tr("texto_conclusion").format(modelo=self.best_model)
        self.pdf.multi_cell(0, 8, conclusion_text) # Eliminado ln=1

    def generate(self, output_filename: str = "reporte_comparativo_modelos.pdf") -> Path:
        """
        Genera el reporte PDF completo y lo guarda en el disco.
        """
        self._add_title_and_intro()
        self._add_machine_specs()
        self._add_eda_visuals()
        self._add_preprocessing_section()
        self._add_metrics_table()
        self._add_pred_vs_real_plots()
        self._add_theil_u_section()
        self._add_dm_test_table()
        self._add_conclusion()
        
        output_path = self.report_path / output_filename
        self.pdf.output(output_path)
        print(f"Reporte generado exitosamente en: {output_path}")
        return output_path
