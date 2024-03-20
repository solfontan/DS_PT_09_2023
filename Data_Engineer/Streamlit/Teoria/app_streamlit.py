import streamlit as st
import pandas as pd
from PIL import Image

# Set Page Layout
st.set_page_config(layout='wide')

URL = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
titanic = pd.read_csv(URL, index_col='PassengerId')

st.title('Titanic :ship:')
image = Image.open(r'Data_Engineer\Streamlit\Teoria\img\puntos-recarga-madrid.jpg')
st.subheader('La historia del Titanic. El Titanic, transatlántico británico de 46.000 toneladas, se convirtió en el mas grande y lujoso de su época (1911). \
        A pesar de ser considerado insumergible, en el curso de su primer viaje chocó contra un iceberg y se hundió (la noche del 14 al 15 de abril de 1912).')

st.image(image, width=200)
st.text('Datos: ')
st.dataframe(titanic.head())
st.balloons()

# 1. Vamos a mostrar un mapa con las distintas estaciones (st.map) 
# 2. Vamos a mostrar un bar_chart con los cargadores por distrito (st.bar_chart) 
# 3. Vamos a mostrar un bar_chart con los cargadores por operador (st.bar_chart)

st.bar_chart(titanic['Pclass'])