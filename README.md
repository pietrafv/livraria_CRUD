# Breve explicação do projeto

Este projeto é um CRUD de uma livraria, desenvolvido em Flask com banco de dados SQLite usando o SQLAlchemy.

## Entidades:
- Autor: representa um autor de livros, com os seguintes atributos: id, nome, nacionalidade e idade.

- Livro: representa um livro, com os seguintes atributos: id, titulo, ano, genero e autor_id (que é uma chave estrangeira que faz referencia ao autor).

## Relacionamento:
- Um autor pode ter muitos livros (Autor.livros).
- Cada livro pertence a um único autor (Livro.autor).
- O relacionamento é configurado com cascade="all, delete", então, ao deletar um autor, todos os livros associados também são removidos automaticamente.

## Como executar o projeto:
- Crie um ambiente virtual e instale as dependências:
1. python -m venv venv
2. source venv/bin/activate (no Linux) ou venv\Scripts\activate (no Windows)
3. pip install -r requirements.txt

- Inicialize o banco de dados:
1. from app import db
2. db.create_all()

- Execute o servidor Flask:
python run.py

- Acesse a aplicação no navegador em:
http://127.0.0.1:5000

