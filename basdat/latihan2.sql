CREATE DATABASE Sistem_perpustakaan;

USE sistem_perpustakaan;
CREATE TABLE penerbit(
    kode_penerbit varchar(10) NOT NULL,
    nama_penerbit varchar(30) NOT NULL,
    PRIMARY KEY(kode_penerbit)
);

CREATE TABLE buku(
    kode_buku varchar(10) NOT NULL,
    kode_penerbit varchar(10) NOT NULL,
    FOREIGN KEY(kode_penerbit)
    REFERENCES penerbit(kode_penerbit),
    nama_buku Varchar(50) NOT NULL,
    PRIMARY KEY(kode_buku)
    
);

INSERT INTO penerbit (kode_penerbit, nama_penerbit)
VALUES
('P001', 'Erlangga'),
('P002', 'Mizan Pustaka'),
('B001', 'Gramedia Pustaka');

INSERT INTO buku (kode_buku, kode_penerbit, nama_buku)
VALUES
('A01','B001','Belajar basis data kilat'),
('A02','B001', 'Basis data MySQL'),
('D01','P001', 'Buku Matematika SMA X'),
('H01','P002', 'Tentang Kamu Tere Liye');

INSERT INTO penerbit (kode_penerbit, nama_penerbit)
VALUES
('0294', 'Penerbit 0294');

INSERT INTO buku (kode_buku, kode_penerbit, nama_buku)
VALUES
('F001','0294','Buku Baru 1'),
('F002','0294', 'Buku Baru 2');

UPDATE penerbit
SET nama_penerbit = "Zelvin Thady"
where kode_penerbit = "0294";

SELECT *
FROM buku
WHERE Kode_penerbit <> '0294';

SELECT *
FROM buku
WHERE Kode_penerbit = '0294';

SELECT P.Kode_penerbit AS Nama_penerbit, COUNT(B.Kode_buku) AS Jumlah
FROM buku B
INNER JOIN penerbit P ON B.Kode_penerbit = P.Kode_penerbit
GROUP BY P.Kode_penerbit
ORDER BY P.Nama_penerbit ASC;

DELETE
FROM buku
WHERE kode_penerbit = 'B001';   