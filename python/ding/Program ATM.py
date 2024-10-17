# NIM: 102022330294
# NAMA: Zelvin Apri Thady

saldoku_0294 = 2000000

print("Selamat datang di Bank KOM")
nama_0294 = input("Masukkan Nama: ")
nim_0294 = input("Masukkan NIM: ")
no_rekening_0294 = input("Masukkan No. Rekening: ")


while True:
    p_0294 = input("Masukkan PIN (6 digit akhir dari NIM): ")
    if p_0294 == nim_0294[-6:]:
        print("\nPIN BENAR. Selamat datang", nama_0294 )
        break  
    else:
        print("PIN yang anda masukkan salah. Silakan coba lagi.")

while True:
    print("\nMenu utama:")
    print("1. Cek Saldo")
    print("2. Tarik Uang")
    print("3. Setor Uang")
    print("4. Keluar")
    opsi_0294 = input("Pilih menu (1/2/3/4): ")

    if opsi_0294 == "1":
            
        print("\nInformasi Nasabah:")
        print("NIM: ", nim_0294)
        print("Nama: ", nama_0294)
        print("No. Rekening: ", no_rekening_0294)
        print("Saldo: Rp", saldoku_0294)

    elif opsi_0294 == "2":
        
        print("\nInformasi Nasabah:")
        print("NIM: ", nim_0294)
        print("Nama: ", nama_0294)
        print("No. Rekening: ", no_rekening_0294)
        nominal_0294 = float(input("Masukkan nominal_0294 yang akan ditarik: "))
        if nominal_0294 > saldoku_0294:
            print("Saldo tidak mencukupi.")
        else:
            saldoku_0294 -= nominal_0294
            print("Saldo akhir: Rp", saldoku_0294)

    elif opsi_0294 == "3":
        
        print("\nInformasi Nasabah:")
        print("NIM: ", nim_0294)
        print("Nama: ", nama_0294)
        print("No. Rekening: ", no_rekening_0294)
        nominal_0294 = float(input("Masukkan nominal_0294 yang akan disetor: "))
        saldoku_0294 += nominal_0294
        print("Saldo akhir: Rp", saldoku_0294)

    elif opsi_0294 == "4":
        print("Terima kasih telah menggunakan Bank KOM")
        break

    else:
        print("Pilihan tidak tersedia, Silakan coba lagi.")
        
    