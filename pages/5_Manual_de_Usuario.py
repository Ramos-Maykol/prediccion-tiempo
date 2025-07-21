import streamlit as st

st.title("📘 Manual de Usuario")
manual_url = "https://transcendent-rabanadas-4ef4f0.netlify.app/"  # Cambia esto por tu URL real
st.markdown(f'<iframe src="{manual_url}" width="100%" height="800px"></iframe>', unsafe_allow_html=True)
