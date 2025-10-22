import streamlit as st

st.title("Calculadora de IMC!")

peso = st.number_input("Digite seu peso:", step=1)
altura = st.number_input("Digite sua altura: ",min_value=0.1)

calculo = peso/altura**2

st.text(f"Seu IMC é: {calculo:.2f} ")