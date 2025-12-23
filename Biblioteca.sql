CREATE TABLE Autor (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    nacionalidade VARCHAR(50)
);

CREATE TABLE Livro (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    ano_publicacao INTEGER,
    autor_id INTEGER NOT NULL,
    FOREIGN KEY (autor_id) REFERENCES Autor(id) ON DELETE CASCADE
);