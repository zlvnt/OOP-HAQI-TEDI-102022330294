
# PROGRAM MENGHITUNG RATA-RATA NILAI
print("\n === PROGRAM MENGHITUNG RATA-RATA NILAI === ")
jumlah_siswa = int(input("Masukkan jumlah siswa: "))

if jumlah_siswa > 0:
    nilai_siswa = []
    for atk in range(jumlah_siswa):
        ada = atk + 1
        nilai = int(input(f"Masukkan nilai siswa ke-{ada}: "))
        if 0 <= nilai <= 100:
            nilai_siswa.append(nilai)
        else:
            print("Gagal! Mohon masukkan nilai dari rentang 0-100!")
            break
                
    rata_siswa = sum(nilai_siswa) / jumlah_siswa
    fn = "{:.3f}".format(rata_siswa)
    print(f"Rata rata nilai =", float(fn))
    print()
else:
    print("Jumlah siswa harus lebih dari 0")


# PROGRAM TARGET MENABUNG
print("\n === PROGRAM TARGET MENABUNG === ")

nmnl = int(input("Masukkan nominal yang diinginkan: "))
wktb = int(input("Masukkan jangka waktu (bulan): "))

uangT = []
tb = 0
bkl = 0

while tb < wktb:
    tb += 1
    nilai = int(input(f"Masukkan uang tabungan di bulan ke-{tb}: "))
    uangT.append(nilai)
    
    bkl += nilai

    kjl = nmnl - bkl

    if bkl >= nmnl:
        print("Anda telah berhasil menabung sesuai target!")
        print("Tabungan anda sekarang sebesar", bkl)
        break

if bkl < nmnl:
    print("Tabungan anda kurang", kjl, "dari", nmnl)
    print("Total tabungan anda sekarang sebesar", bkl, "silahkan menabung lagi!")



