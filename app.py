import pandas as pd
import streamlit as st
import plotly.express as px

# importar los datos desde el archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# solo para verificar que los datos se cargaron correctamente
print(car_data.info())

# Encabezado de la aplicación
st.header('Análisis Exploratorio de Datos (EDA) con Streamlit')
st.write('Selecciona los gráficos que deseas visualizar:')

# Casilla de verificación para mostrar el dataset
show_data = st.checkbox('Mostrar Datos del Dataset')

if show_data:  # Si la casilla de mostrar datos está marcada
    st.write('Mostrando las primeras 100 filas del dataset:')
    # Muestra las primeras 100 filas para no sobrecargar
    st.dataframe(car_data.head(100))
    st.success('Datos del dataset mostrados con éxito!')

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

# Casilla de verificación para el gráfico de tipos de vehículos por fabricante
show_vehicle_types_by_manufacturer = st.checkbox(
    'Mostrar Tipos de Vehículos por Fabricante')

if show_vehicle_types_by_manufacturer:  # Si la casilla está marcada
    st.write(
        'Creación de un gráfico de barras apiladas de tipos de vehículos por fabricante:')
    fig_bar = px.histogram(car_data, x="manufacturer", color="type",
                           title="Tipos de Vehículos por Fabricante",
                           barmode="stack")  # barmode="stack" para barras apiladas
    st.plotly_chart(fig_bar, use_container_width=True)
    st.success('Gráfico de tipos de vehículos por fabricante creado con éxito!')

# Casilla de verificación para el histograma de condición vs año del modelo
show_condition_vs_year_histogram = st.checkbox(
    'Mostrar Histograma de Condición vs Año del Modelo')

if show_condition_vs_year_histogram:  # Si la casilla está marcada
    st.write(
        'Creación de un histograma de la condición del vehículo por año del modelo:')
    fig_condition_year = px.histogram(car_data, x="model_year", color="condition",
                                      title="Histograma de Condición vs Año del Modelo",
                                      barmode="stack")  # Para apilar las barras por condición
    st.plotly_chart(fig_condition_year, use_container_width=True)
    st.success('Histograma de condición vs año del modelo creado con éxito!')

# Nueva sección para comparar la distribución de precios entre fabricantes
st.subheader('Comparar Distribución de Precios entre Fabricantes')

# Obtener la lista única de fabricantes para los selectores
manufacturer_list = sorted(car_data['manufacturer'].dropna().unique())

# Selectores para elegir los fabricantes
selected_manufacturer_1 = st.selectbox(
    'Selecciona el fabricante 1:',
    options=manufacturer_list,
    index=manufacturer_list.index(
        'chevrolet') if 'chevrolet' in manufacturer_list else 0
)

selected_manufacturer_2 = st.selectbox(
    'Selecciona el fabricante 2:',
    options=manufacturer_list,
    index=manufacturer_list.index('bmw') if 'bmw' in manufacturer_list else 1
)

# Casilla de verificación para normalizar el histograma
normalize_histogram = st.checkbox('Normalizar Histograma')

# Filtrar los datos para los fabricantes seleccionados
filtered_data_compare = car_data[
    (car_data['manufacturer'] == selected_manufacturer_1) |
    (car_data['manufacturer'] == selected_manufacturer_2)
]

# Crear el histograma de comparación
if not filtered_data_compare.empty:
    # Determinar si se debe normalizar
    hist_norm_mode = 'percent' if normalize_histogram else None

    fig_compare_price = px.histogram(
        filtered_data_compare,
        x="price",
        color="manufacturer",
        title=f"Distribución de Precios: {selected_manufacturer_1} vs {selected_manufacturer_2}",
        barmode="overlay",  # Para superponer los histogramas
        histnorm=hist_norm_mode  # Normaliza a porcentaje si la casilla está marcada
    )
    st.plotly_chart(fig_compare_price, use_container_width=True)
    st.success('Gráfico de comparación de precios creado con éxito!')
else:
    st.warning(
        "No hay datos disponibles para la combinación de fabricantes seleccionada.")
