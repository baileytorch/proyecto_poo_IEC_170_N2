CREATE TABLE IF NOT EXISTS combustibles(
    id INT AUTO_INCREMENT,
    tipo_combustible VARCHAR(25),
    descripcion_tipo_combustible VARCHAR(255),

    CONSTRAINT pk_combustible PRIMARY KEY (id)
);

ALTER TABLE modelos ADD COLUMN tipo_combustible INT NOT NULL;
ALTER TABLE modelos ADD COLUMN puertas INT NOT NULL;
ALTER TABLE modelos ADD CONSTRAINT fk_modelos_combustibles FOREIGN KEY (tipo_combustible) REFERENCES combustibles(id);