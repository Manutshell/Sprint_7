import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header('Histograma y diagrama de dispersion de anuncios de ventas de coches')

hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
# escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
# crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
# mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    

build_scatter = st.checkbox('Construir un diagrama de dispersión')

if build_scatter: 
    st.write('Creación de diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')

    fig = px.scatter(car_data, y='odometer')

# Mostrar en Streamlit
    st.plotly_chart(fig)