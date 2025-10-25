import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth
from models import session, Usuario

lista_usuarios = session.query(Usuario).all()

#--------------------------------------------------------------------------------------------------------------------------------------------------
# Parte de Autenticação usando o streamlit_authenticator 

credenciais = {"usernames": 
        {usuario.email: {"name": usuario.nome, "password": usuario.senha} for usuario in lista_usuarios}
}

#Estrutura: credenciais, cookie name, cookie key, cookie expire days
authenticator = stauth.Authenticate(credenciais, "credenciais_hashco3", "123456789abcdefg", cookie_expiry_days=14)

#O authenticator_status pode ter 3 valores: True(caso esteja tudo certo), False(Caso as credenciais esteja errado) e None(Caso não tenha preenchido)
def autenticar_usuario(authenticator):
    nome, authenticator_status, username = authenticator.login()

    if authenticator_status:
        return {"nome": nome, "username": username}
    elif authenticator_status == False:
        st.error("Combinação de usuário e senha inválidas")
    else:
        st.error("Preencha o formulário para fazer login")


def logout():
    authenticator.logout()

dados_usuario = autenticar_usuario(authenticator)

#--------------------------------------------------------------------------------------------------------------------------------------------------

if dados_usuario:
    @st.cache_data
    def carregar_dados():
        tabela = pd.read_excel("Base.xlsx")
        return tabela

    base = carregar_dados()

    email_usuario = dados_usuario["username"]
    usuario = session.query(Usuario).filter_by(email=email_usuario).first()

    if usuario.admin:
        pg = st.navigation(
            {
                "Home": [st.Page("homepage.py", title="Hash&Co")],
                "Dashboard": [st.Page("dashboard.py", title="Dashboard"), st.Page("indicadores.py", title="Indicadores")],
                "Conta": [st.Page(logout, title="Sair"), st.Page("criar_conta.py", title="Criar Conta")] 
            }
        )
    else:
        pg = st.navigation(
            {
                "Home": [st.Page("homepage.py", title="Hash&Co")],
                "Dashboard": [st.Page("dashboard.py", title="Dashboard"), st.Page("indicadores.py", title="Indicadores")],
                "Conta": [st.Page(logout, title="Sair")] 
            }
        )

    #st.title("Hash&Co")
    #st.write("Bem vindo, Fulano")
    #st.table(base.head(10))

    pg.run()


