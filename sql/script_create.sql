CREATE DATABASE agencia_viajes;
USE agencia_viajes;

CREATE TABLE rol (
    id_rol INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(20) NOT NULL
);
CREATE TABLE destino(
    id_destino INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(20) NOT NULL,
    descripcion VARCHAR(50),
    precio_base INT NOT NULL,
    is_active BOOLEAN DEFAULT TRUE
);
CREATE TABLE paquete_turistico(
    id_paquete INT PRIMARY KEY AUTO_INCREMENT,
    nombre_paq VARCHAR(30),
    precio INT NOT NULL,
    cupos INT NOT NULL,
    stock BOOLEAN DEFAULT TRUE,
    fecha_ini DATE NOT NULL,
    fecha_fin DATE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE
);
CREATE TABLE usuario(
    id_user INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(12) NOT NULL,
    apellido VARCHAR(12) NOT NULL,
    email VARCHAR(30) NOT NULL,
    passwd VARCHAR(12) NOT NULL,
    fecha_reg TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    id_rol INT,
    is_active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (id_rol) REFERENCES rol(id_rol)
);
CREATE TABLE destino_paquete(
    id_dest_paq INT PRIMARY KEY AUTO_INCREMENT,
    id_destino INT NOT NULL,
    id_paquete INT NOT NULL,
    FOREIGN KEY (id_destino) REFERENCES destino(id_destino),
    FOREIGN KEY (id_paquete) REFERENCES paquete_turistico(id_paquete)
);
CREATE TABLE reserva(
    id_reserva INT PRIMARY KEY AUTO_INCREMENT,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ctd_personas INT NOT NULL,
    precio_pactado INT NOT NULL,
    id_user INT NOT NULL,
    id_paquete INT NOT NULL,
    FOREIGN KEY (id_user) REFERENCES usuario(id_user),
    FOREIGN KEY (id_paquete) REFERENCES paquete_turistico(id_paquete)
);

CREATE INDEX idx_reserva_user ON reserva(id_user);
CREATE INDEX idx_reserva_paquete ON reserva(id_paquete);
CREATE INDEX idx_paquete_active ON paquete_turistico(is_active);