CREATE DATABASE uts_sisbat;

 CREATE TABLE BRAND(
    id_brand VARCHAR(10) NOT NULL,
    nama_brand VARCHAR(50) NOT NULL,
    PRIMARY KEY(id_brand)
);
 CREATE TABLE KATEGORI(
    id_kategori INT(10) NOT NULL,
    nama_kategori VARCHAR(50) NOT NULL,
    PRIMARY KEY(id_kategori)
);
 CREATE TABLE TOSERBA(
    id_toserba VARCHAR(10) NOT NULL,
    nama_toserba VARCHAR(50) NOT NULL,
    PRIMARY KEY(id_toserba)
);
 CREATE TABLE PELANGGAN(
    id_pelanggan VARCHAR(10) NOT NULL,
    nama_pelanggan VARCHAR(50) NOT NULL,
    no_telepon INT(20) NOT NULL,
    PRIMARY KEY(id_pelanggan)
);
 CREATE TABLE detail_pembayaran(
    id_pembayaran VARCHAR(10) NOT NULL,
    total_pembelian int(20) NOT NULL,
    PRIMARY KEY(id_pembayaran)
);
 CREATE TABLE PRODUK(
    id_produk VARCHAR(10) NOT NULL,
    nama_produk VARCHAR(50) NOT NULL,
    id_brand VARCHAR(10) NOT NULL,
    id_kategori INT(10) NOT NULL,
	PRIMARY KEY(id_produk),
    foreign key(id_brand)
        references BRAND(id_brand),
    foreign key(id_kategori)
        references KATEGORI(id_kategori)
);
 CREATE TABLE pembayaran(
    id_pembayaran VARCHAR(10) NOT NULL,
    id_pelanggan VARCHAR(10) NOT NULL,
    id_produk VARCHAR(10) NOT NULL,
    waktu VARCHAR(20) NOT NULL,
    foreign key(id_pembayaran)
        references detail_pembayaran(id_pembayaran),
    foreign key(id_pelanggan)
        references PELANGGAN(id_pelanggan),
    foreign key(id_produk)
        references produk(id_produk)
);
 CREATE TABLE BARANG_TOSERBA(
    id_toserba VARCHAR(10) NOT NULL,
    id_produk VARCHAR(10) NOT NULL,
    foreign key(id_toserba)
        references TOSERBA(id_toserba),
    foreign key(id_produk)
        references PRODUK(id_produk)
);

INSERT INTO BRAND (id_brand, nama_brand)
VALUES
('INDF', 'INDOFOOD'),
('ABC', 'ABC'),
('NST', 'NESTLE'),
('P&G', 'P&G');

INSERT INTO kategori (id_kategori, nama_kategori)
VALUES
(11, 'Makanan'),
(12, 'Minuman'),
(13, 'Kebutuhan Rumah Tangga'),
(14, 'Kencantikan');

INSERT INTO pelanggan (id_pelanggan, nama_pelanggan, no_telepon)
VALUES
('P1', 'Mamat', 08228495),
('P2', 'Parjo', 08219374);

INSERT INTO toserba (id_toserba, nama_toserba)
VALUES
('1BS', 'Beli Seru'),
('1BJ', 'Budi Jaya');

INSERT INTO detail_pembayaran (id_pembayaran, total_pembelian)
VALUES
('PE1', 0 ),
('PE2', 0 );

INSERT INTO produk (id_produk, nama_produk, id_brand, id_kategori)
VALUES ('IM', 'Indomie', 
        (SELECT id_brand FROM brand WHERE id_brand = 'INDF'), (SELECT id_kategori FROM kategori WHERE id_kategori = 11)),
       ('SRG', 'Sari Gandum', 
        (SELECT id_brand FROM brand WHERE id_brand = 'INDF'), (SELECT id_kategori FROM kategori WHERE id_kategori = 11)),
       ('BVT', 'Buavita', 
        (SELECT id_brand FROM brand WHERE id_brand = 'NST'), (SELECT id_kategori FROM kategori WHERE id_kategori = 12)),
       ('AQ', 'Aqua', 
        (SELECT id_brand FROM brand WHERE id_brand = 'NST'), (SELECT id_kategori FROM kategori WHERE id_kategori = 12)),
       ('BRS', 'Beras', 
        (SELECT id_brand FROM brand WHERE id_brand = 'ABC'), (SELECT id_kategori FROM kategori WHERE id_kategori = 13)),
       ('DGL', 'Daging Olahan', 
        (SELECT id_brand FROM brand WHERE id_brand = 'ABC'), (SELECT id_kategori FROM kategori WHERE id_kategori = 13)),
       ('LPS', 'Lipstik', 
        (SELECT id_brand FROM brand WHERE id_brand = 'P&G'), (SELECT id_kategori FROM kategori WHERE id_kategori = 14));

INSERT INTO pembayaran (id_pelanggan, id_pembayaran, id_produk, waktu)
VALUES ((SELECT id_pelanggan FROM pelanggan WHERE id_pelanggan = 'P1'), (SELECT id_pembayaran FROM detail_pembayaran WHERE id_pembayaran = 'PE1'), (SELECT id_produk FROM produk WHERE id_produk = 'BRS'), '11.45'),
	   ((SELECT id_pelanggan FROM pelanggan WHERE id_pelanggan = 'P1'), (SELECT id_pembayaran FROM detail_pembayaran WHERE id_pembayaran = 'PE1'), (SELECT id_produk FROM produk WHERE id_produk = 'IM'), '11.45'),
       ((SELECT id_pelanggan FROM pelanggan WHERE id_pelanggan = 'P2'), (SELECT id_pembayaran FROM detail_pembayaran WHERE id_pembayaran = 'PE2'), (SELECT id_produk FROM produk WHERE id_produk = 'IM'), '13.21'),
       ((SELECT id_pelanggan FROM pelanggan WHERE id_pelanggan = 'P2'), (SELECT id_pembayaran FROM detail_pembayaran WHERE id_pembayaran = 'PE2'), (SELECT id_produk FROM produk WHERE id_produk = 'BVT'), '13.21'),
       ((SELECT id_pelanggan FROM pelanggan WHERE id_pelanggan = 'P2'), (SELECT id_pembayaran FROM detail_pembayaran WHERE id_pembayaran = 'PE2'), (SELECT id_produk FROM produk WHERE id_produk = 'DGL'), '13.21');

INSERT INTO barang_toserba (id_toserba, id_produk)
VALUES 
 ((SELECT id_toserba FROM toserba WHERE id_toserba = '1BS'), (SELECT id_produk FROM produk WHERE id_produk = 'IM')),
 ((SELECT id_toserba FROM toserba WHERE id_toserba = '1BS'), (SELECT id_produk FROM produk WHERE id_produk = 'AQ')),
 ((SELECT id_toserba FROM toserba WHERE id_toserba = '1BS'), (SELECT id_produk FROM produk WHERE id_produk = 'BVT')),
 ((SELECT id_toserba FROM toserba WHERE id_toserba = '1BS'), (SELECT id_produk FROM produk WHERE id_produk = 'SRG')),
 ((SELECT id_toserba FROM toserba WHERE id_toserba = '1BS'), (SELECT id_produk FROM produk WHERE id_produk = 'BRS')),
 ((SELECT id_toserba FROM toserba WHERE id_toserba = '1BS'), (SELECT id_produk FROM produk WHERE id_produk = 'DGL')),
 ((SELECT id_toserba FROM toserba WHERE id_toserba = '1BS'), (SELECT id_produk FROM produk WHERE id_produk = 'LPS')),
 ((SELECT id_toserba FROM toserba WHERE id_toserba = '1BJ'), (SELECT id_produk FROM produk WHERE id_produk = 'IM')),
 ((SELECT id_toserba FROM toserba WHERE id_toserba = '1BJ'), (SELECT id_produk FROM produk WHERE id_produk = 'SRG')),
 ((SELECT id_toserba FROM toserba WHERE id_toserba = '1BJ'), (SELECT id_produk FROM produk WHERE id_produk = 'BRS')),
 ((SELECT id_toserba FROM toserba WHERE id_toserba = '1BJ'), (SELECT id_produk FROM produk WHERE id_produk = 'DGL'));


     