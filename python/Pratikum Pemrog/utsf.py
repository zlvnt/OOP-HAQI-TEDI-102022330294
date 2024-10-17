# NIM: 102022330294
# Nama: Zelvin Apri Thady

makanan_0294 = {
    "Bakso": 30000,
    "Ayam": 40000,
    "Telur": 20000,
    "Piza": 80000,
    "Salad": 25000
}

minuman_0294 = {
    "Susu": 30000,
    "Teh": 20000,
    "Kopi": 25000,
    "Caramel": 40000,
    "Aqua": 15000
}

menu_0294 = {}
total_0294 = 0
pesanan_0294 = []
diskon_0294 = 0

print("Selamat datang")
print("===============")

while True:   
    print("Silakan pilih kategori:")
    print("1. Makanan")
    print("2. Minuman")

    while True:
        pilih_0294 = input("\nMasukkan pilihan (1/2): ")

        if pilih_0294 == "1":
            print("\nKategori Makanan:")
            for mnk_0294, harga_0294 in makanan_0294.items():
                print(f"{mnk_0294}: Rp. {harga_0294}")
            menu_0294 = makanan_0294
            break
        elif pilih_0294 == "2":
            print("\nKategori Minuman:")
            for mnk_0294, harga_0294 in minuman_0294.items():
                print(f"{mnk_0294}: Rp. {harga_0294}")
            menu_0294 = minuman_0294
            break
        else:
            print("\nsilakan pilih item yang sesuai.")
    

    while True:
        mnk_0294 = input("\nPilih item yang akan dibeli (ketik 'n' untuk pembayaran): ")
        if mnk_0294 in menu_0294:
            harga_0294 = menu_0294[mnk_0294]
            totalb_0294 = int(input(f"Masukkan jumlah {mnk_0294}: "))
            pesanan_0294.append((mnk_0294, harga_0294))
        elif mnk_0294.lower() == 'n':
            break
        else:
            print("\nsilakan pilih item yang sesuai.")

    for mnk_0294, harga_0294 in pesanan_0294:
        if mnk_0294 in makanan_0294:
            total_0294 += makanan_0294[mnk_0294] * totalb_0294
        elif mnk_0294 in minuman_0294:
            total_0294 += minuman_0294[mnk_0294] * totalb_0294

    if total_0294 > 500000:
        diskon_0294 = 0.25
    elif total_0294 > 250000:
        diskon_0294 = 0.15
    elif total_0294 > 100000:
        diskon_0294 = 0.10

    totaldiskon_0294 = total_0294 * diskon_0294
    bayar_0294 = total_0294 - totaldiskon_0294

    print("\n----PESANAN----")
    for mnk_0294, harga_0294 in pesanan_0294:
        print(f"{mnk_0294}: {totalb_0294} x Rp. {harga_0294} = Rp. {totalb_0294 * harga_0294}")

    print("Total: Rp", total_0294)
    print("Diskon: ", int(totaldiskon_0294), "%")
    print("Bayar: Rp", int(bayar_0294))

    nim_0294 = input("NIM: ")
    nama_0294 = input("Nama: ")

    while True:
        pembayaran_0294 = int(input("Masukkan Nominal Pembayaran: "))
        if pembayaran_0294 > bayar_0294:
            kembalian_0294 = pembayaran_0294 - bayar_0294
            break
        else:
            print("Nominal Tidak Cukup, masukkan ulang nominal")


    print("-----Kembalian: Rp", int(kembalian_0294), "-----")
    
    restart_0294 = input("\nApakah anda ingin memesan lagi? (y/n): ")
    if restart_0294.lower() == 'n':
        break





