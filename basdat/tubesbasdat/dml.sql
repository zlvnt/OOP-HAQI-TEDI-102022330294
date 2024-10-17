-- Insert data into Fakultas
INSERT INTO Fakultas (ID_Fakultas, Nama_Fakultas) VALUES 
(1, 'Fakultas Teknik'),
(2, 'Fakultas Ekonomi'),
(3, 'Fakultas Ilmu Komputer'),
(4, 'Fakultas Kedokteran'),
(5, 'Fakultas Hukum'),
(6, 'Fakultas Kesehatan Masyarakat'),
(7, 'Fakultas Sastra'),
(8, 'Fakultas Pertanian'),
(9, 'Fakultas Psikologi'),
(10, 'Fakultas Seni Rupa dan Desain');

-- Insert data into Jurusan
INSERT INTO Jurusan (ID_Jurusan, ID_Fakultas, Nama_Jurusan) VALUES 
(1, 1, 'Teknik Elektro'),
(2, 10, 'DKV'),
(3, 2, 'Akuntansi'),
(4, 2, 'Manajemen'),
(5, 3, 'Informatika'),
(6, 3, 'Sistem Informasi'),
(7, 4, 'Kedokteran Umum'),
(8, 8, 'Agribisnis'),
(9, 5, 'Ilmu Hukum'),
(10, 6, 'Ilmu Gizi');

-- Insert data into Mahasiswa
INSERT INTO Mahasiswa (NIM, Nama, Asal_Jurusan, Alamat) VALUES 
(555721, 'Puspa Nurdiyanti', 1, 'Jl. Merdeka No. 1'),
(555115, 'Budi', 2, 'Jl. Sudirman No. 2'),
(555706, 'Sadina Agustina', 3, 'Jl. Gatot Subroto No. 3'),
(555868, 'Purwa Budiyanto', 4, 'Jl. Thamrin No. 4'),
(555325, 'Eka Permata', 5, 'Jl. Juanda No. 5'),
(555044, 'Cayadi Simanjuntak', 6, 'Jl. Kuningan No. 6'),
(555185, 'Rahayu Widiastuti', 7, 'Jl. Senayan No. 7'),
(555246, 'Drajat Firmansyah', 8, 'Jl. Fatmawati No. 8'),
(555750, 'Ika', 9, 'Jl. Blok M No. 9'),
(555437, 'Shania Riyanti', 10, 'Jl. Mangga Dua No. 10'),
(555047, 'Roki Derung', 6, 'Jl. Jawa No. 10'),
(555055, 'Anes Beswiden', 6, 'Jl. Mawar No. 15'),
(555069, 'Janggar Kranowo', 6, 'Jl. Lintas Barat Sumatera No. 10'),
(555088, 'Stevanyoung', 6, 'Jl. Bojongsoang'),
(555020, 'Radwin Kawil', 6, 'Jl. Padang No. 2');

-- Insert data into Dosen
INSERT INTO Dosen (NID, Nama, Bidang_Keahlian) VALUES 
(847, 'Dr. Surya', 'Agronomi'),
(730, 'Dr. Ratna', 'Termodinamika'),
(855, 'Dr. Siti', 'Akuntansi Keuangan'),
(647, 'Dr. Ali', 'Manajemen Bisnis'),
(837, 'Dr. Budi', 'Algoritma'),
(246, 'Dr. Dian', 'Basis Data'),
(738, 'Dr. Eka', 'Kesehatan Umum'),
(934, 'Dr. Fahmi', 'Linguistik'),
(467, 'Dr. Gani', 'Hukum Pidana'),
(619, 'Dr. Hana', 'Gizi Masyarakat');

-- Insert data into Mata_Kuliah
INSERT INTO Mata_Kuliah (ID_MataKuliah, Nama_Mata_Kuliah, Jumlah_SKS) VALUES 
(067, 'Telekomunikasi', 3),
(670, 'Kritik Sastra', 3),
(635, 'Akuntansi Dasar', 3),
(871, 'Pengantar Bisnis', 3),
(649, 'Pemrograman', 4),
(118, 'Sistem Basis Data', 3),
(513, 'Anatomi Manusia', 4),
(729, 'Fisiologi Tanaman', 4),
(791, 'Hukum Tata Negara', 3),
(967, 'Manajemen Pelayanan Kesehatan', 2);

-- Insert data into Kelas
INSERT INTO Kelas (ID_Kelas, ID_Jurusan) VALUES 
(23, 1),
(46, 2),
(98, 3),
(43, 4),
(10, 5),
(75, 6),
(77, 6),
(76, 6),
(29, 9),
(15, 10);

-- Insert data into Nilai_Pemrograman
INSERT INTO Nilai_Pemrograman (NIM, ID_Jurusan, Nilai) VALUES 
(555721, 1, 85.0),
(555115, 2, 88.5),
(555706, 3, 90.0),
(555868, 4, 75.5),
(555325, 5, 92.0),
(555044, 6, 78.0),
(555069, 6, 80.0),
(555246, 8, 85.0),
(555055, 6, 88.0),
(555047, 6, 91.0),
(555088, 6, 75.0),
(555020, 6, 90.0);

-- Insert data into Nilai_Basisdata
INSERT INTO Nilai_Basisdata (NIM, ID_Jurusan, Nilai) VALUES 
(555721, 1, 82.0),
(555088, 6, 84.5),
(555706, 3, 87.0),
(555868, 4, 73.5),
(555325, 5, 89.0),
(555044, 6, 75.0),
(555020, 6, 79.0),
(555069, 6, 82.0),
(555055, 6, 86.0),
(555047, 6, 90.0);

-- Insert data into Nilai_Ekonomi
INSERT INTO Nilai_Ekonomi (NIM, ID_Jurusan, Nilai) VALUES 
(555721, 1, 80.0),
(555088, 6, 83.5),
(555706, 3, 85.0),
(555868, 4, 70.5),
(555325, 5, 87.0),
(555044, 6, 73.0),
(555020, 6, 77.0),
(555246, 8, 80.0),
(555750, 9, 84.0),
(555069, 6, 89.0),
(555055, 6, 85.0),
(555047, 6, 95.0);

-- Insert data into Buku
INSERT INTO Buku (ID_Buku, Nama_Buku, Genre_Buku, Stok_Buku) VALUES 
(5001, 'Pemrograman Dasar', 'Teknologi', 10),
(5002, 'Pengantar Akuntansi', 'Ekonomi', 5),
(5003, 'Fisika untuk Teknik', 'Sains', 7),
(5004, 'Kesehatan Gigi', 'Kedokteran', 3),
(5005, 'Hukum Pidana', 'Hukum', 4),
(5006, 'Dasar Manajemen', 'Bisnis', 6),
(5007, 'Algoritma dan Pemrograman', 'Teknologi', 8),
(5008, 'Kesehatan Umum', 'Kedokteran', 2),
(5009, 'Komunikasi Massa', 'Sosial', 9),
(5010, 'Psikologi Umum', 'Psikologi', 10),
(5011, '5 cm', 'Novel', 5),
(5012, 'Black Swan', 'Sains', 2),
(5013, 'Filosofi Teras', 'Self Improvement', 4),
(5014, 'the richest man in babylon', 'Self Improvement', 3);
