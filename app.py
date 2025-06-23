import streamlit as st
import pandas as pd
import plotly.express as px

# Encabezado de la aplicación
st.header("Análisis de vehículos en EE.UU.")

# Leer el archivo CSV
df = pd.read_csv("vehicles_us.csv")

# Crear botón para construir histograma
if st.button("Construir histograma"):
    st.write("Histograma de kilometraje (odometer)")
    fig_hist = px.histogram(df, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

# Crear botón para construir gráfico de dispersión
if st.button("Construir gráfico de dispersión"):
    st.write("Gráfico de dispersión entre odómetro y precio")
    fig_scatter = px.scatter(df, x="odometer", y="price")
    st.plotly_chart(fig_scatter, use_container_width=True)
    