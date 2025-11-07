import streamlit as st


st.set_page_config(page_title="Gerenciador de Tarefas", layout="centered")


st.sidebar.title(" Navegação")
pagina = st.sidebar.selectbox("Escolha a página:", ["Cadastro de Tarefas", "Listagem de Tarefas"])


if "tarefas" not in st.session_state:
    st.session_state.tarefas = []

if pagina == "Cadastro de Tarefas":
    st.title(" Cadastro de Tarefas")

    nova_tarefa = st.text_input("Digite a nova tarefa:")
    prioridade = st.selectbox("Prioridade:", ["Baixa", "Média", "Alta"])

    if st.button("Adicionar Tarefa"):
        if nova_tarefa.strip():
            st.session_state.tarefas.append({
                "nome": nova_tarefa,
                "prioridade": prioridade
            })
            st.success(f"Tarefa **'{nova_tarefa}'** adicionada com prioridade **{prioridade}**!")
        else:
            st.warning("Digite uma tarefa antes de adicionar.")


elif pagina == "Listagem de Tarefas":
    st.title(" Lista de Tarefas")

    if st.session_state.tarefas:
        for i, tarefa in enumerate(st.session_state.tarefas, start=1):
            st.write(f"**{i}.** {tarefa['nome']} — Prioridade: *{tarefa['prioridade']}*")
    else:
        st.info("Nenhuma tarefa cadastrada ainda.")


    if st.button(" Limpar todas as tarefas"):
        st.session_state.tarefas.clear()
        st.warning("Todas as tarefas foram removidas!")
