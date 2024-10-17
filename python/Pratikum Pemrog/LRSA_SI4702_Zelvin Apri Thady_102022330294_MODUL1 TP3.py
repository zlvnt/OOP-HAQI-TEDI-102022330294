
nama = str(input("Nama: "))
nim = str(input("NIM: "))
kelas = str(input("Kelas: "))
tugas = float(input("Masukkan nilai Tugas: "))
quiz = float(input("Masukkan nilai Quiz: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))

rata_rata = (tugas + quiz + uts + uas) / 4

print(f"Nilai MK Pengantar Sistem Informasi milik {nama} dengan NIM {nim} kelas {kelas} adalah:  {rata_rata:.2f}")
