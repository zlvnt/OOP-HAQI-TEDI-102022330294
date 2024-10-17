# IMPORT LIBRARY NUMPY
#ZELVIN APRI THADY
#102022330294
import numpy as np
data_siswa = {
    # BUAT LAH DICTIONARY DATA SISWA DISINI!!
    "Agus": 70,
    "Budi": 85,
    "Citra": 90,
    "Dian": 75,
    "Eka": 60,
    "Fani": 80,
    "Gina": 95,
    "Hadi": 88,
    "Indra": 77,
    "Joko": 82
}
while True:
    print("\n========= UNIVERSITAS DASPRO =========")
    # BUAT LAH TAMPILAN MENU DISINI!!! 
    
    print("1. Daftar Mahasiswa")
    print("2. Rata-rata Nilai Mahasiswa")
    print("3. Nilai Tertinggi")
    print("4. Nilai Terendah")
    print("5. Mahasiswa Remedi")
    print("6. Keluar")
    print("\n=======================================")
    pilihan = input("Masukkan pilihan (1-6): ")

    if pilihan == '1':
        # UBAH LAH SYNTAX PASS DENGAN YANG BENAR!!!
        for nama,nilai in data_siswa.items():
            print(f"Nama: {nama}, Nilai: {nilai}")
        pass
        next = input()
    elif pilihan == '2':
        ds = np.array(list(data_siswa.values()))
        rt = np.mean(ds)
        print(f"Rata-rata Nilai Mahasiswa {rt}")
        pass
        next = input()
    elif pilihan == '3':
        mx = np.array(list(data_siswa.values()))
        b = np.max(mx)
        print(f"nilai tertinggi mahasiswa: {b}")
        pass
        next = input()
    elif pilihan == '4':
        mx = np.array(list(data_siswa.values()))
        b = np.min(mx)
        print(f"nilai terendah mahasiswa: {b}")
        pass
        next = input()
        
    elif pilihan == '5':

        for n, l in data_siswa.items():
            if l < 70:

                print("Mahasiswa yang remedi: ")
                print(f"nama: {n}, Nilai:{l}")
        pass
        next = input()
    elif pilihan == '6':
        print("Terima Kasih. Program Selesai")
        break

    else:
        print()
