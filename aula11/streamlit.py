import streamlit as st

st.title("ola Mundo")
st.header("Cabeçalho principal")

st.text("olá mundo")

nome = st.text_input("Digite seu nome:")
idade = st.number_input("Digite sua idade:",step=1)