CREATE TABLE IF NOT EXISTS paises(
    id INTEGER AUTO_INCREMENT,
    codigo_iso CHAR(3) NOT NULL,
    nombre_pais VARCHAR(60) NOT NULL,
    nacionalidad VARCHAR(60) NULL,

    CONSTRAINT pk_paises PRIMARY KEY(id)
);

ALTER TABLE marcas ADD COLUMN id_pais INTEGER NOT NULL;
ALTER TABLE marcas ADD CONSTRAINT fk_marcas_paises FOREIGN KEY (id_pais) REFERENCES paises(id);