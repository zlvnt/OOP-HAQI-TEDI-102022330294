SELECT * FROM mahasiswa;

SELECT * FROM mahasiswa WHERE jurusan = 'Sistem Informasi' AND alamat = 'Bandung';

SELECT * FROM mahasiswa WHERE NOT angkatan = '2021';

SELECT nim, nama FROM mahasiswa WHERE angkatan < 2022;

SELECT jurusan, COUNT(*) as total FROM mahasiswa GROUP BY jurusan;

SELECT nama FROM mahasiswa LIMIT 5;

SELECT * FROM mahasiswa WHERE angkatan BETWEEN 2020 AND 2021;

SELECT * FROM mahasiswa WHERE nama LIKE 'andi%';

SELECT DISTINCT jurusan
FROM mahasiswa;

SELECT * 
FROM mahasiswa
ORDER BY jurusan ASC
LIMIT 5

SELECT jurusan, COUNT(*) as jumlah
FROM mahasiswa
GROUP BY jurusan