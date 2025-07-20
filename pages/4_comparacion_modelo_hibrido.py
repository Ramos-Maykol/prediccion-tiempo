import streamlit as st
import numpy as np
import pandas as pd
import os # Importar el módulo os para operaciones de sistema de archivos
from utils.loader import cargar_modelos, cargar_datos_test, cargar_modelo_hibrido
from utils.evaluacion import calcular_metricas, theils_u, prueba_diebold_mariano
from utils.lang.textos_comparacion_ui import TEXTOS_COMPARACION_UI # Importar textos para la UI
from utils.pdf_generator_comparacion import ComparisonPDFGenerator # NUEVO: Importar el generador de PDF

# --- Configuración de la página y selección de idioma ---
st.set_page_config(layout="wide")

st.sidebar.title(TEXTOS_COMPARACION_UI["opciones_idioma"]["es"]) # Título de la sección de idioma en español
LANGUAGE_OPTIONS = {
    "es": "Español 🇪🇸", "en": "English 🇬🇧", "pt": "Português 🇧🇷",
    "fr": "Français 🇫🇷", "it": "Italiano 🇮🇹"
}
idioma_seleccionado = st.sidebar.selectbox(
    TEXTOS_COMPARACION_UI["seleccione_idioma_label"]["es"], # Etiqueta del selector de idioma en español
    options=list(LANGUAGE_OPTIONS.keys()),
    format_func=lambda code: LANGUAGE_OPTIONS[code]
)

# Atajo para los textos de la UI en el idioma seleccionado
T = {key: trans[idioma_seleccionado] for key, trans in TEXTOS_COMPARACION_UI.items()}


# ------------------------------------------------------------------------------
# 🔹 Título y Descripción
# ------------------------------------------------------------------------------

st.title(T["titulo_app"])
st.markdown(T["intro_app"])

# ------------------------------------------------------------------------------
# 🔹 Cargar modelos y datos
# ------------------------------------------------------------------------------

try:
    modelo_ann, modelo_rf, modelo_xgb = cargar_modelos()
    X_test, y_test = cargar_datos_test()
except Exception as e:
    st.error(f"{T['error_carga_modelos']} {e}")
    st.stop()

# Cargar modelo híbrido (puede que no exista si no se ha entrenado/guardado)
modelo_hibrido = None
try:
    modelo_hibrido = cargar_modelo_hibrido() # Asume que esta función maneja si el archivo no existe
except Exception as e:
    st.warning(T["error_carga_hibrido"])
    # Si el híbrido no carga, lo excluimos de las comparaciones
    pass # Continuar sin el modelo híbrido si no se puede cargar

# ------------------------------------------------------------------------------
# 🔹 Obtener predicciones
# ------------------------------------------------------------------------------

y_pred_ann = modelo_ann.predict(X_test).flatten()
y_pred_rf = modelo_rf.predict(X_test)
y_pred_xgb = modelo_xgb.predict(X_test)

# Inicializar predicción híbrida como None o un array vacío si el modelo no carga
y_pred_hibrido = None
if modelo_hibrido is not None:
    y_pred_hibrido = modelo_hibrido.predict(X_test)

# ------------------------------------------------------------------------------
# 🔹 Comparación de Métricas
# ------------------------------------------------------------------------------

st.subheader(T["metricas_rendimiento"])

metricas = {
    "ANN": calcular_metricas(y_test, y_pred_ann),
    "RF": calcular_metricas(y_test, y_pred_rf),
    "XGB": calcular_metricas(y_test, y_pred_xgb),
}
if y_pred_hibrido is not None:
    metricas[T["col_modelo"]] = calcular_metricas(y_test, y_pred_hibrido) # Usar la traducción para "Híbrido"

df_metricas = pd.DataFrame(metricas).T.reset_index().rename(columns={"index": T["col_modelo"]}) # Usar la traducción para "Modelo"

def resaltar_metricas(df_style):
    estilos = pd.DataFrame("", index=df_style.index, columns=df_style.columns)
    # Resaltar MAE y MSE (menor es mejor)
    for col_key in ["col_mae", "col_mse"]:
        col_name = T[col_key]
        if col_name in df_style.columns:
            idx_min = df_style.loc[:, col_name].idxmin()
            estilos.loc[idx_min, col_name] = "background-color: #d4edda; color: #155724; font-weight: bold;"
    # Resaltar R² (mayor es mejor)
    col_name_r2 = T["col_r2"]
    if col_name_r2 in df_style.columns:
        idx_max = df_style.loc[:, col_name_r2].idxmax()
        estilos.loc[idx_max, col_name_r2] = "background-color: #d4edda; color: #155724; font-weight: bold;"
    return estilos

st.dataframe(
    df_metricas.style.format({
        T["col_mae"]: "{:.4f}",
        T["col_mse"]: "{:.4f}",
        T["col_r2"]: "{:.4f}"
    }).apply(resaltar_metricas, axis=None),
    use_container_width=True
)

# ------------------------------------------------------------------------------
# 🔹 Coeficiente U de Theil
# ------------------------------------------------------------------------------

st.subheader(T["coeficiente_theil"])
st.markdown(T["info_theil"])

valores_u = {
    T["col_modelo"]: ["ANN", "RF", "XGB"],
    T["col_utheil"]: [
        theils_u(y_test, y_pred_ann),
        theils_u(y_test, y_pred_rf),
        theils_u(y_test, y_pred_xgb),
    ]
}
if y_pred_hibrido is not None:
    valores_u[T["col_modelo"]].append(T["col_modelo"]) # Añadir "Híbrido" traducido
    valores_u[T["col_utheil"]].append(theils_u(y_test, y_pred_hibrido))

df_u = pd.DataFrame(valores_u)

def resaltar_minimo_theil(df_style):
    idx_min = df_style.loc[:, T["col_utheil"]].idxmin()
    estilos = pd.DataFrame("", index=df_style.index, columns=df_style.columns)
    estilos.loc[idx_min, :] = "background-color: #d4edda; color: #155724; font-weight: bold;"
    return estilos

st.dataframe(
    df_u.style.format({T["col_utheil"]: "{:.4f}"}).apply(resaltar_minimo_theil, axis=None),
    use_container_width=True
)

# ------------------------------------------------------------------------------
# 🔹 Prueba Diebold-Mariano
# ------------------------------------------------------------------------------

st.subheader(T["prueba_dm"])
st.markdown(T["info_dm"])

if y_pred_hibrido is not None:
    # Realizamos las comparaciones entre modelos
    comparaciones_dm = []
    modelos_individuales = [("ANN", y_pred_ann), ("RF", y_pred_rf), ("XGB", y_pred_xgb)]

    for nombre_modelo, y_pred_modelo in modelos_individuales:
        try:
            dm_stat, p_value = prueba_diebold_mariano(y_test, y_pred_modelo, y_pred_hibrido)
            comparaciones_dm.append((f"{nombre_modelo} vs {T['col_modelo']}", dm_stat, p_value))
        except Exception as e:
            st.warning(T["dm_error"].format(nombre_modelo=nombre_modelo, error=e))
            comparaciones_dm.append((f"{nombre_modelo} vs {T['col_modelo']}", np.nan, np.nan)) # Añadir NaN si hay error

    # Convertimos los resultados a DataFrame
    df_dm = pd.DataFrame(comparaciones_dm, columns=[T["col_comparacion"], T["col_estadistico_dm"], T["col_valor_p"]])
    
    # Función para resaltar en verde el valor p si es menor a 0.05
    def resaltar_valor_p_menor_005(row):
        estilos = [''] * len(row)
        if pd.notna(row[T["col_valor_p"]]) and row[T["col_valor_p"]] < 0.05:
            estilos[row.index.get_loc(T["col_valor_p"])] = 'background-color: #d4edda; color: #155724; font-weight: bold;'
        return estilos
    
    # Mostrar tabla con formato y resaltado
    st.dataframe(
        df_dm.style
            .format({
                T["col_estadistico_dm"]: "{:.4f}",
                T["col_valor_p"]: "{:.4f}"
            })
            .apply(resaltar_valor_p_menor_005, axis=1),
        use_container_width=True
    )

    # Notas informativas sobre los resultados del DM
    for _, row in df_dm.iterrows():
        # Asegurarse de que 'Comparación' existe y no es NaN antes de dividir
        if pd.notna(row[T["col_comparacion"]]):
            nombre_modelo = row[T["col_comparacion"]].split(' ')[0] # Extraer el nombre del modelo individual
        else:
            nombre_modelo = "Modelo Desconocido" # Fallback si la comparación es NaN

        p_value = row[T["col_valor_p"]]
        if pd.notna(p_value):
            if p_value < 0.05:
                st.info(T["dm_resultado_significativo"].format(nombre_modelo=nombre_modelo))
            else:
                st.info(T["dm_resultado_no_significativo"].format(nombre_modelo=nombre_modelo))
        else:
            st.warning(T["dm_error"].format(nombre_modelo=nombre_modelo, error="Cálculo fallido."))
else:
    st.info(T["error_carga_hibrido"]) # Mostrar el mismo warning si el híbrido no se cargó

# ------------------------------------------------------------------------------
# 🔹 Nota informativa general
# ------------------------------------------------------------------------------

st.info(T["nota_informativa_p_value"])

# ------------------------------------------------------------------------------
# 🔹 Botón para Generar PDF
# ------------------------------------------------------------------------------
st.markdown("---")
st.subheader(T["generar_reporte_pdf_seccion_titulo"]) # Usar clave traducida
st.markdown(T["generar_reporte_pdf_info"]) # Usar clave traducida

if st.button(T["boton_descargar_reporte_comparacion_pdf"]): # Usar clave traducida
    if modelo_hibrido is None:
        st.warning(T["error_carga_hibrido"]) # Reutilizar el warning de carga si el híbrido no está
    else:
        with st.spinner("Generando reporte PDF..."): # Mantener el spinner en español o añadir a traducciones
            try:
                pdf_generator = ComparisonPDFGenerator(lang=idioma_seleccionado)
                pdf_filename = f"reporte_comparacion_modelos_{idioma_seleccionado}.pdf"
                
                # Pasar los DataFrames directamente al generador de PDF
                pdf_path = pdf_generator.create_pdf(df_metricas, df_u, df_dm, pdf_filename)

                with open(pdf_path, "rb") as pdf_file:
                    st.download_button(
                        label=T["boton_descargar_reporte_comparacion_pdf"], # Usar clave traducida
                        data=pdf_file,
                        file_name=pdf_filename,
                        mime="application/pdf"
                    )
                st.success(T["pdf_generado_exito"]) # Usar clave traducida
            except Exception as e:
                st.error(T["pdf_error_generacion"].format(error=e)) # Usar clave traducida
            finally:
                # Limpiar el archivo temporal después de la descarga
                if pdf_path.exists():
                    os.remove(pdf_path)
                    # Opcional: eliminar el directorio temporal si está vacío
                    try:
                        os.rmdir(pdf_path.parent)
                    except OSError:
                        pass # El directorio no está vacío, no se elimina
