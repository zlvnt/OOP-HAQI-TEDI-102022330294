import numpy as np

nilai_mahasiswa = {
    "Bagas": [69, 90, 83],
    "Javier": [70, 80, 72],
    "Slamet": [92, 85, 74]  
}

print('---------------------------------------------')
print('   BERIKUT INI ADALAH NILAI DARI MAHASISWA   ')
print('             UNIVERSITAS TELKOM              ')
print('---------------------------------------------')

maxk = 3
kesempatan = 0

while kesempatan < maxk:
    pt = str(input("Masukkan nama mahasiswa yang ingin dicek: "))
    if pt in nilai_mahasiswa:
        nilai = np.array(nilai_mahasiswa[pt])   
        print()
        print(f"Nama : {pt}")
        print(f"Nilai Rata-rata: {np.mean(nilai)}")
        print(f"Nilai Tertinggi:  {np.max(nilai)}")
        print(f"Nilai Terrendah: {np.min(nilai)}")
        print(f"Nilai Akhir : {np.mean(nilai) * 0.4 + np.max(nilai) * 0.3 + np.min(nilai) * 0.3}")
        kesempatan += 1
    else:
        kesempatan += 1
        if kesempatan < maxk:
            print(f"Nama tidak ditemukan. Kesempatan tersisa {maxk - kesempatan} lagi!")
        else:
            print("Kesempatan mencari nama mahasiswa habis.")
