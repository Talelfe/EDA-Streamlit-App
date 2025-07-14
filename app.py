import pandas as pd
import streamlit as st
import plotly.express as px

# importar los datos desde el archivo CSV
car_data = pd.read_csv('notebooks/vehicles_us.csv')
# solo para verificar que los datos se cargaron correctamente
print(car_data.info())

# Encabezado de la aplicación
st.header('Análisis Exploratorio de Datos (EDA) con Streamlit')
st.write('Selecciona los gráficos que deseas visualizar:')

# Casilla de verificación para el histograma
show_histogram = st.checkbox('Mostrar Histograma de Odómetro')

if show_histogram:  # Si la casilla del histograma está marcada
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches:')
    # crear un histograma
    fig = px.histogram(car_data, x="odometer",
                       title="Distribución del Odómetro")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    # mostrar un mensaje de éxito
    st.success('Histograma creado con éxito!')

# Casilla de verificación para el gráfico de dispersión
show_scatter = st.checkbox(
    'Mostrar Gráfico de Dispersión (Odómetro vs. Precio)')

if show_scatter:  # Si la casilla del gráfico de dispersión está marcada
    # escribir un mensaje en la aplicación
    st.write(
        'Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches:')
    # crear un gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price",
                             title="Relación entre el Odómetro y el Precio")
    # mostrar el gráfico de dispersión
    st.plotly_chart(fig_scatter, use_container_width=True)
    # mostrar un mensaje de éxito
    st.success('Gráfico de dispersión creado con éxito!')
