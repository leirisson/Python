CREATE DATABASE IF NOT EXISTS cinema;

USE cinema;

CREATE TABLE IF NOT EXISTS filmes (
	titulo VARCHAR(50) NOT NULL,
    genero VARCHAR(30) NOT NULL,
    ano INT NOT NULL,
    PRIMARY KEY (titulo)
);


INSERT INTO filmes (titulo, genero, ano)
VALUE ("Flores Gump", "Drama", 1994);
INSERT INTO filmes (titulo, genero, ano)
VALUE ("Flores Gump2", "Drama", 2000);

