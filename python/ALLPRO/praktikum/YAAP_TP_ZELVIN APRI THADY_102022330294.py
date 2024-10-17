# NIM: 102022330294
# NAMA: Zelvin Apri Thady

database = []
while True:
    print("\n====PROGRAM MANAJEMEN DATA MAHASISWA UNIVERSITAS DASPRO=====")
    print("\n1. Menambahkan Data Mahasiswa")
    print("2. Menampilkan Seluruh Data Mahasiswa")
    print("3. Menghitung nilai akhir")
    print("4. Mengurutkan Data Nilai Akhir(dari yang terbesar)")
    print("5. Menghapus Data Mahasiswa")
    print("0. Exit")
    opsi_0294 = input("\nMasukkan menu yang diinginkan: ")

    if opsi_0294 == "1":
        print("\n>Menambahkan Data Mahasiswa<")
        nama = str(input("Masukkan Nama: "))
        nim = int(input("Masukkan NIM: "))
        kuis = float(input("Masukkan nilai kuis: "))
        tugas = float(input("Masukkan nilai tugas: "))
        ujian = float(input("Masukkan nilai ujian: "))
        dataM = {
        "nama": nama,
        "nim": nim,
        "kuis": kuis,
        "tugas": tugas,
        "ujian": ujian
    }
        database.append(dataM)
        print("Nilai berhasil dimasukkan.")
        
        next = input("\n\t--> Enter to menu <--")

    elif opsi_0294 == "2":
        if not database:
            print("Belum ada pelanggan.")
        else:
            print("\nData Mahasiswa: ")
            for idx, mahasiswa in enumerate(database, start=1):
                print(f"{idx}. Nama: {mahasiswa['nama']}, NIM: {mahasiswa['nim']}, Quiz: {mahasiswa['kuis']}, Tugas: {mahasiswa['tugas']}, Ujian:{mahasiswa['ujian']} ")
                
        next = input("\n\t--> Enter to menu <--")

    elif opsi_0294 == "3":
        
        def nilai_akhir():
            carinim = int(input("\nMasukkan NIM Mahasiswa yang ingin Anda cari: "))
            for mahasiswa1 in database:
                if mahasiswa1["nim"] == carinim: 
                    kuis = mahasiswa1["kuis"]
                    tugas = mahasiswa1["tugas"]
                    ujian = mahasiswa1["ujian"]
                    rata1 = float((kuis * 0.25) + (tugas * 0.25) + (ujian * 0.5))
                    print(f"\nNilai akhir dari mahasiswa dengan nama {mahasiswa1['nama']}, NIM {mahasiswa1['nim']} adalah {rata1}")
        
        nilai_akhir()
        next = input("\n\t--> Enter to menu <--")
        
    elif opsi_0294 == "4":
        nilai_rata = []
        for mahasiswa in database:
            nama = mahasiswa['nama']
            nim = mahasiswa["nim"]
            kuis = mahasiswa["kuis"]
            tugas = mahasiswa["tugas"]
            ujian = mahasiswa["ujian"]
            rata = (kuis * 0.25) + (tugas * 0.25) + (ujian * 0.5)
            nilai_rata.append({"nama": nama, "nim": nim, "rata": rata})
            urut_nilai = sorted(nilai_rata, key=lambda x: x["rata"])   
                
        print("\nData Mahasiswa (Nilai Akhir Terbesar): ")
        for nilai in urut_nilai:
            print(f"Nama: {nilai['nama']}, NIM: {nilai['nim']}, Nilai rata-rata: {nilai['rata']}")
        
        next = input("\n\t--> Enter to menu <--")

    elif opsi_0294 == "5":
        carinim = int(input("\nMasukkan NIM mahasiswa yang akan dihapus: "))
        hapus = False
        for mahasiswa in database:
            if mahasiswa['nim'] == carinim:
                database.remove(mahasiswa)
                print(f"Data mahasiswa dengan NIM {carinim} berhasil dihapus.")
                hapus = True
                break
        if not hapus:
            print(f"Tidak ada mahasiswa dengan NIM {carinim} dalam database.")
        
        next = input("\n\t--> Enter to menu <--")
            
    elif opsi_0294 == "0":
        print("\nProgram selesai,Terima Kasih")
        print()
        break
    else:
        print("\nPilihan tidak tersedia, Silakan coba lagi.")
        print()
        
    