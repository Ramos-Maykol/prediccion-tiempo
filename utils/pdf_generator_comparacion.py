# utils/pdf_generator_comparacion.py
from fpdf import FPDF
from pathlib import Path
import pandas as pd
import numpy as np
import os

# Importar las traducciones específicas para la UI de comparación
from utils.lang.textos_comparacion_ui import TEXTOS_COMPARACION_UI

# --- Constantes para el diseño del PDF ---
FONT_NAME = "DejaVu"
TABLE_HEADER_COLOR = (230, 230, 250) # Light lavender
HIGHLIGHT_COLOR_GOOD = (212, 237, 218) # Light green for good results

class PDF(FPDF):
    """
    Clase FPDF personalizada para registrar fuentes y definir header/footer.
    """
    def __init__(self, lang: str = "es", font_path: Path = Path("utils/fonts/DejaVuSans.ttf")):
        super().__init__()
        self.lang = lang
        self.t = TEXTOS_COMPARACION_UI # Acceso directo al diccionario de traducciones

        # Asegurarse de que el diccionario de traducciones tenga el idioma
        if self.lang not in self.t["titulo_app"]: # Usar una clave común para verificar idioma
            self.lang = "es" # Fallback a español

        if font_path.exists():
            self.add_font(FONT_NAME, "", str(font_path), uni=True)
            self.add_font(FONT_NAME, "B", str(font_path), uni=True)
            self.add_font(FONT_NAME, "I", str(font_path), uni=True)
            self.add_font(FONT_NAME, "BI", str(font_path), uni=True)
            self.set_font(FONT_NAME, "", 12)
        else:
            print(f"Advertencia: Fuente no encontrada en {font_path}. Usando 'Helvetica'.")
            self.set_font("Helvetica", "", 12)
        self.set_auto_page_break(auto=True, margin=15)

    def header(self):
        self.set_y(10)
        self.set_font(FONT_NAME, "B", 10)
        self.cell(0, 5, self.t["titulo_app"][self.lang], 0, 1, "C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font(FONT_NAME, "I", 8)
        self.cell(0, 10, f"{self.t['opciones_idioma'][self.lang]} - Página {self.page_no()}", 0, 0, "C") # Usar una traducción para el footer


class ComparisonPDFGenerator:
    """
    Genera un reporte PDF con la comparación de modelos de predicción.
    """
    def __init__(self, lang: str = "es", output_dir: str = "reportes_comparacion", font_dir: str = "utils/fonts", machine_specs: dict = None):
        self.lang = lang
        self.output_path = Path.cwd() / output_dir
        self.output_path.mkdir(exist_ok=True)
        self.font_path = Path.cwd() / font_dir / "DejaVuSans.ttf"
        self.machine_specs = machine_specs if machine_specs is not None else {}
        
        self.t = TEXTOS_COMPARACION_UI # Acceso directo al diccionario de traducciones
        self.pdf = PDF(self.lang, self.font_path)

    def _tr(self, key: str) -> str:
        """Función helper para obtener traducciones de TEXTOS_COMPARACION_UI."""
        # Accede a la traducción para la clave dada y el idioma actual
        return self.t.get(key, {}).get(self.lang, key)

    def _add_title(self, title: str):
        """Añade un título centrado al PDF."""
        self.pdf.set_font(FONT_NAME, "B", 18)
        self.pdf.cell(0, 10, title, ln=1, align="C")
        self.pdf.ln(10)

    def _add_section_title(self, title: str):
        """Añade un subtítulo de sección al PDF."""
        self.pdf.set_font(FONT_NAME, "B", 14)
        self.pdf.cell(0, 10, title, ln=1)
        self.pdf.ln(5)

    def _add_text(self, text: str, font_style: str = "", font_size: int = 12):
        """Añade texto al PDF con salto de línea automático."""
        self.pdf.set_font(FONT_NAME, font_style, font_size)
        self.pdf.multi_cell(0, 8, text)
        self.pdf.ln(3)

    def _add_metrics_table(self, df_metricas: pd.DataFrame):
        """Añade la tabla de métricas de rendimiento al PDF."""
        self._add_section_title(self._tr("metricas_rendimiento"))
        self._add_text(self._tr("info_metricas"))

        # Columnas y anchos
        col_widths = [40, 30, 30, 30] # Modelo, MAE, MSE, R²
        headers = [self._tr("col_modelo"), self._tr("col_mae"), self._tr("col_mse"), self._tr("col_r2")]

        self.pdf.set_fill_color(*TABLE_HEADER_COLOR)
        self.pdf.set_font(FONT_NAME, "B", 10)
        for i, header in enumerate(headers):
            self.pdf.cell(col_widths[i], 10, header, 1, 0, "C", 1)
        self.pdf.ln()

        self.pdf.set_font(FONT_NAME, "", 10)
        for index, row in df_metricas.iterrows():
            self.pdf.cell(col_widths[0], 8, row[self._tr("col_modelo")], 1)
            
            # Resaltado para MAE y MSE (menor es mejor)
            for i, col_key in enumerate(["col_mae", "col_mse"]):
                col_name = self._tr(col_key)
                cell_value = f"{row[col_name]:.4f}"
                is_min = row[col_name] == df_metricas[col_name].min()
                self.pdf.set_fill_color(*HIGHLIGHT_COLOR_GOOD) if is_min else self.pdf.set_fill_color(255, 255, 255)
                self.pdf.cell(col_widths[i+1], 8, cell_value, 1, 0, "C", 1)
            
            # Resaltado para R² (mayor es mejor)
            col_name_r2 = self._tr("col_r2")
            cell_value_r2 = f"{row[col_name_r2]:.4f}"
            is_max = row[col_name_r2] == df_metricas[col_name_r2].max()
            self.pdf.set_fill_color(*HIGHLIGHT_COLOR_GOOD) if is_max else self.pdf.set_fill_color(255, 255, 255)
            self.pdf.cell(col_widths[3], 8, cell_value_r2, 1, 1, "C", 1)
        self.pdf.ln(5)
        self.pdf.set_fill_color(255, 255, 255) # Reset fill color

    def _add_theils_u_table(self, df_u: pd.DataFrame):
        """Añade la tabla del coeficiente U de Theil al PDF."""
        self._add_section_title(self._tr("coeficiente_theil"))
        self._add_text(self._tr("info_theil"))

        col_widths = [80, 40] # Modelo, U de Theil
        headers = [self._tr("col_modelo"), self._tr("col_utheil")]

        self.pdf.set_fill_color(*TABLE_HEADER_COLOR)
        self.pdf.set_font(FONT_NAME, "B", 10)
        for i, header in enumerate(headers):
            self.pdf.cell(col_widths[i], 10, header, 1, 0, "C", 1)
        self.pdf.ln()

        self.pdf.set_font(FONT_NAME, "", 10)
        for index, row in df_u.iterrows():
            self.pdf.cell(col_widths[0], 8, row[self._tr("col_modelo")], 1)
            
            cell_value = f"{row[self._tr('col_utheil')]:.4f}"
            is_min = row[self._tr('col_utheil')] == df_u[self._tr('col_utheil')].min()
            self.pdf.set_fill_color(*HIGHLIGHT_COLOR_GOOD) if is_min else self.pdf.set_fill_color(255, 255, 255)
            self.pdf.cell(col_widths[1], 8, cell_value, 1, 1, "C", 1)
        self.pdf.ln(5)
        self.pdf.set_fill_color(255, 255, 255) # Reset fill color

    def _add_diebold_mariano_table(self, df_dm: pd.DataFrame):
        """Añade la tabla de la prueba Diebold-Mariano al PDF."""
        self._add_section_title(self._tr("prueba_dm"))
        self._add_text(self._tr("info_dm"))

        col_widths = [70, 40, 40] # Comparación, Estadístico DM, Valor p
        headers = [self._tr("col_comparacion"), self._tr("col_estadistico_dm"), self._tr("col_valor_p")]

        self.pdf.set_fill_color(*TABLE_HEADER_COLOR)
        self.pdf.set_font(FONT_NAME, "B", 10)
        for i, header in enumerate(headers):
            self.pdf.cell(col_widths[i], 10, header, 1, 0, "C", 1)
        self.pdf.ln()

        self.pdf.set_font(FONT_NAME, "", 10)
        for index, row in df_dm.iterrows():
            self.pdf.cell(col_widths[0], 8, row[self._tr("col_comparacion")], 1)
            
            stat_value = f"{row[self._tr('col_estadistico_dm')]:.4f}" if pd.notna(row[self._tr('col_estadistico_dm')]) else "N/A"
            p_value = f"{row[self._tr('col_valor_p')]:.4f}" if pd.notna(row[self._tr('col_valor_p')]) else "N/A"

            self.pdf.cell(col_widths[1], 8, stat_value, 1, 0, "C")
            
            # Resaltar valor p si es significativo
            if pd.notna(row[self._tr('col_valor_p')]) and row[self._tr('col_valor_p')] < 0.05:
                self.pdf.set_fill_color(*HIGHLIGHT_COLOR_GOOD)
            else:
                self.pdf.set_fill_color(255, 255, 255)
            self.pdf.cell(col_widths[2], 8, p_value, 1, 1, "C", 1)
        self.pdf.ln(5)
        self.pdf.set_fill_color(255, 255, 255) # Reset fill color

        # Notas informativas sobre los resultados del DM
        for _, row in df_dm.iterrows():
            # Asegurarse de que 'Comparación' existe y no es NaN antes de dividir
            if pd.notna(row[self._tr("col_comparacion")]):
                nombre_modelo = row[self._tr("col_comparacion")].split(' ')[0] # Extraer el nombre del modelo individual
            else:
                nombre_modelo = "Modelo Desconocido" # Fallback si la comparación es NaN

            p_value = row[self._tr("col_valor_p")]
            if pd.notna(p_value):
                if p_value < 0.05:
                    self._add_text(self._tr("dm_resultado_significativo").format(nombre_modelo=nombre_modelo))
                else:
                    self._add_text(self._tr("dm_resultado_no_significativo").format(nombre_modelo=nombre_modelo))
            else:
                self._add_text(self._tr("dm_error").format(nombre_modelo=nombre_modelo, error="Cálculo fallido."))
        self.pdf.ln(5)

    def _add_machine_specs(self):
        """Añade las especificaciones de la máquina al PDF."""
        self._add_section_title(self._tr("especificaciones_maquina_titulo"))
        self._add_text(self._tr("especificaciones_maquina_info"))
        self.pdf.ln(2)

        for spec, value in self.machine_specs.items():
            # Usar las claves de traducción genéricas si están definidas en textos_app.py
            # O simplemente usar el spec tal cual si no hay traducción específica aquí.
            translated_spec = self._tr(f"{spec.lower()}_label") if f"{spec.lower()}_label" in self.t else spec
            self.pdf.set_font(FONT_NAME, "B", 12)
            self.pdf.cell(0, 8, f"- {translated_spec}: {value}", ln=1)
        self.pdf.ln(5)


    def create_pdf(self, df_metricas: pd.DataFrame, df_u: pd.DataFrame, df_dm: pd.DataFrame, filename: str = "reporte_comparacion_modelos.pdf") -> Path:
        """
        Crea el PDF completo con la comparación de modelos.
        Retorna la ruta completa del archivo PDF generado.
        """
        self.pdf.add_page()
        self._add_title(self._tr("titulo_app"))
        self._add_text(self._tr("intro_app"))
        self.pdf.ln(5)

        # Añadir especificaciones de la máquina al inicio del reporte
        if self.machine_specs:
            self._add_machine_specs()
            self.pdf.add_page() # Nueva página después de las specs, para que las tablas empiecen limpias

        self._add_metrics_table(df_metricas)
        self.pdf.add_page() # Nueva página para Theil's U
        self._add_theils_u_table(df_u)
        self.pdf.add_page() # Nueva página para Diebold-Mariano
        self._add_diebold_mariano_table(df_dm)

        # Nota informativa final
        self._add_text(self._tr("nota_informativa_p_value"), font_style="I")

        output_path = self.output_path / filename
        self.pdf.output(output_path)
        return output_path
