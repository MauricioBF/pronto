CREATE TABLE 'CartoonFunny'

CREATE TABLE 'Personagens' (
    'ID_Personagem' INTEGER,
    'Criador' VARCHAR,
    'Descricao' VARCHAR,
    'Especie' VARCHAR,
    'Nome' VARCHAR
);
 
ALTER TABLE 'Personagens' ADD CONSTRAINT 'ID_Personagem' PRIMARY KEY ('ID_Personagem');

CREATE TABLE 'PersonagemDesenho' (
    'ID_Personagem',
    'ID_Desenho'
);
 
ALTER TABLE 'PersonagemDesenho' ADD CONSTRAINT 'FK_PersonagemDesenho_1'
    FOREIGN KEY ('ID_Personagem', 'ID_Desenho')
    REFERENCES 'Personagem'('ID_Personagem');
    REFERENCES 'Desenho'('ID_Desenho');

CREATE TABLE 'Desenho' (
    'Nome' VARCHAR,
    'Autor' VARCHAR,
    'Genero' VARCHAR,
    'Sinopse' VARCHAR,
    'ID_Desenho' INTEGER PRIMARY KEY,
    'Criador' VARCHAR,
    'ID_Episodio'
);
 
ALTER TABLE 'Desenho' ADD CONSTRAINT 'FK_Desenho_2'
    FOREIGN KEY ('ID_Episodio')
    REFERENCES 'Episodio'('ID_Episodio');

CREATE TABLE 'Episodio' (
    'Data_Lancamento' DATE,
    'Duracao' INTEGER,
    'Sinopse' VARCHAR,
    'ID_Episodio' INTEGER PRIMARY KEY,
    'Temporada' NUMERIC,
    'Nome' VARCHAR,
    'ID_Desenho'
);
 
ALTER TABLE 'Episodio' ADD CONSTRAINT 'FK_Episodio_2'
    FOREIGN KEY ('ID_Desenho')
    REFERENCES 'Desenho'('ID_Desenho');