-- Trigger 1
DELIMITER $$

CREATE TRIGGER nilai_pemro
AFTER INSERT ON Nilai_Pemrograman
FOR EACH ROW
BEGIN
    CALL Rata_Mahasiswa_Si();
END$$

DELIMITER ;

-- Trigger 2
DELIMITER $$

CREATE TRIGGER nilai_basdat
AFTER INSERT ON Nilai_Basisdata
FOR EACH ROW
BEGIN
    CALL Rata_Mahasiswa_Si();
END$$

DELIMITER ;

-- Trigger 3
DELIMITER $$

CREATE TRIGGER nilai_okonom
AFTER INSERT ON Nilai_Ekonomi
FOR EACH ROW
BEGIN
    CALL Rata_Mahasiswa_Si();
END$$

DELIMITER ;


-- Store Procedure 1
DELIMITER $$

CREATE PROCEDURE Rata_Mahasiswa_Si()
BEGIN
    DELETE FROM Rata_Nilai_si WHERE NIM IN (
        SELECT NIM FROM Mahasiswa WHERE Asal_Jurusan = 6
    );

    INSERT INTO Rata_Nilai_si (NIM, ratarata_nilai)
    SELECT NIM, AVG(Nilai) as ratarata_nilai
    FROM (
        SELECT NIM, Nilai FROM Nilai_Pemrograman
        UNION ALL
        SELECT NIM, Nilai FROM Nilai_Basisdata
        UNION ALL
        SELECT NIM, Nilai FROM Nilai_Ekonomi
    ) as Semua_Nilai
    WHERE NIM IN (SELECT NIM FROM Mahasiswa WHERE Asal_Jurusan = 6)
    GROUP BY NIM;
END$$

DELIMITER ;


-- Store Procedure 2 (Untuk Melihat Identitas Mahasiswa dan Nilai)
DELIMITER $$

CREATE PROCEDURE Detail_Identitas_dan_Nilai(IN MASUKNIM INT)
BEGIN

    DECLARE rata_rata_nilai VARCHAR(10);

    SELECT IFNULL(CAST(ratarata_nilai AS CHAR), '-') INTO rata_rata_nilai
    FROM Rata_Nilai_si
    WHERE NIM = MASUKNIM;

    SELECT 
        m.NIM, 
        m.Nama, 
        m.Alamat, 
        j.Nama_Jurusan, 
        f.Nama_Fakultas,
        rata_rata_nilai
    FROM 
        Mahasiswa m 
    JOIN 
        Jurusan j ON m.Asal_Jurusan = j.ID_Jurusan
    JOIN 
        Fakultas f ON j.ID_Fakultas = f.ID_Fakultas
    WHERE 
        m.NIM = MASUKNIM;
END$$
     
DELIMITER ;

-- Pemanggilan prosedure identitas mahasiswa dan nilai
CALL Detail_Identitas_dan_Nilai(NIM);

