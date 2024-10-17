import sqlite3
import matplotlib.pyplot as plt
import numpy as np

DATABASE_FILE = "karakter_anime.sqlite3"

def create_table():
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS tabel_anime(
                id INTEGER PRIMARY KEY,
                nama TEXT NOT NULL,
                anime TEXT NOT NULL,
                power_level INT NOT NULL,
                healt INT NOT NULL)""")
    conn.commit()
    c.close()
    print("Database sudah dibuat")

def insert_character(nama, anime, power_level, healt):
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()
    c.execute("""INSERT INTO tabel_anime (nama, anime, power_level, healt)
                 VALUES (?, ?, ?, ?)""", (nama, anime, power_level, healt))
    conn.commit()
    conn.close()

def select_all_characters():
    conn = sqlite3.connect(DATABASE_FILE)
    cur = conn.cursor()
    cur.execute("SELECT * FROM tabel_anime")
    characters = cur.fetchall()
    
    if not characters:
        print("Tidak ada karakter dalam database")
    else:
        print("Karakter dalam database:")
        for character in characters:
            print(character)
    conn.close()

def simulate_battle(character_id, enemy_id):
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()

    # Retrieve character and enemy data
    c.execute("SELECT * FROM tabel_anime WHERE id=?", (character_id,))
    character = c.fetchone()
    c.execute("SELECT * FROM tabel_anime WHERE id=?", (enemy_id,))
    enemy = c.fetchone()

    if character and enemy:
        # Calculate new health for the enemy using NumPy
        new_health = np.maximum(enemy[4] - character[3], 0)

        # Update enemy's health in the database
        c.execute("UPDATE tabel_anime SET healt=? WHERE id=?", (int(new_health), enemy_id))
        conn.commit()

        print(f"{character[1]} menyerang {enemy[1]}! Kesehatan {enemy[1]} sekarang {new_health}.")
    else:
        print("Karakter atau musuh tidak ditemukan dalam database.")
    
    conn.close()

def visualize_health():
    conn = sqlite3.connect(DATABASE_FILE)
    cur = conn.cursor()
    cur.execute("SELECT nama, healt FROM tabel_anime")
    data = cur.fetchall()
    conn.close()

    if data:
        names = [row[0] for row in data]
        health = [row[1] for row in data]

        plt.figure(figsize=(10, 6))
        plt.bar(names, health, color='skyblue')
        plt.xlabel('Nama Karakter')
        plt.ylabel('Kesehatan')
        plt.title('Kesehatan Karakter Setelah Pertarungan')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
    else:
        print("Tidak ada data untuk divisualisasikan.")

# Create table and insert characters
create_table()
insert_character("Son Goku", "Dragon Ball", 5000, 10000)
insert_character("Naruto Uzumaki", "Naruto", 4000, 7500)
insert_character("Monkey D. Luffy", "One Piece", 3000, 6000)
insert_character("Ichigo Kurosaki", "Bleach", 3500, 5000)

# Select and display all characters
select_all_characters()

# Simulate a battle
simulate_battle(1, 2)  # Example: Son Goku attacks Naruto Uzumaki

# Visualize health
visualize_health()
