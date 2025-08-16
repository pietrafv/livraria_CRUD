from . import db

class Autor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    nacionalidade = db.Column(db.String(50))
    idade = db.Column(db.Integer)
    livros = db.relationship('Livro', backref='autor', cascade="all, delete")

class Livro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    ano = db.Column(db.Integer)
    genero = db.Column(db.String(50))
    autor_id = db.Column(db.Integer, db.ForeignKey('autor.id'))
