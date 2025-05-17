import streamlit as st
import plotly.express as px
import pandas as pd
from datetime import date, datetime
from vistaGeneral import load_data

# Genera el titulo de la pagina
st.title("Exploracion de Datos")

# Valida si hay selecciones guardadas
if "visibility" not in st.session_state:
    st.session_state["visibility"] = 'visible'
if "disabled" not in st.session_state:
    st.session_state["disabled"] = False

# Definir las columnas y su ancho
col1, col2 = st.columns([2, 4])

# Cargar los datos
datos_completos = load_data()
lista_clientes = datos_completos["Cliente"].unique().tolist()
min_date = datos_completos["Fecha"].min()
max_date = datos_completos["Fecha"].max()

with col1:
    ####################################################################
    # Define los clientes
    ####################################################################
    cliente = st.multiselect(
        "Seleccione los clientes de interes:",
        lista_clientes,
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled)
    if cliente:
        None
    else:
        cliente = lista_clientes
    datos_cliente = datos_completos[datos_completos['Cliente'].isin(cliente)]

    ####################################################################
    # Define las fechas
    ####################################################################
    fecha = st.date_input(
        label="Seleccione el rango de fechas de interes:",
        value = (min_date, max_date),
        min_value = min_date,
        max_value = max_date,
        format="MM.DD.YYYY")
    if (len(fecha) == 1):
        fecha_min = datetime.combine(fecha[0], datetime.min.time())
        fecha_max = datetime.combine(fecha[0], datetime.min.time())
    elif (fecha[0] > fecha[1]) or (fecha[0] == fecha[1]):
        fecha_min = datetime.combine(fecha[0], datetime.min.time())
        fecha_max = datetime.combine(fecha[0], datetime.min.time())
        fecha_max = fecha_min
    elif (fecha[0] < fecha[1]):
        fecha_min = datetime.combine(fecha[0], datetime.min.time())
        fecha_max = datetime.combine(fecha[1], datetime.min.time())

    ####################################################################
    # Define el rango de valores en la variable Volumen
    ####################################################################
    volumen = st.slider(
        label="Seleccione el rango del volumen de interes:",
        min_value=float(datos_cliente['Volumen'].min()),
        max_value=float(datos_cliente['Volumen'].max()),
        value=(0.0, float(datos_cliente['Volumen'].max())))

    ####################################################################
    # Define el rango de valores en la variable Presion
    ####################################################################
    presion = st.slider(
        label="Seleccione el rango de la presion de interes:",
        min_value=float(datos_cliente['Presion'].min()),
        max_value=float(datos_cliente['Presion'].max()),
        value=(0.0, float(datos_cliente['Presion'].max())))

    ####################################################################
    # Define el rango de valores en la variable Temperatura
    ####################################################################
    temperatura = st.slider(
        label="Seleccione el rango de la temperatura de interes:",
        min_value=float(datos_cliente['Temperatura'].min()),
        max_value=float(datos_cliente['Temperatura'].max()),
        value=(0.0, float(datos_cliente['Temperatura'].max())))

with col2:
    st.dataframe(datos_completos)

fig_box_vol = px.box(datos_cliente, x="Cliente", y="Volumen")
st.plotly_chart(fig_box_vol)