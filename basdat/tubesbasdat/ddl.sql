-- Tabel Fakultas
CREATE TABLE Fakultas (
    ID_Fakultas INT PRIMARY KEY,
    Nama_Fakultas VARCHAR(50)
);

-- Tabel Jurusan
CREATE TABLE Jurusan (
    ID_Jurusan INT PRIMARY KEY,
    ID_Fakultas INT,
    Nama_Jurusan VARCHAR(50),
    FOREIGN KEY(ID_Fakultas) REFERENCES Fakultas(ID_Fakultas)
);

-- Tabel Mahasiswa
CREATE TABLE Mahasiswa (
    NIM INT PRIMARY KEY,
    Nama VARCHAR(50),
    Asal_Jurusan INT,
    Alamat VARCHAR(100),
    FOREIGN KEY(Asal_Jurusan) REFERENCES Jurusan(ID_Jurusan)
);

-- Tabel Dosen
CREATE TABLE Dosen (
    NID INT PRIMARY KEY,
    Nama VARCHAR(50),
    Bidang_Keahlian VARCHAR(50)
);

-- Tabel Mata Kuliah
CREATE TABLE Mata_Kuliah (
    ID_MataKuliah INT PRIMARY KEY,
    Nama_Mata_Kuliah VARCHAR(100),
    Jumlah_SKS INT
);

-- Tabel Kelas
CREATE TABLE Kelas (
    ID_Kelas INT PRIMARY KEY,
    ID_Jurusan INT,
    FOREIGN KEY (ID_Jurusan) REFERENCES Jurusan(ID_Jurusan)
);

-- Tabel Nilai Pemrograman
CREATE TABLE Nilai_Pemrograman (
    ID_Nilai_Pemrograman INT AUTO_INCREMENT PRIMARY KEY,
    NIM INT,
    ID_Jurusan INT,
    Nilai FLOAT,
    FOREIGN KEY (NIM) REFERENCES Mahasiswa(NIM),
    FOREIGN KEY (ID_Jurusan) REFERENCES Jurusan(ID_Jurusan)
);

-- Tabel Nilai Basisdata
CREATE TABLE Nilai_Basisdata (
    ID_Nilai_Basisdata INT AUTO_INCREMENT PRIMARY KEY,
    NIM INT,
    ID_Jurusan INT,
    Nilai FLOAT,
    FOREIGN KEY (NIM) REFERENCES Mahasiswa(NIM),
    FOREIGN KEY (ID_Jurusan) REFERENCES Jurusan(ID_Jurusan)
);

-- Tabel Nilai Ekonomi
CREATE TABLE Nilai_Ekonomi (
    ID_Nilai_Ekonomi INT AUTO_INCREMENT PRIMARY KEY,
    NIM INT,
    ID_Jurusan INT,
    Nilai FLOAT,
    FOREIGN KEY (NIM) REFERENCES Mahasiswa(NIM),
    FOREIGN KEY (ID_Jurusan) REFERENCES Jurusan(ID_Jurusan)
);

-- Tabel Rata Nilai
CREATE TABLE Rata_Nilai_si (
    ID_Rata_Nilai INT AUTO_INCREMENT PRIMARY KEY,
    NIM INT,
    ratarata_nilai FLOAT,
    FOREIGN KEY (NIM) REFERENCES Mahasiswa(NIM)
);

-- Tabel Buku
CREATE TABLE Buku (
    ID_Buku INT PRIMARY KEY,
    Nama_Buku VARCHAR(50),
    Genre_Buku VARCHAR(50),
    Stok_Buku INT
);

-- Tabel Peminjaman Buku
CREATE TABLE Peminjaman_Buku (
    ID_Peminjaman INT AUTO_INCREMENT PRIMARY KEY,
    NIM INT,
    Kode_Buku INT,
    Status_Pengembalian ENUM('sudah', 'belum') DEFAULT 'belum',
    FOREIGN KEY (NIM) REFERENCES Mahasiswa(NIM),
    FOREIGN KEY (Kode_Buku) REFERENCES Buku(ID_Buku)
);