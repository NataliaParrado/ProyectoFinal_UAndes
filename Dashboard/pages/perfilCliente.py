import streamlit as st
import plotly.express as px
import pandas as pd
from datetime import date, datetime
import altair as alt

# Genera el titulo de la pagina
st.title("Perfilado del Cliente")

# Valida si hay selecciones guardadas
if "visibility" not in st.session_state:
    st.session_state["visibility"] = 'visible'
if "disabled" not in st.session_state:
    st.session_state["disabled"] = False

# Ruta absoluta a la carpeta donde está este script
base_path = os.path.dirname(os.path.abspath(__file__))
# Ruta al archivo CSV en esa misma carpeta
csv_path = os.path.join(base_path, "anomaliasDetectadas.csv")
def load_data():
    # Leer todas las hojas del archivo en un diccionario de DataFrames
    datos_completos = pd.read_csv(csv_path,parse_dates=['Fecha'])
    return datos_completos

# Definir las columnas y su ancho
col1, col2, col3 = st.columns([2, 1, 4])

# Cargar los datos
datos_completos = load_data()
lista_clientes = datos_completos["Cliente"].unique().tolist()
min_date = datos_completos["Fecha"].min()
max_date = datos_completos["Fecha"].max()

with col1:
    ####################################################################
    # Define los clientes
    ####################################################################
    cliente = st.selectbox(
        "Seleccione el cliente de interes:",
        lista_clientes,
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled)
    datos_cliente = datos_completos[datos_completos['Cliente'] == cliente]

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
    print('')

with col3:
    st.subheader("Resumen del Cliente")
    st.write(f"**ID Cliente:** {datos_cliente['Cliente'].unique()[0]}")
    st.write(f"**Fecha de inicio:** {datos_cliente['Fecha'].min()}")
    st.write(f"**Fecha final:** {datos_cliente['Fecha'].max()}")
    st.write(f"**Total registros:** {len(datos_cliente)}")
    st.subheader("Estadísticas Históricas")
    df_resumen = datos_cliente.drop(columns=["Fecha"]).describe().T
    df_resumen_f = df_resumen[["mean", "std", "min", "max"]].copy()
    df_resumen_f.rename(columns={"mean": "Media", "std": "Desviación Estándar", "min": "Mínimo", "max": "Máximo"}, inplace=True)
    st.dataframe(df_resumen_f)

##################################################################
# Filtra los datos
################################################################
df = datos_cliente[datos_cliente['Cliente'] == cliente]
df = df[(df["Fecha"] >= fecha_min) & (df["Fecha"] <= fecha_max)]
df = df[(df["Volumen"] >= volumen[0]) & (df["Volumen"] <= volumen[1])]
df = df[(df["Temperatura"] >= temperatura[0]) & (df["Temperatura"] <= temperatura[1])]
df = df[(df["Presion"] >= presion[0]) & (df["Presion"] <= presion[1])].sort_values(by="Fecha")
df.reset_index(drop=True, inplace=True)

##############################################################
# Genera visualizaciones
################################################################

## Analisis temporal
st.subheader("Analisis temporal", divider=True)
tab1, tab2, tab3 = st.tabs(["Volumen", "Temperatura", "Presion"])
with tab1:
    st.header("Volumen...")
    # Mostrar la serie de tiempo Volumen
    fig_vol = px.line(df, x="Fecha", y="Volumen")
    df_anomalias_vol = df[df["AnomaliaVolumen"] == True]
    # Agregar puntos rojos por anomalías
    fig_vol.add_scatter(x=df_anomalias_vol["Fecha"],
                     y=df_anomalias_vol["Volumen"],
                     mode="markers",
                     marker=dict(color="red", size=8, symbol="circle"),
                     name="Anomalía")
    st.plotly_chart(fig_vol)
with tab2:
    st.header("Temperatura...")
    # Mostrar la serie de tiempo Temperatura
    fig_temp = px.line(df, x="Fecha", y="Temperatura")
    df_anomaliasTemp = df[df["AnomaliaTemperatura"] == True]
    # Agregar puntos rojos por anomalías
    fig_temp.add_scatter(x=df_anomaliasTemp["Fecha"],
                     y=df_anomaliasTemp["Temperatura"],
                     mode="markers",
                     marker=dict(color="red", size=8, symbol="circle"),
                     name="Anomalía")
    st.plotly_chart(fig_temp)
with tab3:
    st.header("Presion...")
    # Mostrar la serie de tiempo Presion
    fig_pre = px.line(df, x="Fecha", y="Presion")
    df_anomaliasPre = df[df["AnomaliaPresion"] == True]
    fig_pre.add_scatter(x=df_anomaliasPre["Fecha"],
                         y=df_anomaliasPre["Presion"],
                        mode="markers",
                        marker=dict(color="red", size=8, symbol="circle"))
    st.plotly_chart(fig_pre)

# Analisis estadistico
st.subheader("Analisis estadistico", divider=True)
col1_est, col2_est, col3_est = st.columns([5, 1, 5])
with col1_est:
    tab1_est, tab2_est, tab3_est = st.tabs(["Volumen", "Temperatura", "Presion"])
    with tab1_est:
        st.header("Volumen...")
        # Mostrar la serie de tiempo Volumen
        fig_vol_est = px.histogram(df, x="Volumen", marginal="box")
        st.plotly_chart(fig_vol_est)
    with tab2_est:
        st.header("Temperatura...")
        # Mostrar la serie de tiempo Temperatura
        fig_temp_est = px.histogram(df, x="Temperatura", marginal="box")
        st.plotly_chart(fig_temp_est)
    with tab3_est:
        st.header("Presion...")
        # Mostrar la serie de tiempo Presion
        fig_pre_est = px.histogram(df, x="Presion", marginal="box")
        st.plotly_chart(fig_pre_est)
with col2_est:
    print('')
with col3_est:
    st.markdown("*Correlograma:*")
    c = (
        alt.Chart(df)
        .mark_circle()
        .encode(alt.X(alt.repeat("column"), type='quantitative'),
        alt.Y(alt.repeat("row"), type='quantitative')
    ).properties(
        width=150,
        height=150
    ).repeat(
        row=['Volumen', 'Presion', 'Temperatura'],
        column=['Temperatura', 'Presion', 'Volumen']
    ).interactive())
    st.altair_chart(c)

# Analisis temporal
st.subheader("Exploracion de datos", divider=True)
# Mostrar el DataFrame filtrado
df.drop(columns=["Cliente"], inplace=True)
st.dataframe(df, use_container_width=True)


st.dataframe(datos_completos, use_container_width=True)