import streamlit as st

st.title("Conversor de Moedas!")
dolar = st.number_input("dolar",placeholder="Digite o valor em dolar:",step=2)

reais = dolar *5

st.text(f"O valor de {dolar:.2f} dolares é igual a {reais:} Reais.")

