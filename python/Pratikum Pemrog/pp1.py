# Input dua nilai dari pengguna
nilai1 = int(input("Masukkan nilai pertama: "))
nilai2 = int(input("Masukkan nilai kedua: "))

# Membandingkan dua nilai
if nilai1 > nilai2:
    print("Nilai pertama ({}) lebih besar dari nilai kedua ({}).".format(nilai1, nilai2))
elif nilai2 > nilai1:
    print("Nilai kedua ({}) lebih besar dari nilai pertama ({}).".format(nilai2, nilai1))
else:
    print("Nilai pertama ({}) sama dengan nilai kedua ({}).".format(nilai1, nilai2))
