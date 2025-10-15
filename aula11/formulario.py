import streamlit as st
lista_usuarios=[]
st.title("Formulário")

nome = st.text_input("Nome",placeholder="Digite seu nome:")
Idade = st.number_input("Idade",placeholder="Digite sua idade:")
task = st.checkbox("Estou estudando em casa!")
color = st.color_picker("Escolha uma cor")
stacks = st.selectbox("Escolha as stacks", ["backand", "Frontand", "fullstack","Estagiário"])
on = st.toggle("ligar")
print(on)
if on:
    st.write("Modo Dark")
else:
    st.write("Modo Write")
print(color)

def clicar_botao():
    lista_usuarios.append(nome)

def listar_tarefas():
    pass

botao = st.button("Enviar", type="primary", on_click=clicar_botao)
visualizar_tarefas = st.button("Visualizar",on_click=listar_tarefas)