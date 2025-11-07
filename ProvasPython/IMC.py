import streamlit as st


st.set_page_config(page_title="Calculadora de IMC", page_icon="💪", layout="centered")


st.title(" Calculadora de IMC")
st.write("Descubra seu **Índice de Massa Corporal (IMC)** e veja em qual faixa você se encontra!")


st.subheader(" Insira seus dados abaixo:")
peso = st.number_input("Digite seu peso (kg):", min_value=0.0, step=0.1, format="%.1f")
altura = st.number_input("Digite sua altura (m):", min_value=0.0, step=0.01, format="%.2f")


if st.button("Calcular IMC"):
    if peso > 0 and altura > 0:
        imc = peso / (altura ** 2)
        
        
        if imc < 18.5:
            nivel = "Abaixo do peso"
            mensagem = " Você está abaixo do peso ideal. Que tal conversar com um nutricionista?"
        elif imc < 24.9:
            nivel = "Peso normal"
            mensagem = " Parabéns! Seu peso está dentro da faixa considerada saudável."
        elif imc < 29.9:
            nivel = "Sobrepeso"
            mensagem = " Atenção! Você está com sobrepeso. Pequenas mudanças na rotina podem ajudar."
        elif imc < 34.9:
            nivel = "Obesidade Grau I"
            mensagem = " Cuidado! É importante adotar hábitos mais saudáveis e fazer acompanhamento médico."
        elif imc < 39.9:
            nivel = "Obesidade Grau II"
            mensagem = " Risco elevado. Procure orientação profissional para cuidar da sua saúde."
        else:
            nivel = "Obesidade Grau III"
            mensagem = " Nível grave! Busque orientação médica o quanto antes."

        
        st.success(f"**Seu IMC é:** {imc:.2f}")
        st.info(f"**Classificação:** {nivel}")
        st.write(mensagem)

        
        st.markdown("---")
        st.caption("📘 Referência: Organização Mundial da Saúde (OMS)")
        st.markdown("""
        | Faixa de IMC | Classificação |
        |---------------|----------------|
        | Abaixo de 18.5 | Abaixo do peso |
        | 18.5 – 24.9 | Peso normal |
        | 25.0 – 29.9 | Sobrepeso |
        | 30.0 – 34.9 | Obesidade Grau I |
        | 35.0 – 39.9 | Obesidade Grau II |
        | 40.0 ou mais | Obesidade Grau III |
        """)
    else:
        st.warning("Por favor, insira valores válidos de **peso** e **altura**.")
