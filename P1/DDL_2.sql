DROP TABLE IF EXISTS NascidoEm CASCADE;
DROP TABLE IF EXISTS ExisteEm CASCADE;
DROP TABLE IF EXISTS AlergicoA CASCADE;

CREATE TABLE NascidoEm (
	personagem		VARCHAR(20),
	planeta		VARCHAR(20),

	CONSTRAINT ne_pk PRIMARY KEY (personagem)
);

CREATE TABLE ExisteEm (
	flor			VARCHAR(20),
	planeta			VARCHAR(20),
	
	CONSTRAINT ee_pk PRIMARY KEY (flor)
);

CREATE TABLE AlergicoA (
	personagem		VARCHAR(20),
	flor		VARCHAR(20),
	
	CONSTRAINT aa_pk PRIMARY KEY (personagem, flor)
);