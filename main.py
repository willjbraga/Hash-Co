import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth

#--------------------------------------------------------------------------------------------------------------------------------------------------
# Parte de Autenticação usando o streamlit_authenticator 

senhas_criptografadas = stauth.Hasher(["123", "456", "789"]).generate()

credenciais = {"usernames": {
       "lira@gmail.com": {"name": "Lira", "password": senhas_criptografadas[0]},
       "alon@gmail.com": {"name": "Alon", "password": senhas_criptografadas[1]},
       "amanda@gmail.com": {"name": "Amanda", "password": senhas_criptografadas[2]}
}}

#Estrutura: credenciais, cookie name, cookie key, cookie expire days
authenticator = stauth.Authenticate(credenciais, "credenciais_hashco", "123456789abcdefg", cookie_expiry_days=14)

#O authenticator_status pode ter 3 valores: True(caso esteja tudo certo), False(Caso as credenciais esteja errado) e None(Caso não tenha preenchido)
def autenticar_usuario(authenticator):
    nome, authenticator_status, username = authenticator.login()

    if authenticator_status:
        return {"nome": nome, "username": username}
    elif authenticator_status == False:
        st.error("Combinação de usuário e senha inválidas")
    else:
        st.error("Preencha o formulário para fazer login")


def logout(authenticator):
    authenticator.logout()

dados_usuario = autenticar_usuario(authenticator)

#--------------------------------------------------------------------------------------------------------------------------------------------------

if dados_usuario:
    @st.cache_data
    def carregar_dados():
        tabela = pd.read_excel("Base.xlsx")
        return tabela

    base = carregar_dados()

    pg = st.navigation(
        {
            "Home Page": [st.Page("homepage.py", title="Hash&Co")],
            "Dashboard": [st.Page("dashboard.py", title="Dashboard"), st.Page("indicadores.py", title="Indicadores")],
            "Conta": [st.Page(logout, title="Sair"), st.Page("criar_conta.py", title="Criar Conta")] 
        }
    )

    st.title("Hash&Co")
    st.write("Bem vindo, Fulano")
    st.table(base.head(10))

