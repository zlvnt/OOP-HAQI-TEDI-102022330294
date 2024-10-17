SELECT nim 
FROM mahasiswa 
INNER JOIN nilai_mahasiswa ON mahasiswa.nim = nilai_mahasiswa.nim_mahasiswa;    #inerjoin

SELECT nama
FROM mahasiswa
WHERE nim IN (
    SELECT nim_mahasiswa
    FROM nilai_mahasiswa
    WHERE kode_mata_kuliah = 'mk001' AND nilai < 70 #nested querry
)

SELECT *
FROM mahasiswa
INNER JOIN nilai_mahasiswa ON mahasiswa.nim = nilai_mahasiswa.nim_mahasiswa
WHERE nilai (
    SELECT max(nilai)
    FROM nilai_mahasiswa
    WHERE kode_mata_kuliah = "mk001"
)