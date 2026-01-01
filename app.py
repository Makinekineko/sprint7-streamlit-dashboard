import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Sprint 7 Dashboard", layout="wide")

st.header("Sprint 7 — Dashboard de anuncios de coches")

# Cargar datos
@st.cache_data
def load_data():
    return pd.read_csv("vehicles_us.csv")

df = load_data()

st.write("Vista previa del dataset:")
st.dataframe(df.head())

# Columnas numéricas
numeric_cols = df.select_dtypes(include="number").columns.tolist()

st.subheader("Visualizaciones")

# Histograma
build_hist = st.checkbox("Construir histograma")
if build_hist:
    col = st.selectbox("Columna para histograma", numeric_cols)
    fig_hist = px.histogram(df, x=col)
    st.plotly_chart(fig_hist, use_container_width=True)

# Dispersión
build_scatter = st.checkbox("Construir gráfico de dispersión")
if build_scatter:
    x_col = st.selectbox("Eje X", numeric_cols, key="x")
    y_col = st.selectbox("Eje Y", numeric_cols, key="y")
    fig_scatter = px.scatter(df, x=x_col, y=y_col)
    st.plotly_chart(fig_scatter, use_container_width=True)