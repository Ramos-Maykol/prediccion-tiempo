# utils/pdf_generator_prediccion.py
from fpdf import FPDF, XPos # Importar XPos para centrar imágenes
from pathlib import Path
from typing import Dict, List, Any, Optional
import os # Necesario para Path.cwd()

# Se asume que este import funciona y trae el diccionario de traducciones
from utils.lang.textos_pdf_prediccion import TRADUCCIONES_PREDICCION

# --- Constantes para el diseño del PDF ---
FONT_NAME = "DejaVu"
TABLE_HEADER_COLOR = (230, 230, 250) # Light lavender

class PDF(FPDF):
    """
    Clase FPDF personalizada para registrar fuentes y definir header/footer.
    """
    def __init__(self, font_path: Path, lang: str = "es"):
        super().__init__()
        self.lang = lang
        self.t = TRADUCCIONES_PREDICCION.get(lang, TRADUCCIONES_PREDICCION["es"])

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
        self.cell(0, 5, self.t["titulo_reporte"], 0, 1, "C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font(FONT_NAME, "I", 8)
        self.cell(0, 10, f"{self.t['pie_pagina']} - Página {self.page_no()}", 0, 0, "C")


class PredictionPDFGenerator:
    """
    Genera un reporte PDF con la predicción del tiempo de producción
    y una recomendación de recogida.
    """
    def __init__(self, lang: str = "es", output_dir: str = "reportes_prediccion", font_dir: str = "utils/fonts"):
        self.lang = lang
        self.output_path = Path.cwd() / output_dir
        self.output_path.mkdir(exist_ok=True)
        self.font_path = Path.cwd() / font_dir / "DejaVuSans.ttf"
        
        self.t = TRADUCCIONES_PREDICCION.get(lang, TRADUCCIONES_PREDICCION["es"])
        self.pdf = PDF(self.font_path, self.lang) # Pasar el idioma al constructor de PDF

    def _tr(self, key: str) -> str:
        """Función helper para obtener traducciones."""
        return self.t.get(key, key)

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
        self.pdf.multi_cell(0, 8, text) # Ajustar alto de línea para mejor legibilidad
        self.pdf.ln(3) # Espacio después del texto

    def _add_parameters_table(self, input_data: Dict[str, Any], etiquetas: Dict[str, str]):
        """Añade una tabla con los parámetros de entrada utilizados."""
        self._add_section_title(self._tr("seccion_parametros"))

        # Definir el ancho de las columnas
        col_width_label = 80
        col_width_value = 100
        row_height = 8

        self.pdf.set_fill_color(*TABLE_HEADER_COLOR)
        self.pdf.set_font(FONT_NAME, "B", 10)
        self.pdf.cell(col_width_label, row_height, self._tr("parametro"), 1, 0, "C", 1)
        self.pdf.cell(col_width_value, row_height, self._tr("valor"), 1, 1, "C", 1)

        self.pdf.set_font(FONT_NAME, "", 10)
        for key, value in input_data.items():
            # Usar la etiqueta traducida si existe, de lo contrario usar la clave
            display_label = etiquetas.get(key, key)
            self.pdf.cell(col_width_label, row_height, display_label, 1)
            self.pdf.cell(col_width_value, row_height, str(value), 1, 1)
        self.pdf.ln(5)

    def generate_recommendation(self, predicted_time: float) -> str:
        """Genera una recomendación de recogida basada en el tiempo estimado."""
        if predicted_time <= 8:
            return self._tr("recomendacion_1")
        elif 8 < predicted_time <= 16:
            return self._tr("recomendacion_2")
        else:
            return self._tr("recomendacion_3")

    def create_pdf(self, predicted_time: float, model_name: str, input_data: Dict[str, Any], etiquetas: Dict[str, str], filename: str = "reporte_prediccion.pdf") -> Path:
        """
        Crea el PDF completo con la predicción y la recomendación.
        Retorna la ruta completa del archivo PDF generado.
        """
        self.pdf.add_page()
        self._add_title(self._tr("titulo_reporte"))
        self._add_text(self._tr("introduccion_reporte"))

        self._add_section_title(self._tr("seccion_prediccion"))
        self._add_text(f"{self._tr('texto_prediccion_modelo')} **{model_name}**.", font_style="B")
        self._add_text(f"{self._tr('tiempo_estimado')} **{predicted_time:.2f} {self._tr('horas_unidad')}**.", font_style="B", font_size=14)
        self.pdf.ln(5)

        self._add_section_title(self._tr("seccion_recomendacion"))
        recommendation = self.generate_recommendation(predicted_time)
        self._add_text(recommendation)
        self.pdf.ln(5)

        # Añadir tabla de parámetros de entrada
        self._add_parameters_table(input_data, etiquetas)

        output_path = self.output_path / filename
        self.pdf.output(output_path)
        return output_path
