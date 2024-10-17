-- Trigger 4
DELIMITER $$

CREATE TRIGGER Pinjambuku
AFTER INSERT ON Peminjaman_Buku
FOR EACH ROW
BEGIN
    UPDATE Buku
    SET Stok_Buku = Stok_Buku - 1
    WHERE ID_Buku = NEW.Kode_Buku;
END$$

DELIMITER ;

-- Triger 5
DELIMITER $$

CREATE TRIGGER Kembalibuku
AFTER UPDATE ON Peminjaman_Buku
FOR EACH ROW
BEGIN
    IF OLD.Status_Pengembalian = 'belum' AND NEW.Status_Pengembalian = 'sudah' THEN
        UPDATE Buku
        SET Stok_Buku = Stok_Buku + 1
        WHERE ID_Buku = NEW.Kode_Buku;
    END IF;
END$$

DELIMITER ;

--Triger 6
DELIMITER $$

CREATE TRIGGER HapusData
AFTER DELETE ON Peminjaman_Buku
FOR EACH ROW
BEGIN
    IF OLD.Status_Pengembalian = 'belum' THEN
        UPDATE Buku
        SET Stok_Buku = Stok_Buku + 1
        WHERE ID_Buku = OLD.Kode_Buku;
    END IF;
END$$

DELIMITER ;



-- Store Procedure 3
DELIMITER $$

CREATE PROCEDURE PinjamBuku (
    IN MASUKNIM INT,
    IN MASUKIDBUKU INT
)
BEGIN
    INSERT INTO Peminjaman_Buku (NIM, Kode_Buku)
    VALUES (MASUKNIM, MASUKIDBUKU);
END$$

DELIMITER ;

-- Pemanggilan prosedure peminjaman buku
CALL PinjamBuku(NIM, ID_Buku);

-- Store Procedure 4
DELIMITER $$

CREATE PROCEDURE PengembalianBuku (
    IN MASUKNIM INT,
    IN MASUKIDBUKU INT
)
BEGIN
    UPDATE Peminjaman_Buku
    SET Status_Pengembalian = 'sudah'
    WHERE ID_Peminjaman = (
        SELECT ID_Peminjaman
        FROM (
            SELECT ID_Peminjaman
            FROM Peminjaman_Buku
            WHERE NIM = MASUKNIM 
              AND Kode_Buku = MASUKIDBUKU 
              AND Status_Pengembalian = 'belum'
            LIMIT 1
        ) AS UbahStatus
    );
END$$

DELIMITER ;

-- Pemanggilan prosedure pengembalian buku
CALL PengembalianBuku(NIM, ID_Buku);


