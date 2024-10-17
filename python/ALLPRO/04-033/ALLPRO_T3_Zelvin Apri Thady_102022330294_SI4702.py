def matrixs(baris, kolom):
    nilai_mentah = []
    for row in baris:
        raw_score = sum([x * y for x, y in zip(row[1:], kolom)])
        nilai_mentah.append(raw_score)
    return [row + [raw_score] for row, raw_score in zip(baris, nilai_mentah)]

jumlah_siswa = int(input("Masukkan jumlah mahasiswa: "))
kolom = [0.3, 0.3, 0.1, 0.3]

penyimpanan = []
for i in range(jumlah_siswa):
    nim = input(f"Masukkan NIM Mahasiswa ke-{i+1}: ")
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))
    quiz = float(input("Nilai Quiz: "))
    praktikum = float(input("Nilai Praktikum: "))
    penyimpanan.append([nim, uts, uas, quiz, praktikum])

nilai_mentah = matrixs(penyimpanan, kolom)

print("\n-----Data Mahasiswa-----")
print("\nNIM:")
for row in nilai_mentah:
    print(row[0])
    print("UTS:")
    print(row[1]) 
    print("UAS:")
    print(row[2])  
    print("Quiz:")
    print(row[3])
    print("Praktikum:")
    print(row[4])
    print("Nilai Mentah:")
    print(row[5])
    print()
