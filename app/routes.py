from flask import Blueprint, render_template, request, redirect, url_for
from .models import Autor, Livro
from .repositories import *

bp = Blueprint('routes', __name__)

# autores
@bp.route('/autores')
def listar_autores_view():
    autores = listar_autores()
    return render_template('autores/listar.html', autores=autores)

@bp.route('/autores/criar', methods=['GET','POST'])
def criar_autor_view():
    if request.method == 'POST':
        nome = request.form['nome']
        nacionalidade = request.form['nacionalidade']
        idade = request.form['idade']
        idade = int(idade) if idade else None
        criar_autor(Autor(nome=nome, nacionalidade=nacionalidade, idade=idade))
        return redirect(url_for('routes.listar_autores_view'))
    return render_template('autores/criar.html')

@bp.route('/autores/editar/<int:id>', methods=['GET','POST'])
def editar_autor_view(id):
    autor = buscar_autor(id)
    if request.method == 'POST':
        autor.nome = request.form['nome']
        autor.nacionalidade = request.form['nacionalidade']
        idade = request.form['idade']
        autor.idade = int(idade) if idade else None
        atualizar_autor(autor)
        return redirect(url_for('routes.listar_autores_view'))
    return render_template('autores/editar.html', autor=autor)

@bp.route('/autores/deletar/<int:id>')
def deletar_autor_view(id):
    autor = buscar_autor(id)
    deletar_autor(autor)
    return redirect(url_for('routes.listar_autores_view'))

# livros
@bp.route('/livros')
def listar_livros_view():
    livros = listar_livros()
    return render_template('livros/listar.html', livros=livros)

@bp.route('/livros/criar', methods=['GET','POST'])
def criar_livro_view():
    autores = listar_autores()
    if request.method == 'POST':
        titulo = request.form['titulo']
        ano = request.form['ano']
        ano = int(ano) if ano else None
        genero = request.form['genero']
        autor_id = int(request.form['autor_id'])
        criar_livro(Livro(titulo=titulo, ano=ano, genero=genero, autor_id=autor_id))
        return redirect(url_for('routes.listar_livros_view'))
    return render_template('livros/criar.html', autores=autores)

@bp.route('/livros/editar/<int:id>', methods=['GET','POST'])
def editar_livro_view(id):
    livro = buscar_livro(id)
    autores = listar_autores()
    if request.method == 'POST':
        livro.titulo = request.form['titulo']
        ano = request.form['ano']
        livro.ano = int(ano) if ano else None
        livro.genero = request.form['genero']
        livro.autor_id = int(request.form['autor_id'])
        atualizar_livro(livro)
        return redirect(url_for('routes.listar_livros_view'))
    return render_template('livros/editar.html', livro=livro, autores=autores)

@bp.route('/livros/deletar/<int:id>')
def deletar_livro_view(id):
    livro = buscar_livro(id)
    deletar_livro(livro)
    return redirect(url_for('routes.listar_livros_view'))