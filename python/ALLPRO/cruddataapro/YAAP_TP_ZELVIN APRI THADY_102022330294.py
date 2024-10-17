import sqlite3
import matplotlib.pyplot as plt
from prettytable import PrettyTable

def b_tabel():
    co = sqlite3.connect('inventaris_buku.db')
    cu = co.cursor()
    cu.execute("""
               CREATE TABLE IF NOT EXISTS tabel_buku(
                   id_buku INTEGER PRIMARY KEY AUTOINCREMENT,
                   judul TEXT NOT NULL,
                   penulis TEXT NOT NULL,
                   tahun_terbit INTEGER,
                   genre TEXT,
                   stok INTEGER NOT NULL
                 )
            """)
    co.commit()
    print(f"Tabel 'tabel_buku' berhasil dibuat.")
    co.close()

def in_data(j, p, t, g, s):
    co = sqlite3.connect('inventaris_buku.db')
    cu = co.cursor()
    cu.execute("INSERT INTO tabel_buku(judul, penulis, tahun_terbit, genre, stok) VALUES (?, ?, ?, ?, ?)", (j, p, t, g, s))
    co.commit()
    print(f"Buku '{j}' telah ditambahkan ke dalam database")
    co.close()

def m_data():
    while True:
        j = str(input('Masukkan judul buku (n = exit): '))
        if j.lower() == 'n':
            break
        p = str(input('Masukkan penulis buku: '))
        t = int(input('Masukkan tahun terbit: '))
        g = str(input('Masukkan genre buku: '))
        s = int(input('Masukkan jumlah stok: '))
        in_data(j, p, t, g, s)

def tampilkan_buku():
    co = sqlite3.connect('inventaris_buku.db')
    cu = co.cursor()
    cu.execute("SELECT * FROM tabel_buku")
    rows = cu.fetchall()
    if not rows:
        print("Tidak ada data buku yang tersedia.")
    else:
        table = PrettyTable()       
        table.field_names = ["id_buku", "judul", "penulis", "tahun_terbit", "genre", "stok"]
        for row in rows:
            table.add_row(row)
        print(table)
    co.close()

def hapus_buku():
    co = sqlite3.connect('inventaris_buku.db')
    cu = co.cursor()
    id_buku = int(input("Masukkan ID buku yang akan dihapus: "))
    cu.execute("DELETE FROM tabel_buku WHERE id_buku = ?", (id_buku,))
    co.commit()
    print(f"Buku dengan ID {id_buku} telah dihapus dari database.")
    co.close()

def visualisasi_data():
    co = sqlite3.connect('inventaris_buku.db')
    cu = co.cursor()
    cu.execute("SELECT genre, SUM(stok) FROM tabel_buku GROUP BY genre")
    data = cu.fetchall()
    if not data:
        print("Tidak ada data untuk divisualisasikan.")
    else:
        genres = [row[0] for row in data]
        stocks = [row[1] for row in data]
        
        plt.bar(genres, stocks, color='skyblue')
        plt.xlabel('Genre')
        plt.ylabel('Jumlah Buku')
        plt.title('Jumlah Buku per Genre')
        plt.show()
    co.close()


while True:
    print("\nMenu:")
    print("1. Buat Tabel")
    print("2. Masukkan Buku")
    print("3. Tampilkan Buku")
    print("4. Hapus Buku")
    print("5. Visualisasi Data")
    print("6. Keluar")
    pilihan = input("Pilih Menu: ")
    
    if pilihan == '1':
        b_tabel()
    elif pilihan == '2':
        m_data()
    elif pilihan == '3':
        tampilkan_buku()
    elif pilihan == '4':
        hapus_buku()
    elif pilihan == '5':
        visualisasi_data()
    elif pilihan == '6':
        print("Terima kasih! Program Berakhir.")
        break
    else:
        print("Pilihan Tidak Tersedia.")
