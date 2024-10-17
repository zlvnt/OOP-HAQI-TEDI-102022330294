CREATE DATABASE resto_db;

USE resto_db;
 CREATE TABLE pelanggan(
    id_pelanggan int NOT NULL,
    nama_pelanggan VARCHAR(50) NOT NULL,
    alamat_pelanggan VARCHAR(50) NOT NULL,
    primary key(id_pelanggan)
);
 CREATE TABLE Menu(
    id_menu int not null,
    nama_menu varchar(50) not null,
    harga_menu varchar(50) not null,
    primary key(id_menu)
);
 CREATE TABLE pesan(
    id_pelanggan INT NOT NULL,
    id_menu INT NOT NULL,
    foreign key(id_pelanggan)
        references pelanggan(id_pelanggan),
    foreign key(id_menu)
        references menu(id_menu)
);
     
ALTER TABLE pelanggan CHANGE nama_pelanggan nama varchar(50);