import streamlit as st
st.title("Evolución de ventas")

entrada=st.text_input("Ingrese los datos separados por coma:",value="18,15,18,26,31")
entrada2=entrada.split(",")

serie=[float(i) for i in entrada2]
st.line_chart(serie)



