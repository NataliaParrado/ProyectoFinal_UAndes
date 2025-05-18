import streamlit as st
import pandas as pd
import os

base_path = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(base_path, "image_proyectoFinal.png")

st.set_page_config(page_title="ConGas IA", page_icon=":material/edit:",layout="wide")
st.title("Bienvenido a la Aplicación de ConGas IA")

# Definir las columnas y su ancho
col1, col2, col3 = st.columns([20, 1, 20])

# Sirve como separador
with col2:
    print('')

with col1:
    st.image(img_path, use_container_width=True)
    st.write("""ConGas IA \n
             Aplicación de análisis de datos de consumo de gas \n
             Versión 1.0""")
    st.write("Desarrollado por: Grupo ConGas")
    st.write("Fecha: 2023-10-01")
with col3:
    st.write("Esta aplicación está diseñada para ayudar a los usuarios a explorar y analizar datos relacionados con el consumo de gas.")
    st.write("Utiliza el menú de la barra lateral para navegar entre las diferentes secciones de la aplicación.")
    st.write("ConGas IA es una aplicación que permite a los usuarios explorar y analizar datos relacionados con el consumo de gas.")
    st.write("La aplicación ofrece una interfaz intuitiva y fácil de usar, lo que facilita la navegación y la comprensión de los datos.")
    st.write("Los usuarios pueden seleccionar diferentes clientes, rangos de fechas y valores de interés para obtener información detallada sobre el consumo de gas.")
    st.write("La aplicación también incluye gráficos interactivos y visualizaciones para ayudar a los usuarios a comprender mejor los datos.")
    st.write("ConGas IA es una herramienta valiosa para cualquier persona interesada en el consumo de gas y su análisis.")