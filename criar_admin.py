#Usado para criar um usuário admin no banco de dados
from models import session, Usuario
import streamlit_authenticator as stauth

senha_criptografada = stauth.Hasher(["123123"]).generate()[0]
usuario = Usuario(nome="William", senha=senha_criptografada, email="william@gmail.com", admin=True)

session.add(usuario)
session.commit()

