import sqlite3
import matplotlib.pyplot as plt
from numpy import character

DATABASE_FILE = "karakter_anime.sqlite3"

def create_table():
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()
    c.execute  ("""CREATE TABLE IF NOT EXISTS tabel_anime(id INTEGER
                primary key, nama TEXT not null,anime TEXT not
                null, power_level INT not null, healt INT not null)""")
    conn.commit()
    c.close()
    print("Database sudah dibuat")
    
    # Buat kode untuk membuat tabel anime pada database karakter_anime.sqlite3
    

def insert_character(nama, anime, power_level, healt):
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()
    c.execute ("""INSERT INTO
    tabel_anime(nama,anime,power_level,healt)
    VALUES(?,?,?,?)""",(nama, anime, power_level, healt))

    conn.commit()
    conn.close()
    
    # Buat kode untuk memasukkan 4 karakter legendaris secara otomatis ke dalam tabel anime


def select_all_characters():
    conn = sqlite3.connect(DATABASE_FILE)
    cur = conn.cursor()
    cur.execute("SELECT * FROM tabel_anime")
    characters = cur.fetchall()
    
    if not characters :
        print("Tidak ada karakter dalam database")
    else:
        print("karakter dalam database: ")
        for character in characters:
            print (character)
    conn.close()
    
    
    # Buat kode untuk menampilkan isi dari semua tabel anime


def simulate_battle(character_id, enemy_id):

    """Mensimulasikan pertempuran antara karakter dengan musuh
    Args:
        character_id: int, id karakter yang menyerang
        enemy_id: int, id musuh yang diserang
    Output: Hasil pertempuran
    Returns: None
    """
    # Buat kode untuk mengambil informasi karakter yang menyerang (character_id) dan musuh yang diserang (enemy_id)


    # Mengurangi health musuh berdasarkan power level karakter


    # Buat kode untuk mengupdate kesehatan musuh dalam database setelah


    # print hasil pertempuran


def visualize_health():
    # data = select_all_characters()
    # nama_karakter = [character[4] for characters in data]
    # stok = [barang[4] for barang in data]
    # plt.figure(figsize=(10, 6))
    # plt.bar(nama, healt, color='skyblue')
    # plt.xlabel('Ukuran Barang')
    # plt.ylabel('Jumlah Stok')
    # plt.title('Inventarisasi Stok Barang Berdasarkan Ukuran')
    # plt.xticks(rotation=45, ha='right')
    # plt.tight_layout()
    # plt.show()
    """"maaf error ini jdi dicmmandin"""
    """Visualisasi kesehatan karakter setelah semua pertarungan selesai dilakukan"""

# Buat kode untuk menampilkan visualisasi (bar chart) dimana nama karakter di sumbu x dan tingkat kesehatan di sumbu y.


# Buat pemanggilan fungsi sesuai dengan operasi yang diminta pada soal latihan
create_table()
insert_character("Son Goku","Dragon Ball",5000,10000)
insert_character("Naruto Uzumaki","Naruto",4000,7500)
insert_character("Monkey D. Luffy","One Piece",3000,6000)
insert_character("Ichigo Kurosaki","Bleach",3500,5000)
select_all_characters()
visualize_health()