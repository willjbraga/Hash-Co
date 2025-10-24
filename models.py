from sqlalchemy import create_engine, Integer, String, Boolean, Column
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine("sqlite:///database/meubanco.db")
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column("id", Integer, primary_key = True, autoincrement = True)
    nome = Column("nome", String)
    email = Column("email", String, nullable = True)
    senha = Column("senha", String)
    admin = Column("admin", Boolean)

    def __init__ (self, nome, email, senha, usuario, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.usuario = usuario
        self.admin = admin

Base.metadata.create_all(bind=db)