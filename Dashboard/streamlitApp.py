import streamlit as st
import pandas as pd

st.set_page_config(page_title="ConGas IA", page_icon=":material/edit:",layout="wide")
st.title("Vista General")
st.write("Contenido de la vista general.")
st.sidebar.success("Select a demo above.")

# Define las hojas de la aplicación
#vistaGeneral = st.Page("vistaGeneral.py", title="Vista General", icon="🚥")
#perfilCliente = st.Page("perfilCliente.py", title="Perfil Cliente", icon="🧑‍🏫")
#analisisAnomalias = st.Page("analisisAnomalias.py", title="Analisis Anomalias", icon="📊")
#exploracionDatos = st.Page("exploracionDatos.py", title="Exploracion de Datos", icon="📊")

# Define la navegacion de las hojas
#pg = st.navigation([vistaGeneral, perfilCliente, analisisAnomalias])
#pg.run()