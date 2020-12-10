/* EJECUTO ESTAS LINEAS DE SQL EN PHPMYADMIN PARA CREAR LA BASE DE DATOS Y LAS TABLAS QUE VOY A NECESITAR*/
CREATE DATABASE IF NOT EXISTS proyecto_python;
USE proyecto_python;

CREATE table usuarios(
    id          int(255) auto_increment not null,
    nombre      varchar(100) not null,
    apellidos   varchar(255) not null,
    email       varchar(255) not null,
    passwd      varchar(255) not null,
    fecha       date not null,
    CONSTRAINT pk_usuarios PRIMARY KEY(id),
    CONSTRAINT uq_email UNIQUE(email)
)ENGINE=InnoDb;

CREATE table notas(
    id          int(25) auto_increment not null,
    usuario_id  int(255) not null,
    titulo      varchar(255) not null,
    descripcion MEDIUMTEXT,
    fecha       date not null,
    CONSTRAINT pk_notas PRIMARY KEY(id)
    CONSTRAINT fk_nota_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
)ENGINE=InnoDb;