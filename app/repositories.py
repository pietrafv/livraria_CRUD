from .models import Autor, Livro
from . import db

# CRUD - autores
def criar_autor(autor):
    db.session.add(autor)
    db.session.commit()

def listar_autores():
    return Autor.query.all()

def buscar_autor(id):
    return Autor.query.get(id)

def atualizar_autor(autor):
    db.session.commit()

def deletar_autor(autor):
    db.session.delete(autor)
    db.session.commit()

# CRUD - livros
def criar_livro(livro):
    db.session.add(livro)
    db.session.commit()

def listar_livros():
    return Livro.query.all()

def buscar_livro(id):
    return Livro.query.get(id)

def atualizar_livro(livro):
    db.session.commit()

def deletar_livro(livro):
    db.session.delete(livro)
    db.session.commit()