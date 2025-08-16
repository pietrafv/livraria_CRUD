from .repositories import *

def criar_livro_com_autor(titulo, ano, genero, autor_id):
    livro = Livro(titulo=titulo, ano=ano, genero=genero, autor_id=autor_id)
    criar_livro(livro)