# 🎓📚 BIBLIOTECA-MVC
### *CRUD de Autores e Livros — Python + MVC + PostgreSQL*

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?logo=python" />
  <img src="https://img.shields.io/badge/PostgreSQL-12+-blue?logo=postgresql" />
  <img src="https://img.shields.io/badge/Status-Ativo-success" />
  <img src="https://img.shields.io/badge/Arquitetura-MVC-important" />
  <img src="https://img.shields.io/badge/Plataforma-CLI-lightgrey" />
</p>

---

# 📑 Sumário

- [✨ Sobre o Projeto](#-sobre-o-projeto)
- [🚀 Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [📦 Pré-requisitos](#-pré-requisitos)
- [📥 Instalação do Projeto](#-instalação-do-projeto)
- [🗄 Configuração do Banco PostgreSQL](#-configuração-do-banco-postgresql)
- [⚙ Arquivo de Conexão](#-arquivo-de-conexão)
- [▶ Como Executar](#-como-executar)
- [📂 Estrutura do Projeto](#-estrutura-do-projeto)

---

## ✨ Sobre o Projeto

Este é um sistema de biblioteca universitária desenvolvido em **Python** com arquitetura **MVC**, utilizando **PostgreSQL** para persistência dos dados.

Funcionalidades principais:

- Cadastro de autores (nome + nacionalidade)   
- Cadastro de livros (título + ano de publicação + autor)  
- Listagem de autores  
- Listagem de livros  

---

## 🚀 Tecnologias Utilizadas

- 🐍 Python 3.8+    
- 🐘 PostgreSQL    
- 🔌 psycopg2  
- 🧱 Arquitetura MVC  
- 🖥 Interface de linha de comando (CLI)

---

## 📦 Pré-requisitos

Python 3.8+  
PostgreSQL 12+  
psycopg2  
Git (opcional)  

## 📥 Instalação do Projeto

1️⃣ Clone o repositório
https://github.com/MeirejaneChaves605/BIBLIOTECA-MVC.git
cd BIBLIOTECA-MVC

2️⃣ Crie o ambiente virtual (opcional)
python -m venv venv

Ativar no Windows:

venv\Scripts\activate


Ativar no Linux/macOS:

source venv/bin/activate

3️⃣ Instale as dependências
pip install -r requirements.txt


Se o arquivo não existir:

pip install psycopg2

## 🗄 Configuração do Banco PostgreSQL
🔧 Criar banco de dados  
CREATE DATABASE biblioteca;  

🔧 Criar usuário (opcional)  
CREATE USER biblioteca_user WITH PASSWORD 'senha123';  
GRANT ALL PRIVILEGES ON DATABASE biblioteca TO biblioteca_user;  

🔧 Criar as tabelas  
CREATE TABLE autor (  
    id SERIAL PRIMARY KEY,  
    nome VARCHAR(150) NOT NULL,  
    nacionalidade VARCHAR(100) NOT NULL  
);

CREATE TABLE livro (  
    id SERIAL PRIMARY KEY,  
    titulo VARCHAR(200) NOT NULL,  
    ano_publicacao INT NOT NULL,  
    id_autor INTEGER NOT NULL REFERENCES autor(id)  
);

## ⚙ Arquivo de Conexão

Edite models/conexao.py conforme seu ambiente:

DB_CONFIG = {  
    "host": "localhost",  
    "port": 5432,  
    "dbname": "biblioteca",  
    "user": "biblioteca_user",  
    "password": "senha123"  
}

## ▶ Como Executar

python main.py


O menu permitirá:

➕ Cadastrar autor  

➕ Cadastrar livro  

📄 Listar autores  

📄 Listar livros  

❌ Sair  

## 📂 Estrutura do Projeto
Sistema-de-Biblioteca-Universit-ria/  
├── controllers/  
│   ├── autor_controller.py  
│   ├── livro_controller.py  
├── models/  
│   ├── autor.py  
│   ├── livro.py  
│   ├── conexao.py  
├── views/  
│   ├── autor_view.py  
│   ├── livro_view.py  
│   ├── menu_view.py  
├── main.py  
├── README.md  
└── requirements.txt  

