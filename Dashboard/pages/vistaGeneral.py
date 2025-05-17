import streamlit as st
import plotly.express as px
import pandas as pd
import datetime as dt

st.set_page_config(page_title="Vista General", page_icon="🚥")

st.title("Vista General")
st.write("Contenido de prueba")

#############################################################################
# Carga el archivo
#############################################################################
## Se define la funcion que lee el archivo de excel y lo carga en un dataframe
# Se utiliza el decorador @st.cache_data para almacenar en caché los resultados de la función
# Esto mejora el rendimiento al evitar la lectura repetida del archivo
@st.cache_data
def load_data():
    # Leer todas las hojas del archivo en un diccionario de DataFrames
    # hojas = pd.read_excel(f'../datos_contugas.xlsx',sheet_name=None)
    # Concatenar todas las hojas en un solo DataFrame
    # # Agregamos una columna 'Cliente' con el nombre de la hoja para identificar a cada cliente
    # datos_completos = pd.concat([df.assign(Cliente=nombre) for nombre, df in hojas.items()])
    datos_completos = pd.read_csv(f'../../anomaliasDetectadas.csv',parse_dates=['Fecha'])
    return datos_completos

# Cargar los datos
df = load_data()
lista_clientes = df["Cliente"].unique().tolist()
min_date = df["Fecha"].min()
max_date = df["Fecha"].max()
# Genera los datos para la ultima semana mas reciente
diaAnteriror = max_date - dt.timedelta(days=7)
df_filtrado = df[(df['Fecha'] >= diaAnteriror) & (df['Fecha'] <= max_date)]
# Genera los datos para el ultimo dia
df_dia_f = df[(df['Fecha'] >= max_date)]
df_dia_f["Volumen"] = df_dia_f["Volumen"].round(2)
df_dia_f["Presion"] = df_dia_f["Presion"].round(2)
df_dia_f["Temperatura"] = df_dia_f["Temperatura"].round(2)

# Genera el titulo de la pagina
st.title("Sistema de Alertas de ConGas IA")

# Definir las columnas y su ancho
col1, col2, col3 = st.columns([20, 1, 20])

# Sirve como separador
with col3:
    print('')

with col1:
    with st.expander("Cliente 1",expanded=True):
        col_cliente_1_1, col_cliente_1_2 = st.columns([1, 3])
        with col_cliente_1_1:
            with st.container(border=True,height = 150):
                st.metric(label="Volumen Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 1']['Volumen'], delta=None)
            with st.container(border=True,height = 150):
                st.metric(label="Presion Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 1']['Presion'], delta=None)
            with st.container(border=True,height = 150):
                st.metric(label="Temperatura Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 1']['Temperatura'], delta=None)
        with col_cliente_1_2:
            with st.container(border=True):
                fig_vol_1 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 1'], x="Fecha", y="Volumen", height=120)
                fig_vol_1.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_vol_1, config={"displayModeBar": False})
            with st.container(border=True):
                fig_pres_1 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 1'], x="Fecha", y="Presion", height=120)
                fig_pres_1.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_pres_1, config={"displayModeBar": False})
            with st.container(border=True):
                fig_temp_1 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 1'], x="Fecha", y="Temperatura", height=120)
                fig_temp_1.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_temp_1, config={"displayModeBar": False})
    with st.expander("Cliente 2",expanded=True):
        col_cliente_2_1, col_cliente_2_2 = st.columns([1, 3])
        with col_cliente_2_1:
            with st.container(border=True,height = 150):
                st.metric(label="Volumen Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 2']['Volumen'], delta=None)
            with st.container(border=True,height = 150):
                st.metric(label="Presion Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 2']['Presion'], delta=None)
            with st.container(border=True,height = 150):
                st.metric(label="Temperatura Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 2']['Temperatura'], delta=None)
        with col_cliente_2_2:
            with st.container(border=True):
                fig_vol_2 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 2'], x="Fecha", y="Volumen", height=120)
                fig_vol_2.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_vol_2, config={"displayModeBar": False})
            with st.container(border=True):
                fig_pres_2 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 2'], x="Fecha", y="Presion", height=120)
                fig_pres_2.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_pres_2, config={"displayModeBar": False})
            with st.container(border=True):
                fig_temp_2 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 2'], x="Fecha", y="Temperatura", height=120)
                fig_temp_2.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_temp_2, config={"displayModeBar": False})
    with st.expander("Cliente 3",expanded=True):
        col_cliente_3_1, col_cliente_3_2 = st.columns([1, 3])
        with col_cliente_3_1:
            with st.container(border=True,height = 150):
                st.metric(label="Volumen Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 3']['Volumen'], delta=None)
            with st.container(border=True,height = 150):
                st.metric(label="Presion Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 3']['Presion'], delta=None)
            with st.container(border=True,height = 150):
                st.metric(label="Temperatura Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 3']['Temperatura'], delta=None)
        with col_cliente_3_2:
            with st.container(border=True):
                fig_vol_3 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 3'], x="Fecha", y="Volumen", height=120)
                fig_vol_3.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_vol_3, config={"displayModeBar": False})
            with st.container(border=True):
                fig_pres_3 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 3'], x="Fecha", y="Presion", height=120)
                fig_pres_3.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_pres_3, config={"displayModeBar": False})
            with st.container(border=True):
                fig_temp_3 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 3'], x="Fecha", y="Temperatura", height=120)
                fig_temp_3.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_temp_3, config={"displayModeBar": False})
    with st.expander("Cliente 4",expanded=True):
        col_cliente_4_1, col_cliente_4_2 = st.columns([1, 3])
        with col_cliente_4_1:
            with st.container(border=True,height = 150):
                st.metric(label="Volumen Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 4']['Volumen'], delta=None)
            with st.container(border=True,height = 150):
                st.metric(label="Presion Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 4']['Presion'], delta=None)
            with st.container(border=True,height = 150):
                st.metric(label="Temperatura Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 4']['Temperatura'], delta=None)
        with col_cliente_4_2:
            with st.container(border=True):
                fig_vol_4 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 4'], x="Fecha", y="Volumen", height=120)
                fig_vol_4.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_vol_4, config={"displayModeBar": False})
            with st.container(border=True):
                fig_pres_4 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 4'], x="Fecha", y="Presion", height=120)
                fig_pres_4.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_pres_4, config={"displayModeBar": False})
            with st.container(border=True):
                fig_temp_4 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 4'], x="Fecha", y="Temperatura", height=120)
                fig_temp_4.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_temp_4, config={"displayModeBar": False})
    with st.expander("Cliente 5",expanded=True):
        col_cliente_5_1, col_cliente_5_2 = st.columns([1, 3])
        with col_cliente_5_1:
            with st.container(border=True,height = 150):
                st.metric(label="Volumen Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 5']['Volumen'], delta=None)
            with st.container(border=True,height = 150):
                st.metric(label="Presion Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 5']['Presion'], delta=None)
            with st.container(border=True,height = 150):
                st.metric(label="Temperatura Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 5']['Temperatura'], delta=None)
        with col_cliente_5_2:
            with st.container(border=True):
                fig_vol_5 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 5'], x="Fecha", y="Volumen", height=120)
                fig_vol_5.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_vol_5, config={"displayModeBar": False})
            with st.container(border=True):
                fig_pres_5 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 5'], x="Fecha", y="Presion", height=120)
                fig_pres_5.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_pres_5, config={"displayModeBar": False})
            with st.container(border=True):
                fig_temp_5 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 5'], x="Fecha", y="Temperatura", height=120)
                fig_temp_5.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_temp_5, config={"displayModeBar": False})
    with st.expander("Cliente 6",expanded=True):
        col_cliente_6_1, col_cliente_6_2 = st.columns([1, 3])
        with col_cliente_6_1:
            with st.container(border=True,height = 150):
                st.metric(label="Volumen Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 6']['Volumen'], delta=None)
            with st.container(border=True,height = 150):
                st.metric(label="Presion Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 6']['Presion'], delta=None)
            with st.container(border=True,height = 150):
                st.metric(label="Temperatura Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 6']['Temperatura'], delta=None)
        with col_cliente_6_2:
            with st.container(border=True):
                fig_vol_6 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 6'], x="Fecha", y="Volumen", height=120)
                fig_vol_6.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_vol_6, config={"displayModeBar": False})
            with st.container(border=True):
                fig_pres_6 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 6'], x="Fecha", y="Presion", height=120)
                fig_pres_6.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_pres_6, config={"displayModeBar": False})
            with st.container(border=True):
                fig_temp_6 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 6'], x="Fecha", y="Temperatura", height=120)
                fig_temp_6.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_temp_6, config={"displayModeBar": False})
    with st.expander("Cliente 7",expanded=True):
        col_cliente_7_1, col_cliente_7_2 = st.columns([1, 3])
        with col_cliente_7_1:
            with st.container(border=True,height = 150):
                st.metric(label="Volumen Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 7']['Volumen'], delta=None)
            with st.container(border=True,height = 150):
                st.metric(label="Presion Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 7']['Presion'], delta=None)
            with st.container(border=True,height = 150):
                st.metric(label="Temperatura Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 7']['Temperatura'], delta=None)
        with col_cliente_7_2:
            with st.container(border=True):
                fig_vol_7 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 7'], x="Fecha", y="Volumen", height=120)
                fig_vol_7.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_vol_7, config={"displayModeBar": False})
            with st.container(border=True):
                fig_pres_7 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 7'], x="Fecha", y="Presion", height=120)
                fig_pres_7.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_pres_7, config={"displayModeBar": False})
            with st.container(border=True):
                fig_temp_7 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 7'], x="Fecha", y="Temperatura", height=120)
                fig_temp_7.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_temp_7, config={"displayModeBar": False})
    with st.expander("Cliente 8",expanded=True):
        col_cliente_8_1, col_cliente_8_2 = st.columns([1, 3])
        with col_cliente_8_1:
            with st.container(border=True,height = 150):
                st.metric(label="Volumen Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 8']['Volumen'], delta=None)
            with st.container(border=True,height = 150):
                st.metric(label="Presion Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 8']['Presion'], delta=None)
            with st.container(border=True,height = 150):
                st.metric(label="Temperatura Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 8']['Temperatura'], delta=None)
        with col_cliente_8_2:
            with st.container(border=True):
                fig_vol_8 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 8'], x="Fecha", y="Volumen", height=120)
                fig_vol_8.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_vol_8, config={"displayModeBar": False})
            with st.container(border=True):
                fig_pres_8 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 8'], x="Fecha", y="Presion", height=120)
                fig_pres_8.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_pres_8, config={"displayModeBar": False})
            with st.container(border=True):
                fig_temp_8 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 8'], x="Fecha", y="Temperatura", height=120)
                fig_temp_8.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_temp_8, config={"displayModeBar": False})
    with st.expander("Cliente 9",expanded=True):
        col_cliente_9_1, col_cliente_9_2 = st.columns([1, 3])
        with col_cliente_9_1:
            with st.container(border=True,height = 150):
                st.metric(label="Volumen Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 9']['Volumen'], delta=None)
            with st.container(border=True,height = 150):
                st.metric(label="Presion Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 9']['Presion'], delta=None)
            with st.container(border=True,height = 150):
                st.metric(label="Temperatura Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 9']['Temperatura'], delta=None)
        with col_cliente_9_2:
            with st.container(border=True):
                fig_vol_9 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 9'], x="Fecha", y="Volumen", height=120)
                fig_vol_9.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_vol_9, config={"displayModeBar": False})
            with st.container(border=True):
                fig_pres_9 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 9'], x="Fecha", y="Presion", height=120)
                fig_pres_9.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_pres_9, config={"displayModeBar": False})
            with st.container(border=True):
                fig_temp_9 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 9'], x="Fecha", y="Temperatura", height=120)
                fig_temp_9.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_temp_9, config={"displayModeBar": False})
    with st.expander("Cliente 10",expanded=True):
        col_cliente_10_1, col_cliente_10_2 = st.columns([1, 3])
        with col_cliente_10_1:
            with st.container(border=True,height = 150):
                st.metric(label="Volumen Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 10']['Volumen'], delta=None)
            with st.container(border=True,height = 150):
                st.metric(label="Presion Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 10']['Presion'], delta=None)
            with st.container(border=True,height = 150):
                st.metric(label="Temperatura Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 10']['Temperatura'], delta=None)
        with col_cliente_10_2:
            with st.container(border=True):
                fig_vol_10 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 10'], x="Fecha", y="Volumen", height=120)
                fig_vol_10.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_vol_10, config={"displayModeBar": False})
            with st.container(border=True):
                fig_pres_10 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 10'], x="Fecha", y="Presion", height=120)
                fig_pres_10.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_pres_10, config={"displayModeBar": False})
            with st.container(border=True):
                fig_temp_10 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 10'], x="Fecha", y="Temperatura", height=120)
                fig_temp_10.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_temp_10, config={"displayModeBar": False})

with col3:
    with st.expander("Cliente 11",expanded=True):
        col_cliente_11_1, col_cliente_11_2 = st.columns([1, 3])
        with col_cliente_11_1:
            with st.container(border=True,height = 150):
                st.metric(label="Volumen Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 11']['Volumen'], delta=None)
            with st.container(border=True,height = 150):
                st.metric(label="Presion Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 11']['Presion'], delta=None)
            with st.container(border=True,height = 150):
                st.metric(label="Temperatura Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 11']['Temperatura'], delta=None)
        with col_cliente_11_2:
            with st.container(border=True):
                fig_vol_11 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 11'], x="Fecha", y="Volumen", height=120)
                fig_vol_11.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_vol_11, config={"displayModeBar": False})
            with st.container(border=True):
                fig_pres_11 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 11'], x="Fecha", y="Presion", height=120)
                fig_pres_11.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_pres_11, config={"displayModeBar": False})
            with st.container(border=True):
                fig_temp_11 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 11'], x="Fecha", y="Temperatura", height=120)
                fig_temp_11.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_temp_11, config={"displayModeBar": False})
    with st.expander("Cliente 12",expanded=True):
        col_cliente_12_1, col_cliente_12_2 = st.columns([1, 3])
        with col_cliente_12_1:
            with st.container(border=True,height = 150):
                st.metric(label="Volumen Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 12']['Volumen'], delta=None)
            with st.container(border=True,height = 150):
                st.metric(label="Presion Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 12']['Presion'], delta=None)
            with st.container(border=True,height = 150):
                st.metric(label="Temperatura Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 12']['Temperatura'], delta=None)
        with col_cliente_12_2:
            with st.container(border=True):
                fig_vol_12 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 12'], x="Fecha", y="Volumen", height=120)
                fig_vol_12.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_vol_12, config={"displayModeBar": False})
            with st.container(border=True):
                fig_pres_12 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 12'], x="Fecha", y="Presion", height=120)
                fig_pres_12.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_pres_12, config={"displayModeBar": False})
            with st.container(border=True):
                fig_temp_12 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 12'], x="Fecha", y="Temperatura", height=120)
                fig_temp_12.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_temp_12, config={"displayModeBar": False})
    with st.expander("Cliente 13",expanded=True):
        col_cliente_13_1, col_cliente_13_2 = st.columns([1, 3])
        with col_cliente_13_1:
            with st.container(border=True,height = 150):
                st.metric(label="Volumen Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 13']['Volumen'], delta=None)
            with st.container(border=True,height = 150):
                st.metric(label="Presion Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 13']['Presion'], delta=None)
            with st.container(border=True,height = 150):
                st.metric(label="Temperatura Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 13']['Temperatura'], delta=None)
        with col_cliente_13_2:
            with st.container(border=True):
                fig_vol_13 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 13'], x="Fecha", y="Volumen", height=120)
                fig_vol_13.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_vol_13, config={"displayModeBar": False})
            with st.container(border=True):
                fig_pres_13 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 13'], x="Fecha", y="Presion", height=120)
                fig_pres_13.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_pres_13, config={"displayModeBar": False})
            with st.container(border=True):
                fig_temp_13 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 13'], x="Fecha", y="Temperatura", height=120)
                fig_temp_13.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_temp_13, config={"displayModeBar": False})
    with st.expander("Cliente 14",expanded=True):
        col_cliente_14_1, col_cliente_14_2 = st.columns([1, 3])
        with col_cliente_14_1:
            with st.container(border=True,height = 150):
                st.metric(label="Volumen Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 14']['Volumen'], delta=None)
            with st.container(border=True,height = 150):
                st.metric(label="Presion Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 14']['Presion'], delta=None)
            with st.container(border=True,height = 150):
                st.metric(label="Temperatura Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 14']['Temperatura'], delta=None)
        with col_cliente_14_2:
            with st.container(border=True):
                fig_vol_14 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 14'], x="Fecha", y="Volumen", height=120)
                fig_vol_14.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_vol_14, config={"displayModeBar": False})
            with st.container(border=True):
                fig_pres_14 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 14'], x="Fecha", y="Presion", height=120)
                fig_pres_14.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_pres_14, config={"displayModeBar": False})
            with st.container(border=True):
                fig_temp_14 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 14'], x="Fecha", y="Temperatura", height=120)
                fig_temp_14.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_temp_14, config={"displayModeBar": False})
    with st.expander("Cliente 15",expanded=True):
        col_cliente_15_1, col_cliente_15_2 = st.columns([1, 3])
        with col_cliente_15_1:
            with st.container(border=True,height = 150):
                st.metric(label="Volumen Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 15']['Volumen'], delta=None)
            with st.container(border=True,height = 150):
                st.metric(label="Presion Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 15']['Presion'], delta=None)
            with st.container(border=True,height = 150):
                st.metric(label="Temperatura Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 15']['Temperatura'], delta=None)
        with col_cliente_15_2:
            with st.container(border=True):
                fig_vol_15 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 15'], x="Fecha", y="Volumen", height=120)
                fig_vol_15.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_vol_15, config={"displayModeBar": False})
            with st.container(border=True):
                fig_pres_15 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 15'], x="Fecha", y="Presion", height=120)
                fig_pres_15.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_pres_15, config={"displayModeBar": False})
            with st.container(border=True):
                fig_temp_15 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 15'], x="Fecha", y="Temperatura", height=120)
                fig_temp_15.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_temp_15, config={"displayModeBar": False})
    with st.expander("Cliente 16",expanded=True):
        col_cliente_16_1, col_cliente_16_2 = st.columns([1, 3])
        with col_cliente_16_1:
            with st.container(border=True,height = 150):
                st.metric(label="Volumen Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 16']['Volumen'], delta=None)
            with st.container(border=True,height = 150):
                st.metric(label="Presion Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 16']['Presion'], delta=None)
            with st.container(border=True,height = 150):
                st.metric(label="Temperatura Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 16']['Temperatura'], delta=None)
        with col_cliente_16_2:
            with st.container(border=True):
                fig_vol_16 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 16'], x="Fecha", y="Volumen", height=120)
                fig_vol_16.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_vol_16, config={"displayModeBar": False})
            with st.container(border=True):
                fig_pres_16 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 16'], x="Fecha", y="Presion", height=120)
                fig_pres_16.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_pres_16, config={"displayModeBar": False})
            with st.container(border=True):
                fig_temp_16 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 16'], x="Fecha", y="Temperatura", height=120)
                fig_temp_16.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_temp_16, config={"displayModeBar": False})
    with st.expander("Cliente 17",expanded=True):
        col_cliente_17_1, col_cliente_17_2 = st.columns([1, 3])
        with col_cliente_17_1:
            with st.container(border=True,height = 150):
                st.metric(label="Volumen Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 17']['Volumen'], delta=None)
            with st.container(border=True,height = 150):
                st.metric(label="Presion Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 17']['Presion'], delta=None)
            with st.container(border=True,height = 150):
                st.metric(label="Temperatura Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 17']['Temperatura'], delta=None)
        with col_cliente_17_2:
            with st.container(border=True):
                fig_vol_17 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 17'], x="Fecha", y="Volumen", height=120)
                fig_vol_17.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_vol_17, config={"displayModeBar": False})
            with st.container(border=True):
                fig_pres_17 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 17'], x="Fecha", y="Presion", height=120)
                fig_pres_17.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_pres_17, config={"displayModeBar": False})
            with st.container(border=True):
                fig_temp_17 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 17'], x="Fecha", y="Temperatura", height=120)
                fig_temp_17.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_temp_17, config={"displayModeBar": False})
    with st.expander("Cliente 18",expanded=True):
        col_cliente_18_1, col_cliente_18_2 = st.columns([1, 3])
        with col_cliente_18_1:
            with st.container(border=True,height = 150):
                st.metric(label="Volumen Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 18']['Volumen'], delta=None)
            with st.container(border=True,height = 150):
                st.metric(label="Presion Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 18']['Presion'], delta=None)
            with st.container(border=True,height = 150):
                st.metric(label="Temperatura Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 18']['Temperatura'], delta=None)
        with col_cliente_18_2:
            with st.container(border=True):
                fig_vol_18 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 18'], x="Fecha", y="Volumen", height=120)
                fig_vol_18.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_vol_18, config={"displayModeBar": False})
            with st.container(border=True):
                fig_pres_18 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 18'], x="Fecha", y="Presion", height=120)
                fig_pres_18.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_pres_18, config={"displayModeBar": False})
            with st.container(border=True):
                fig_temp_18 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 18'], x="Fecha", y="Temperatura", height=120)
                fig_temp_18.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_temp_18, config={"displayModeBar": False})
    with st.expander("Cliente 19",expanded=True):
        col_cliente_19_1, col_cliente_19_2 = st.columns([1, 3])
        with col_cliente_19_1:
            with st.container(border=True,height = 150):
                st.metric(label="Volumen Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 19']['Volumen'], delta=None)
            with st.container(border=True,height = 150):
                st.metric(label="Presion Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 19']['Presion'], delta=None)
            with st.container(border=True,height = 150):
                st.metric(label="Temperatura Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 19']['Temperatura'], delta=None)
        with col_cliente_19_2:
            with st.container(border=True):
                fig_vol_19 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 19'], x="Fecha", y="Volumen", height=120)
                fig_vol_19.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_vol_19, config={"displayModeBar": False})
            with st.container(border=True):
                fig_pres_19 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 19'], x="Fecha", y="Presion", height=120)
                fig_pres_19.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_pres_19, config={"displayModeBar": False})
            with st.container(border=True):
                fig_temp_19 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 19'], x="Fecha", y="Temperatura", height=120)
                fig_temp_19.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_temp_19, config={"displayModeBar": False})
    with st.expander("Cliente 20",expanded=True):
        col_cliente_20_1, col_cliente_20_2 = st.columns([1, 3])
        with col_cliente_20_1:
            with st.container(border=True,height = 150):
                st.metric(label="Volumen Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 20']['Volumen'], delta=None)
            with st.container(border=True,height = 150):
                st.metric(label="Presion Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 20']['Presion'], delta=None)
            with st.container(border=True,height = 150):
                st.metric(label="Temperatura Actual:", value=df_dia_f[df_dia_f['Cliente']=='CLIENTE 20']['Temperatura'], delta=None)
        with col_cliente_20_2:
            with st.container(border=True):
                fig_vol_20 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 20'], x="Fecha", y="Volumen", height=120)
                fig_vol_20.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_vol_20, config={"displayModeBar": False})
            with st.container(border=True):
                fig_pres_20 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 20'], x="Fecha", y="Presion", height=120)
                fig_pres_20.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_pres_20, config={"displayModeBar": False})
            with st.container(border=True):
                fig_temp_20 = px.line(df_filtrado[df_filtrado['Cliente']=='CLIENTE 20'], x="Fecha", y="Temperatura", height=120)
                fig_temp_20.update_layout(xaxis_title=None,yaxis_title=None,margin=dict(l=0, r=0, t=0, b=0))
                st.plotly_chart(fig_temp_20, config={"displayModeBar": False})