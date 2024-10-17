#import library sqlite 3 dan maplotlib
import sqlite3
import matplotlib.pyplot as plt
from prettytable import PrettyTable

#buatlah database yang dapat diakses secara keseluruhan

db = "LATIHAN.sqlite3"

#Buatlah fungsi untuk membuat tabel
def buattabel(): 
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute  ("""CREATE TABLE IF NOT EXISTS daftar_obat(id_obat INTEGER
                primary key, nama TEXT not null,harga INTEGER not
                null, stok INTEGER not null, jenis_obat TEXT not null)""")
    conn.commit()
    c.close()
    print("Tabel berhasil dibuat")
    pass

#Buatlah fungsi untuk menambahkan obat
def tambah_obat(id_obat, nama, harga, stok, jenis_obat):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute ("""INSERT INTO
    daftar_obat (id_obat, nama, harga, stok, jenis_obat)
    VALUES(?,?,?,?,?)""",(id_obat, nama, harga, stok, jenis_obat))
    conn.commit()
    print('Obat berhasil ditambahkan')
    conn.close()
    pass
    
#Buatlah fungsi untuk hapus obat berdasarkan id obat
def hapus_obat():
    conn = sqlite3.connect(db)
    c = conn.cursor()
    id_obat = int(input("Masukkan ID obat yang akan dihapus: "))
    c.execute("DELETE FROM daftar_obat WHERE id_obat=?", (id_obat,))
    conn.commit()
    print('Obat berhasil dihapus!')
    conn.close()
    pass
    
#Buatlah fungsi untuk mencari obat berdasarkan id
def cari_obat(id_obat : int):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute(
    f"""SELECT * FROM daftar_obat WHERE nama LIKE "{id_obat}%"
    """
    )
    result = c.fetchall()
   
    conn.close()
    if len(result) < 0:
        return "Barang tidak ditemukan"
    else:
         table = PrettyTable()       
         table.field_names = ["id_obat", "nama", "harga", "stok", "jenis_obat"]
         for row in result:
            table.add_row(row)
            print(table)

    pass

#Buatlah fungsi untuk menampilkan seluruh obat yang ada pada tabel
def tampilkan_obat():
    pass
        
#Buatlah fungsi untuk visualisasi data dalam bentuk bar chart
def vis_data():
    pass

#buatlah perulangan untuk menampilkan pilihan menu dan menjalankan program
while True:
    #Tampilkan menu
    print('1. Membuat tabel')
    print('2. Menambahkan obat')
    print('3. Menghapus obat')
    print('4. Mencari obat')
    print('5. Menampilkan data')
    print('6. Visualisai data')
    print('7. Keluar')
    pilihan = int(input("Masukan pilihan menu: "))
    if pilihan == 1:
        buattabel()
        pass
    elif pilihan == 2:
        id_obat = int(input('Masukkan id_obat: '))
        nama = str(input('Masukkan nama obat: '))
        harga = int(input('Masukkan harga obat: '))
        stok = str(input('Masukkan jumlah stok: '))
        jenis_obat = str(input('Masukkan jenis obat: '))
        tambah_obat(id_obat, nama, harga, stok, jenis_obat)
        pass
    elif pilihan == 3:
        hapus_obat()
        pass
    elif pilihan == 4:
        id_obat = input('Masukkan id obat yang akan dicari:')
        cari_obat(id_obat)
        pass
    elif pilihan == 5:
        pass
    elif pilihan == 6:
        pass
    elif pilihan == 7:
        break
    else :
        pass