import streamlit as st

# Leemos los datos 
 
# 1. Leeremos los datos exactamente igual que en pandas. (pd.read_csv) 
# 2. Por defecto vamos a leer los datos a través de un path que le pasemos. Pero vamos 
# a darle la opción al usuario para que introduzca el archivo que le de la gana. 
# (st.file_uploader) 
# 3. Para celebrar que hemos leído los datos vamos a lanzar unos globos (st.balloons) 
 
 
# Creamos la home 
 
# 1. Vamos a poner una cabecera (st.title) 
# 2. Vamos a cargar una imagen (st.image) 
# 3. Vamos a escribir una pequeña descripción... pero tampoco me apetece que se vea 
# siempre (st.write / st.beta_expander) 
# 4. Vamos a mostrar los datos que hemos leído, pero además queremos que se vea con 
# el código que necesitamos para imprimir los datos (st.dataframe / st.echo) 
# 5. Ostia los globos se lanzan tela veces... que esta pasando? (st.cache) 
 
 
# Vamos a crear visualizaciones 
 
# 1. Vamos a mostrar un mapa con las distintas estaciones (st.map) 
# 2. Vamos a mostrar un bar_chart con los cargadores por distrito (st.bar_chart) 
# 3. Vamos a mostrar un bar_chart con los cargadores por operador (st.bar_chart)

st.title('esto es un titulo')

st.subheader('esto es un subheader')

st.text('esto es un texto')

st.text('esto se puede usar para otras cosas')