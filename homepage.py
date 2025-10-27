import streamlit as st


coluna_esquerda, coluna_direita =  st.columns([1, 1.5])

# tudo que era st."alguma coisa" vira coluna_esquerda pois estára na minha coluna esquerda

coluna_esquerda.title("Hash&Co")
coluna_esquerda.write("#### Bem vindo, Fulano")

botao_dashboard = coluna_esquerda.button("Dashboards Projetos")
botao_indicadores = coluna_esquerda.button("Principais indicadores")
#-----------------------------------------------------------------------------------------------



if botao_dashboard:
    st.switch_page("dashboard.py")

if botao_indicadores:
    st.switch_page("indicadores.py")

container = coluna_direita.container(border=True)
container.image("imagens/time-comunidade.webp")