import streamlit as st

st.title('Hola MUNDOO! :heart:')

st.text_input('Escribe tu email, lindo/a :heart:')

st.balloons()

st.button(label='SUBMIT :sunglasses:')

color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)

