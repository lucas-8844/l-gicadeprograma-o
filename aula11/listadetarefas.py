import streamlit as st
st.session_state.lista_tarefas = []
st.header("Gerenciador de Tarefas")
tarefas = st.text_input("Digite o nome da tarefa:")

def clicar_botao():
    st.session_state.lista_tarefas.append(tarefas)


botao = st.button("Enviar", type="primary", on_click=clicar_botao)

titulo_2 = st.header("Lista:")

def listar_tarefas():
     if st.session_state.lista_tarefas:
          for i, t in enumerate(st.session_state.lista_tarefas, start=1):
            st.write(f"{i}. {t}")
     else:
         st.info("Nenhuma tarefa adicionada")

visualizar_tarefas = st.button("Visualizar",on_click=listar_tarefas)
