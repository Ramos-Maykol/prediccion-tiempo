import streamlit as st
import numpy as np
import pandas as pd
import os
from pathlib import Path

# --- MEJORA: Importar la nueva clase en lugar de la función antigua ---
from utils.pdf_generator import PDFReportGenerator
from utils.loader import cargar_modelos, cargar_datos_test
from utils.evaluacion import calcular_metricas, theils_u, prueba_diebold_mariano
from utils.lang.textos_comparacion import TEXTOS_COMPARACION

# --- Constantes y Configuración ---
# Nombres de modelos consistentes
MODEL_NAMES = ["Red Neuronal ANN", "Random Forest", "XGBoost"]

# --- Funciones Cacheadas para Rendimiento ---
# Usamos el decorador de Streamlit para no recalcular todo en cada interacción.
@st.cache_data
def obtener_resultados_modelos():
    """
    Carga modelos, datos y ejecuta todas las evaluaciones.
    Devuelve un diccionario con todos los resultados.
    """
    modelo_ann, modelo_rf, modelo_xgb = cargar_modelos()
    X_test, y_test = cargar_datos_test()

    # Predicciones
    y_pred_ann = modelo_ann.predict(X_test).flatten()
    y_pred_rf = modelo_rf.predict(X_test)
    y_pred_xgb = modelo_xgb.predict(X_test)

    # Métricas
    metricas_dict = {
        MODEL_NAMES[0]: calcular_metricas(y_test, y_pred_ann),
        MODEL_NAMES[1]: calcular_metricas(y_test, y_pred_rf),
        MODEL_NAMES[2]: calcular_metricas(y_test, y_pred_xgb),
    }
    # MEJORA: DataFrame con nombres de columna fijos y en inglés (o un idioma base).
    # La clase PDFReportGenerator se encargará de la traducción.
    df_metricas = pd.DataFrame(metricas_dict).T.reset_index().rename(columns={"index": "Modelo", "R²": "R2"})

    # Coeficiente U de Theil
    theil_values = {
        MODEL_NAMES[0]: theils_u(y_test, y_pred_ann),
        MODEL_NAMES[1]: theils_u(y_test, y_pred_rf),
        MODEL_NAMES[2]: theils_u(y_test, y_pred_xgb),
    }

    # Prueba de Diebold-Mariano
    comparaciones = [
        ("ANN vs RF", *prueba_diebold_mariano(y_test, y_pred_ann, y_pred_rf)),
        ("ANN vs XGB", *prueba_diebold_mariano(y_test, y_pred_ann, y_pred_xgb)),
        ("RF vs XGB", *prueba_diebold_mariano(y_test, y_pred_rf, y_pred_xgb)),
    ]
    # MEJORA: Nombres de columna fijos.
    df_dm = pd.DataFrame(comparaciones, columns=["Comparación", "Estadístico DM", "Valor p"])

    return {
        "df_metricas": df_metricas,
        "theil_values": theil_values,
        "df_dm": df_dm,
        "y_test": y_test,
        "predictions": {
            MODEL_NAMES[0]: y_pred_ann,
            MODEL_NAMES[1]: y_pred_rf,
            MODEL_NAMES[2]: y_pred_xgb,
        },
        "model_names": MODEL_NAMES,
        "best_model": df_metricas.loc[df_metricas['MAE'].idxmin()]['Modelo'],
        "training_times": {MODEL_NAMES[0]: 15.2, MODEL_NAMES[1]: 3.1, MODEL_NAMES[2]: 2.5}
    }

# --- Interfaz de Usuario de Streamlit ---

# 1. Barra Lateral (Sidebar)
st.sidebar.title("⚙️ Opciones del Reporte")
st.sidebar.markdown("---")

LANGUAGE_OPTIONS = {
    "es": "Español 🇪🇸", "en": "English 🇬🇧", "pt": "Português 🇧🇷",
    "fr": "Français 🇫🇷", "it": "Italiano 🇮🇹"
}
idioma = st.sidebar.selectbox(
    "Seleccione el idioma:",
    options=list(LANGUAGE_OPTIONS.keys()),
    format_func=lambda code: LANGUAGE_OPTIONS[code]
)

# Atajo para los textos de la UI
T = {key: trans[idioma] for key, trans in TEXTOS_COMPARACION.items()}

# 2. Cuerpo Principal de la App
st.title(T["titulo"])
st.markdown(T["introduccion"])

# Cargar y procesar los datos (usará el caché si no hay cambios)
try:
    results = obtener_resultados_modelos()
except Exception as e:
    st.error(f"Error al cargar o procesar los modelos y datos: {e}")
    st.stop() # Detiene la ejecución si hay un error crítico

# 3. Mostrar Tablas de Resultados en la UI
st.subheader(T["subtitulo_metricas"])
st.dataframe(results["df_metricas"].style.format({"MAE": "{:.4f}", "MSE": "{:.4f}", "R2": "{:.4f}"}), use_container_width=True)

st.subheader(T["subtitulo_theils_u"])
df_theil_display = pd.DataFrame(results["theil_values"].items(), columns=[T["modelo_col"], "U de Theil"])
st.dataframe(df_theil_display.style.format({"U de Theil": "{:.4f}"}), use_container_width=True)

st.subheader(T["subtitulo_dm"])
# Renombramos columnas solo para mostrar en la UI
df_dm_display = results["df_dm"].rename(columns={
    "Comparación": T["comparacion_col"],
    "Estadístico DM": T["estadistico_col"],
    "Valor p": T["p_valor_col"]
})
st.dataframe(df_dm_display.style.format({T["estadistico_col"]: "{:.4f}", T["p_valor_col"]: "{:.4f}"}), use_container_width=True)
st.info(T["dm_info"])

# 4. Generar el Reporte PDF
st.write("---")
st.subheader(T["generar_pdf"])
st.write(T["pdf_desc"])

if st.button(T["boton_generar"]):
    with st.spinner(T["generando"]):
        try:
            # --- MEJORA: Usar la nueva clase PDFReportGenerator ---
            
            # Configuraciones que antes estaban hardcodeadas en el generador
            machine_specs_config = {
                "CPU": "Intel Core i7-11800H @ 2.30GHz", "RAM": "16 GB DDR4", "GPU": "NVIDIA RTX 3060"
            }
            eda_images_config = {
                "Histograma de Producción": "img/eda_hist_production_time.png",
                "Matriz de Correlación": "img/eda_heatmap_corr.png",
            }
            
            # 1. Crear la instancia del generador
            report_generator = PDFReportGenerator(
                df_metricas=results["df_metricas"],
                theil_values=results["theil_values"],
                df_dm=results["df_dm"],
                y_test=results["y_test"],
                predictions=results["predictions"],
                model_names=results["model_names"],
                best_model=results["best_model"],
                training_times=results["training_times"],
                machine_specs=machine_specs_config,
                eda_images=eda_images_config,
                lang=idioma  # El idioma seleccionado se pasa aquí
            )

            # 2. Generar el archivo PDF
            output_filename = f"reporte_comparativo_{idioma}.pdf"
            pdf_path = report_generator.generate(output_filename)

            st.success(T["exito"])

            # 3. Ofrecer el archivo para descargar
            with open(pdf_path, "rb") as pdf_file:
                st.download_button(
                    label=T["descargar"],
                    data=pdf_file,
                    file_name=os.path.basename(pdf_path),
                    mime="application/pdf"
                )
        except FileNotFoundError as e:
            st.error(f"Error de archivo no encontrado. Asegúrate de que las imágenes EDA existan en la carpeta 'img/'. Detalle: {e}")
        except Exception as e:
            st.error(f"{T['error']}: {e}")

