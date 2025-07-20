# pages/2_Predicción.py
import streamlit as st
import pandas as pd
from utils.loader import cargar_modelos, cargar_scaler
import numpy as np # Importar numpy para flatten si es necesario para ANN
from utils.pdf_generator_prediccion import PredictionPDFGenerator # Importar el generador de PDF
from utils.lang.textos_prediccion_ui import TEXTOS_PREDICCION_UI # NUEVO: Importar textos para la UI

st.set_page_config(layout="wide") # Configurar el layout de la página a ancho completo para una mejor visualización

# --- Selección de Idioma en la barra lateral ---
st.sidebar.title("⚙️ Opciones de Idioma")
LANGUAGE_OPTIONS = {
    "es": "Español 🇪🇸", "en": "English 🇬🇧", "pt": "Português 🇧🇷",
    "fr": "Français 🇫🇷", "it": "Italiano 🇮🇹"
}
idioma_seleccionado = st.sidebar.selectbox(
    TEXTOS_PREDICCION_UI["seleccione_idioma"]["es"], # Usar español para la etiqueta del selector de idioma
    options=list(LANGUAGE_OPTIONS.keys()),
    format_func=lambda code: LANGUAGE_OPTIONS[code]
)

# Atajo para los textos de la UI en el idioma seleccionado
T = {key: trans[idioma_seleccionado] for key, trans in TEXTOS_PREDICCION_UI.items()}

st.title(T["titulo_app"])

st.markdown(T["intro_app"])

# Cargar todos los modelos y scaler
# Asegúrate de que cargar_modelos() devuelve los tres modelos en el orden esperado
try:
    modelo_ann, modelo_rf, modelo_xgb = cargar_modelos()
    scaler = cargar_scaler()
except Exception as e:
    st.error(f"{T['error_carga_modelos']} {e}")
    st.stop() # Detener la ejecución si los modelos no se cargan

# Diccionario de modelos para fácil acceso
modelos = {
    "Random Forest": modelo_rf,
    "Red Neuronal ANN": modelo_ann,
    "XGBoost": modelo_xgb
}

# Etiquetas en español para los inputs (estas son las claves internas, no las mostradas en UI)
# Las etiquetas mostradas en la UI se obtendrán de T[]
etiquetas_internas = {
    'Machine ID': 'ID de Máquina',
    'Units Produced': 'Unidades Producidas',
    'Defects': 'Número de Defectos',
    'Labour Cost Per Hour': 'Costo Mano de Obra por Hora (S/.)',
    'Energy Consumption kWh': 'Consumo de Energía (kWh)',
    'Operator Count': 'Cantidad de Operarios',
    'Maintenance Hours': 'Horas de Mantenimiento',
    'Down time Hours': 'Horas de Inactividad',
    'Production Volume Cubic Meters': 'Volumen de Producción (m³)',
    'Scrap Rate': 'Tasa de Desecho',
    'Rework Hours': 'Horas de Retrabajo',
    'Quality Checks Failed': 'Controles de Calidad Fallidos',
    'Average Temperature C': 'Temperatura Promedio (°C)',
    'Average Humidity Percent': 'Humedad Promedio (%)'
}

# Valores por defecto para los inputs (algunos son fijos, otros editables)
valores_defecto = {
    'Machine ID': 3,
    'Units Produced': 120,
    'Defects': 2,
    'Labour Cost Per Hour': 12.5,
    'Energy Consumption kWh': 220,
    'Operator Count': 4,
    'Maintenance Hours': 0.8,
    'Down time Hours': 1.2,
    'Production Volume Cubic Meters': 0.95,
    'Scrap Rate': 0.015,
    'Rework Hours': 0.5,
    'Quality Checks Failed': 1,
    'Average Temperature C': 23.0, # Cambiado a float
    'Average Humidity Percent': 58.0, # Cambiado a float
    'Product Type': 'Electrónica',
    'Shift': 'Tarde'
}

# Opciones de tipo de producto y turnos (para One-Hot Encoding)
tipos_producto = {
    'Automotriz': [1, 0, 0, 0], # Product Type_Automotive
    'Electrónica': [0, 1, 0, 0], # Product Type_Electronics
    'Muebles': [0, 0, 1, 0],    # Product Type_Furniture
    'Textiles': [0, 0, 0, 1]    # Product Type_Textiles
}

turnos = {
    'Día': {'Shift_Night': 0, 'Shift_Swing': 0}, # Asumiendo 'Día' es la categoría base
    'Tarde': {'Shift_Night': 0, 'Shift_Swing': 1}, # Asumiendo 'Tarde' es 'Swing'
    'Noche': {'Shift_Night': 1, 'Shift_Swing': 0}
}

# --- Formulario de Predicción ---
with st.form("form_prediccion_tiempo"):
    st.subheader(T["configuracion_prediccion"])

    # Selección del modelo
    modelo_seleccionado_nombre = st.selectbox(
        T["seleccione_modelo"],
        options=list(modelos.keys()),
        index=0, # Por defecto, "Random Forest"
        help=T["help_modelo"]
    )
    st.markdown("---") # Separador visual

    st.subheader(T["ingrese_parametros"])
    st.markdown(T["ajuste_parametros"])

    datos = {}

    # Sección: Parámetros de Producción
    st.markdown(T["parametros_produccion"])
    col1, col2, col3 = st.columns(3)
    with col1:
        datos['Machine ID'] = st.number_input(
            etiquetas_internas['Machine ID'], # Usar etiqueta interna para el key, mostrar traducción
            value=valores_defecto['Machine ID'],
            step=1,
            min_value=1,
            help=T["help_machine_id"]
        )
    with col2:
        datos['Units Produced'] = st.number_input(
            etiquetas_internas['Units Produced'],
            value=valores_defecto['Units Produced'],
            step=1,
            min_value=1,
            help=T["help_units_produced"]
        )
    with col3:
        datos['Operator Count'] = st.number_input(
            etiquetas_internas['Operator Count'],
            value=valores_defecto['Operator Count'],
            step=1,
            min_value=1,
            help=T["help_operator_count"]
        )
    
    # Valores fijos que no se muestran como input al usuario
    datos['Defects'] = valores_defecto['Defects']
    datos['Maintenance Hours'] = valores_defecto['Maintenance Hours']
    datos['Rework Hours'] = valores_defecto['Rework Hours']
    datos['Energy Consumption kWh'] = valores_defecto['Energy Consumption kWh']
    datos['Down time Hours'] = valores_defecto['Down time Hours']
    datos['Production Volume Cubic Meters'] = valores_defecto['Production Volume Cubic Meters']


    # Sección: Parámetros de Calidad y Ambiente
    st.markdown(T["parametros_calidad_ambiente"])
    col4, col5, col6 = st.columns(3)
    with col4:
        datos['Scrap Rate'] = st.number_input(
            etiquetas_internas['Scrap Rate'],
            value=valores_defecto['Scrap Rate'],
            min_value=0.0,
            max_value=1.0,
            step=0.001,
            format="%.3f",
            help=T["help_scrap_rate"]
        )
    with col5:
        datos['Quality Checks Failed'] = st.number_input(
            etiquetas_internas['Quality Checks Failed'],
            value=valores_defecto['Quality Checks Failed'],
            step=1,
            min_value=0,
            help=T["help_quality_checks_failed"]
        )
    with col6:
        datos['Average Temperature C'] = st.number_input(
            etiquetas_internas['Average Temperature C'],
            value=valores_defecto['Average Temperature C'],
            step=0.1,
            help=T["help_avg_temp_c"]
        )
    datos['Average Humidity Percent'] = st.number_input(
        etiquetas_internas['Average Humidity Percent'],
        value=valores_defecto['Average Humidity Percent'],
        step=0.1,
        help=T["help_avg_humidity_percent"]
    )
    datos['Labour Cost Per Hour'] = st.number_input(
        etiquetas_internas['Labour Cost Per Hour'],
        value=valores_defecto['Labour Cost Per Hour'],
        step=0.1,
        help=T["help_labour_cost_per_hour"]
    )

    # Sección: Tipo de Producto y Turno
    st.markdown(T["tipo_producto_turno"])
    col7, col8 = st.columns(2)
    with col7:
        tipo_producto = st.selectbox(
            T["tipo_producto_label"],
            list(tipos_producto.keys()),
            index=list(tipos_producto.keys()).index(valores_defecto['Product Type']),
            help=T["help_tipo_producto"]
        )
    with col8:
        turno = st.selectbox(
            T["turno_label"],
            list(turnos.keys()),
            index=list(turnos.keys()).index(valores_defecto['Shift']),
            help=T["help_turno"]
        )

    submitted = st.form_submit_button(T["boton_predecir"])

# Procesar predicción
if submitted:
    # Obtener el modelo seleccionado
    modelo_a_usar = modelos[modelo_seleccionado_nombre]

    # Preparar los datos para la predicción
    dummies_producto = tipos_producto[tipo_producto]
    
    # Generar los dummies de turno basados en el diccionario 'turnos'
    shift_dummies_dict = turnos[turno]
    shift_night_val = shift_dummies_dict.get('Shift_Night', 0)
    shift_swing_val = shift_dummies_dict.get('Shift_Swing', 0)

    # Capturar los valores de los inputs (editables) y los valores por defecto (fijos)
    # Crear un diccionario para los parámetros de entrada que se mostrarán en el PDF
    input_parameters_for_pdf = {
        'Machine ID': datos['Machine ID'],
        'Units Produced': datos['Units Produced'],
        'Operator Count': datos['Operator Count'],
        'Scrap Rate': datos['Scrap Rate'],
        'Quality Checks Failed': datos['Quality Checks Failed'],
        'Average Temperature C': datos['Average Temperature C'],
        'Average Humidity Percent': datos['Average Humidity Percent'],
        'Labour Cost Per Hour': datos['Labour Cost Per Hour'],
        'Defects': valores_defecto['Defects'],
        'Maintenance Hours': valores_defecto['Maintenance Hours'],
        'Rework Hours': valores_defecto['Rework Hours'],
        'Energy Consumption kWh': valores_defecto['Energy Consumption kWh'],
        'Down time Hours': valores_defecto['Down time Hours'],
        'Production Volume Cubic Meters': valores_defecto['Production Volume Cubic Meters'],
        'Product Type': tipo_producto, # Añadir el tipo de producto seleccionado
        'Shift': turno # Añadir el turno seleccionado
    }


    datos_numericos = [
        datos['Machine ID'], datos['Units Produced'], datos['Defects'],
        datos['Labour Cost Per Hour'], datos['Energy Consumption kWh'],
        datos['Operator Count'], datos['Maintenance Hours'],
        datos['Down time Hours'], datos['Production Volume Cubic Meters'],
        datos['Scrap Rate'], datos['Rework Hours'],
        datos['Quality Checks Failed'], datos['Average Temperature C'],
        datos['Average Humidity Percent']
    ]

    datos_completos_lista = datos_numericos + dummies_producto + [shift_night_val, shift_swing_val]

    # Orden de las columnas según el entrenamiento del modelo
    # Es CRUCIAL que este orden coincida EXACTAMENTE con el orden de las características
    # que fueron usadas para entrenar los modelos.
    orden_columnas_final = [
        'Machine ID', 'Units Produced', 'Defects', 'Labour Cost Per Hour',
        'Energy Consumption kWh', 'Operator Count', 'Maintenance Hours',
        'Down time Hours', 'Production Volume Cubic Meters', 'Scrap Rate',
        'Rework Hours', 'Quality Checks Failed', 'Average Temperature C',
        'Average Humidity Percent',
        'Product Type_Automotive', 'Product Type_Electronics',
        'Product Type_Furniture', 'Product Type_Textiles',
        'Shift_Night', 'Shift_Swing' # Estas son las columnas dummy si 'Day' es la base
    ]

    nuevo_producto_df = pd.DataFrame([datos_completos_lista], columns=orden_columnas_final)

    # Escalar los datos de entrada
    nuevo_producto_scaled = scaler.transform(nuevo_producto_df)

    # Realizar la predicción con el modelo seleccionado
    if modelo_seleccionado_nombre == "Red Neuronal ANN":
        tiempo_estimado = modelo_a_usar.predict(nuevo_producto_scaled).flatten()
    else:
        tiempo_estimado = modelo_a_usar.predict(nuevo_producto_scaled)

    st.success(T["prediccion_exitosa"].format(modelo=modelo_seleccionado_nombre, tiempo=tiempo_estimado[0]))

    # --- Generar y ofrecer el PDF ---
    st.markdown("---")
    st.subheader(T["reporte_pdf_titulo"])
    st.info(T["info_descarga_pdf"])
    try:
        # Pasar el idioma y los datos de entrada a la clase PredictionPDFGenerator
        pdf_generator = PredictionPDFGenerator(lang=idioma_seleccionado)
        pdf_filename = f"reporte_prediccion_{modelo_seleccionado_nombre.replace(' ', '_').lower()}.pdf"
        pdf_path = pdf_generator.create_pdf(tiempo_estimado[0], modelo_seleccionado_nombre, input_parameters_for_pdf, etiquetas_internas, pdf_filename)

        with open(pdf_path, "rb") as pdf_file:
            st.download_button(
                label=T["boton_descargar_pdf"],
                data=pdf_file,
                file_name=pdf_filename,
                mime="application/pdf"
            )
    except Exception as e:
        st.error(T["error_generar_pdf"].format(error=e))
