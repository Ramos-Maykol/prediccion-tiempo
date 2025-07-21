import streamlit as st

# Título y botón alineados horizontalmente
col1, col2 = st.columns([8, 2])  # Puedes ajustar las proporciones

with col1:
    st.title("📘 Manual de Usuario")

with col2:
    st.markdown(
        f"""<a href="https://transcendent-rabanadas-4ef4f0.netlify.app/" target="_blank">
                <button style="margin-top: 25px; padding: 0.5em 1em; background-color: #0e76a8; color: white; border: none; border-radius: 5px;">
                    🔗 Redirigir
                </button>
            </a>""",
        unsafe_allow_html=True
    )

# Mostrar el manual embebido
manual_url = "https://transcendent-rabanadas-4ef4f0.netlify.app/"
st.markdown(f'<iframe src="{manual_url}" width="100%" height="800px"></iframe>', unsafe_allow_html=True)
