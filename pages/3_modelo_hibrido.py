import streamlit as st
import numpy as np
import pandas as pd
import joblib
import os
from pathlib import Path # Importar Path para manejo de rutas

from utils.loader import cargar_modelos, cargar_datos_test
from utils.evaluacion import theils_u, calcular_metricas, prueba_diebold_mariano
from utils.modelo_hibrido import ModeloHibrido # ✅ IMPORTACIÓN CORRECTA
from utils.lang.textos_hibrido_ui import TEXTOS_HIBRIDO_UI # NUEVO: Importar textos para la UI

# --- Configuración de la página y selección de idioma ---
st.set_page_config(layout="wide")

st.sidebar.title(TEXTOS_HIBRIDO_UI["opciones_idioma"]["es"]) # Título de la sección de idioma en español
LANGUAGE_OPTIONS = {
    "es": "Español 🇪🇸", "en": "English 🇬🇧", "pt": "Português 🇧🇷",
    "fr": "Français 🇫🇷", "it": "Italiano 🇮🇹"
}
idioma_seleccionado = st.sidebar.selectbox(
    TEXTOS_HIBRIDO_UI["seleccione_idioma_label"]["es"], # Etiqueta del selector de idioma en español
    options=list(LANGUAGE_OPTIONS.keys()),
    format_func=lambda code: LANGUAGE_OPTIONS[code]
)

# Atajo para los textos de la UI en el idioma seleccionado
T = {key: trans[idioma_seleccionado] for key, trans in TEXTOS_HIBRIDO_UI.items()}

# -------------------------------------------------------------------
st.title(T["titulo_app"])
st.markdown(T["intro_app"])

# Cargar modelos y datos de prueba
try:
    modelo_ann, modelo_rf, modelo_xgb = cargar_modelos()
    X_test, y_test = cargar_datos_test()
except Exception as e:
    st.error(f"{T['error_carga_modelos']} {e}")
    st.stop()

# -------------------------------------------------------------------
st.subheader(T["asignacion_pesos"])
st.markdown(T["ajusta_pesos_info"])

col_pesos_1, col_pesos_2, col_pesos_3 = st.columns(3)
with col_pesos_1:
    peso_ann = st.number_input(T["peso_ann"], min_value=0.0, max_value=1.0, value=0.33, step=0.01, help=T["help_peso_ann"])
with col_pesos_2:
    peso_rf = st.number_input(T["peso_rf"], min_value=0.0, max_value=1.0, value=0.33, step=0.01, help=T["help_peso_rf"])
with col_pesos_3:
    peso_xgb = st.number_input(T["peso_xgb"], min_value=0.0, max_value=1.0, value=0.34, step=0.01, help=T["help_peso_xgb"])

# Ajuste automático de pesos para que sumen 1.0 (opcional, pero útil)
total_pesos = peso_ann + peso_rf + peso_xgb
if abs(total_pesos - 1.0) > 1e-4:
    st.warning(T["warning_suma_pesos"])
    # Normalizar pesos para que sumen 1.0 si no lo hacen
    if total_pesos != 0:
        peso_ann_norm = peso_ann / total_pesos
        peso_rf_norm = peso_rf / total_pesos
        peso_xgb_norm = peso_xgb / total_pesos
    else: # Evitar división por cero si todos los pesos son 0
        peso_ann_norm, peso_rf_norm, peso_xgb_norm = 1/3, 1/3, 1/3
    weights_to_use = [peso_ann_norm, peso_rf_norm, peso_xgb_norm]
else:
    weights_to_use = [peso_ann, peso_rf, peso_xgb]

if st.button(T["boton_entrenar"]):
    with st.spinner(T["spinner_entrenamiento"]):
        modelo_hibrido = ModeloHibrido(modelo_ann, modelo_rf, modelo_xgb, weights_to_use)
        
        # Realizar predicciones de todos los modelos
        y_pred_ann = modelo_ann.predict(X_test).flatten()
        y_pred_rf = modelo_rf.predict(X_test)
        y_pred_xgb = modelo_xgb.predict(X_test)
        y_pred_hibrido = modelo_hibrido.predict(X_test)

        st.success(T["success_entrenamiento"])

        # Guardar el modelo híbrido y sus predicciones en session_state
        st.session_state["modelo_hibrido"] = modelo_hibrido
        st.session_state["y_pred_hibrido"] = y_pred_hibrido
        st.session_state["y_pred_ann"] = y_pred_ann
        st.session_state["y_pred_rf"] = y_pred_rf
        st.session_state["y_pred_xgb"] = y_pred_xgb
        st.session_state["y_test"] = y_test

# Mostrar resultados solo si el modelo híbrido ha sido entrenado
if "modelo_hibrido" in st.session_state:
    y_pred_hibrido = st.session_state["y_pred_hibrido"]
    y_pred_ann = st.session_state["y_pred_ann"]
    y_pred_rf = st.session_state["y_pred_rf"]
    y_pred_xgb = st.session_state["y_pred_xgb"]
    y_test = st.session_state["y_test"]

    # ---------------- Comparación U de Theil ----------------
    st.subheader(T["comparacion_theil"])
    st.markdown(T["info_theil"])

    resultados_u = {
        T["col_modelo"]: ["ANN", "RF", "XGB", T["col_modelo"]], # Usar T["col_modelo"] para "Híbrido"
        T["col_utheil"]: [
            round(theils_u(y_test, y_pred_ann), 4),
            round(theils_u(y_test, y_pred_rf), 4),
            round(theils_u(y_test, y_pred_xgb), 4),
            round(theils_u(y_test, y_pred_hibrido), 4),
        ]
    }

    df_u = pd.DataFrame(resultados_u)

    def resaltar_minimo(df_style):
        # Asegúrate de que 'U de Theil' es el nombre de la columna traducido
        idx_min = df_style.loc[:, T["col_utheil"]].idxmin()
        estilos = pd.DataFrame("", index=df_style.index, columns=df_style.columns)
        estilos.loc[idx_min, :] = "background-color: #d4edda; color: #155724; font-weight: bold;" # Verde claro para resaltar
        return estilos

    st.dataframe(df_u.style.apply(resaltar_minimo, axis=None), use_container_width=True)

    # ---------------- Comparación de Métricas ----------------
    st.subheader(T["comparacion_metricas"])
    st.markdown(T["info_metricas"])

    metricas = {
        T["col_modelo"]: ["ANN", "RF", "XGB", T["col_modelo"]], # Usar T["col_modelo"] para "Híbrido"
        T["col_mae"]: [
            calcular_metricas(y_test, y_pred_ann)["MAE"],
            calcular_metricas(y_test, y_pred_rf)["MAE"],
            calcular_metricas(y_test, y_pred_xgb)["MAE"],
            calcular_metricas(y_test, y_pred_hibrido)["MAE"],
        ],
        T["col_mse"]: [
            calcular_metricas(y_test, y_pred_ann)["MSE"],
            calcular_metricas(y_test, y_pred_rf)["MSE"],
            calcular_metricas(y_test, y_pred_xgb)["MSE"],
            calcular_metricas(y_test, y_pred_hibrido)["MSE"],
        ],
        T["col_r2"]: [
            calcular_metricas(y_test, y_pred_ann)["R²"],
            calcular_metricas(y_test, y_pred_rf)["R²"],
            calcular_metricas(y_test, y_pred_xgb)["R²"],
            calcular_metricas(y_test, y_pred_hibrido)["R²"],
        ]
    }

    df_metricas = pd.DataFrame(metricas)

    def resaltar_metricas(df_style):
        estilos = pd.DataFrame("", index=df_style.index, columns=df_style.columns)
        for col_key in ["col_mae", "col_mse"]: # Usar las claves de traducción
            col_name = T[col_key] # Obtener el nombre de la columna traducido
            idx_min = df_style.loc[:, col_name].idxmin()
            estilos.loc[idx_min, col_name] = "background-color: #d4edda; color: #155724; font-weight: bold;"
        
        col_name_r2 = T["col_r2"] # Obtener el nombre de la columna R² traducido
        idx_max = df_style.loc[:, col_name_r2].idxmax()
        estilos.loc[idx_max, col_name_r2] = "background-color: #d4edda; color: #155724; font-weight: bold;"
        return estilos

    st.dataframe(df_metricas.style.apply(resaltar_metricas, axis=None).format({T["col_mae"]: "{:.4f}", T["col_mse"]: "{:.4f}", T["col_r2"]: "{:.4f}"}), use_container_width=True)

    # ---------------- Diebold-Mariano ----------------
    st.subheader(T["prueba_dm"])
    st.markdown(T["info_dm"])

    combinaciones = [
        ("ANN", y_pred_ann),
        ("RF", y_pred_rf),
        ("XGB", y_pred_xgb),
    ]

    for nombre, y_pred_modelo in combinaciones:
        try:
            dm_stat, p_value = prueba_diebold_mariano(y_test, y_pred_modelo, y_pred_hibrido)
            st.write(f"📎 **{nombre} vs {T['col_modelo']}** → Estadístico DM: `{dm_stat:.4f}`, Valor p: `{p_value:.4f}`")
            if p_value < 0.05:
                st.info(T["dm_resultado_significativo"].format(nombre=nombre))
            else:
                st.info(T["dm_resultado_no_significativo"].format(nombre=nombre))
        except Exception as e:
            st.warning(T["dm_error"].format(nombre=nombre, error=e))

    # ---------------- Guardar Modelo Híbrido ----------------
    st.subheader(T["guardar_modelo"])
    st.markdown(T["info_guardar_modelo"])

    # Crear un archivo temporal para el modelo
    temp_model_dir = Path("temp_models") # Directorio temporal
    temp_model_dir.mkdir(exist_ok=True)
    temp_model_path = temp_model_dir / "modelo_hibrido_entrenado.pkl"

    try:
        joblib.dump(st.session_state["modelo_hibrido"], temp_model_path)
        
        with open(temp_model_path, "rb") as file:
            st.download_button(
                label=T["boton_descargar_modelo"],
                data=file,
                file_name="modelo_hibrido_entrenado.pkl",
                mime="application/octet-stream",
                help=T["help_descargar_modelo"]
            )
        st.info(T["info_modelo_listo"])
    except Exception as e:
        st.error(T["error_preparar_descarga"].format(error=e))
    finally:
        # Asegurarse de que el archivo temporal se elimine después de la descarga
        if temp_model_path.exists():
            os.remove(temp_model_path)
            # Opcional: eliminar el directorio temporal si está vacío
            try:
                os.rmdir(temp_model_dir)
            except OSError:
                pass # El directorio no está vacío, no se elimina
