CREATE SCHEMA monitoreo_precios;
USE monitoreo_precios;
CREATE TABLE personas(
	id INT NOT NULL AUTO_INCREMENT,
	correo VARCHAR(45) NOT NULL,
    pass VARCHAR(45) NOT NULL,
    PRIMARY KEY (id)
);
CREATE TABLE productos(
	id INT NOT NULL AUTO_INCREMENT,
	nombre VARCHAR(500) NOT NULL,
    tienda VARCHAR(20) NOT NULL,
    url VARCHAR(500) NOT NULL,
    PRIMARY KEY (id)
);
CREATE TABLE per_pro(
	id INT NOT NULL AUTO_INCREMENT,
	id_persona INT,
    id_producto INT,
    PRIMARY KEY (id),
    FOREIGN KEY (id_persona) REFERENCES personas(id),
    FOREIGN KEY (id_producto) REFERENCES productos(id)
);
CREATE TABLE precios(
	id INT NOT NULL AUTO_INCREMENT,
    precio BIGINT NOT NULL,
    fecha DATETIME,
    id_producto INT,
    PRIMARY KEY (id),
    FOREIGN KEY (id_producto) REFERENCES productos(id)
);
ALTER TABLE personas ADD CONSTRAINT correo CHECK (correo LIKE '%___@___%');
ALTER TABLE personas ADD UNIQUE(correo);
ALTER TABLE productos ADD UNIQUE(nombre);
ALTER TABLE productos ADD UNIQUE(url);
ALTER TABLE precios MODIFY COLUMN fecha DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP;