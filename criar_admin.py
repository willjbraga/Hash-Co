#Usado para criar um usuário admin no banco de dados
from models import session, Usuario
import streamlit_authenticator as stauth

senha_criptografada = stauth.Hasher(["1231234"]).generate()[0]
usuario = Usuario(nome="Lira", senha=senha_criptografada, email="lira@gmail.com", admin=False)

session.add(usuario)
session.commit()

