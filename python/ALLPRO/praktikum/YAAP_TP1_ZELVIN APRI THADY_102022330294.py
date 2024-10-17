# NIM: 102022330294
# NAMA: Zelvin Apri Thady

while True:
    print("\nMenu:")
    print("1. Masukkan nilai (Kuis, Tugas, UTS, UAS)")
    print("2. Menampilkan nilai")
    print("3. Menghitung nilai akhir")
    print("4. Menampilkan status kelulusan")
    print("5. Keluar program")
    opsi_0294 = input("\nPilih menu: ")

    if opsi_0294 == "1":
        print("\n === INPUT NILAI ===")
        kuis = float(input("Masukkan nilai kuis: "))
        tugas = float(input("Masukkan nilai tugas: "))
        uts = float(input("Masukkan nilai UTS: "))
        uas = float(input("Masukkan nilai UAS: "))
        print("Nilai berhasil dimasukkan.")
        next = input("\n\t--> Enter to menu <--")

    elif opsi_0294 == "2":
        print("\n === DATA NILAI ===")
        print("Nilai kuis:", kuis)
        print("Nilai Tugas:", tugas)
        print("Nilai UTS:", uts)
        print("Nilai UAS:", uas)
        next = input("\n\t--> Enter to menu <--")
        
    elif opsi_0294 == "3":
        rata1 = (kuis * 0.2) + (tugas * 0.15) + (uts * 0.3) + (uas * 0.35)
        
        if 80 < rata1:
            nilai = "A"
        elif 70 < rata1 <= 80:
            nilai = "AB"
        elif 65 < rata1 <= 70:
            nilai = "B"    
        elif 60 < rata1 <= 65:
            nilai = "BC"
        elif 50 < rata1 <= 60:
            nilai = "BC"
        elif 40 < rata1 <= 50:
            nilai = "D"
        else:
            nilai = "E" 
        print("Nilai akhir: ", rata1)
        print("Indeks huruf: ", nilai)
        next = input("\n\t--> Enter to menu <--")
        
    elif opsi_0294 == "4":
        
        if nilai == "E" :
            status = "Tidak lulus"
        else:
            status = "Lulus"
        print("\nStatus Kelulusan: ", status)
        
        next = input("\n\t--> Enter to menu <--")

    elif opsi_0294 == "5":
        print("\nTerima kasih telah menggunakan Bank Program ini")
        print()
        break

    else:
        print("\nPilihan tidak tersedia, Silakan coba lagi.")
        print()
        
    