import sqlite3
import matplotlib.pyplot as plt

DF = "karakter_anime.sqlite3"

def create_table():

    conn = sqlite3.connect(DF)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS tabel_anime(
                id INTEGER AUTO INCREMENT PRIMARY KEY,
                nama TEXT NOT NULL,
                anime TEXT NOT NULL,
                power_level INTEGER NOT NULL,
                healt INTEGER NOT NULL)""")
    conn.commit()
    print("Tabel berhasil dibuat!")
    conn.close()
    
def insert_character(nama, anime, power_level, healt):
    conn = sqlite3.connect(DF)
    c = conn.cursor()
    c.execute("""INSERT INTO tabel_anime (nama, anime, power_level, healt)
                 VALUES (?, ?, ?, ?)""", (nama, anime, power_level, healt))
    conn.commit()
    print('Karakter berhasil ditambahkan ke database!')
    conn.close()

def select_all_characters():
    conn = sqlite3.connect(DF)
    c = conn.cursor()
    c.execute("SELECT * FROM tabel_anime")
    kar = c.fetchall()
    
    print("Karakter dalam database:")
    for car in kar:
            print(car)
    conn.close()

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
    """Visualisasi kesehatan karakter setelah semua pertarungan selesai dilakukan"""

    # Buat kode untuk menampilkan visualisasi (bar chart) dimana nama karakter di sumbu x dan tingkat kesehatan di sumbu y.


# Buat pemanggilan fungsi sesuai dengan operasi yang diminta pada soal latihan

create_table()

insert_character("Son Goku", "Dragon Ball", 5000, 10000)
insert_character("Naruto Uzumaki", "Naruto", 4000, 7500)
insert_character("Monkey D. Luffy", "One Piece", 3000, 6000)
insert_character("Ichigo Kurosaki", "Bleach", 3500, 5000)

select_all_characters()