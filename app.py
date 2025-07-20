import streamlit as st
from utils.lang.textos_app import TEXTOS_APP

# Configuración de la página
st.set_page_config(page_title="Inicio", layout="wide")

# Selección de idioma
st.sidebar.title("🌐 " + TEXTOS_APP["seleccion_idioma"]["es"]) # Título del selector de idioma en español
idioma = st.sidebar.selectbox(
    TEXTOS_APP["subtitulo_idioma"]["es"], # Subtítulo del selector de idioma en español
    ("es", "en", "pt", "fr", "it"),
    format_func=lambda x: {
        "es": "Español",
        "en": "English",
        "pt": "Português",
        "fr": "Français",
        "it": "Italiano"
    }[x]
)

# Atajo para los textos de la UI
T = {key: trans[idioma] for key, trans in TEXTOS_APP.items()}

# Mostrar título y descripción en el idioma seleccionado
st.title(T["titulo"])
st.markdown(T["descripcion"])

# --- Sección de Especificaciones de la Máquina ---
st.markdown("---") # Separador visual
st.subheader(T["especificaciones_maquina_titulo"])
st.markdown(T["especificaciones_maquina_info"])

# Usar un contenedor para simular una "tarjeta"
with st.container(border=True):
    st.markdown(f"- **{T['cpu_label']}**: Intel Core i7-11800H @ 2.30GHz")
    st.markdown(f"- **{T['ram_label']}**: 16 GB DDR4")
    st.markdown(f"- **{T['gpu_label']}**: NVIDIA RTX 3060")

st.markdown("---") # Otro separador visual
