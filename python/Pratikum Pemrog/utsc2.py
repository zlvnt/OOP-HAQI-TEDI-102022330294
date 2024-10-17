# Tampilkan menu utama
print("Menu Utama:")
print("1. Makanan")
print("2. Minuman")

# Pilih kategori
kategori = input("Pilih kategori (1/2): ")

menu = {}
total_harga = 0

if kategori == "1":
    # Tampilkan menu makanan
    print("Menu Makanan:")
    makanan = {
        "Nasi Goreng": 20000,
        "Mie Goreng": 18000,
        "Ayam Goreng": 25000,
        "Sate Ayam": 30000,
        "Bakso": 15000
    }
    menu = makanan
elif kategori == "2":
    # Tampilkan menu minuman
    print("Menu Minuman:")
    minuman = {
        "Air Mineral": 5000,
        "Teh Manis": 7000,
        "Es Jeruk": 10000,
        "Soda Gembira": 12000,
        "Kopi Hitam": 8000
    }
    menu = minuman
else:
    print("Pilihan tidak valid")
    exit()

pesanan = {}
while True:
    # Pilih item
    item = input("Pilih item (Ketik 'selesai' untuk mengakhiri): ")
    if item.lower() == "selesai":
        break
    if item in menu:
        jumlah = int(input("Jumlah item yang dibeli: "))
        if item in pesanan:
            pesanan[item] += jumlah
        else:
            pesanan[item] = jumlah
        total_harga += menu[item] * jumlah

diskon = 0
if total_harga > 500000:
    diskon = 0.25
elif total_harga > 250000:
    diskon = 0.15
elif total_harga > 100000:
    diskon = 0.10

total_diskon = total_harga * diskon
total_bayar = total_harga - total_diskon

# Tampilkan pesanan
print("\nPesanan:")
for item, jumlah in pesanan.items():
    print(f"{item}: {jumlah} x Rp. {menu[item]} = Rp. {jumlah * menu[item]}")

# Tampilkan total harga
print(f"Total Harga: Rp. {total_harga}")
print(f"Diskon: {int(diskon * 100)}%")
print(f"Total Setelah Diskon: Rp. {total_bayar}")

# Masukkan NIM dan Nama
nim = input("Masukkan NIM: ")
nama = input("Masukkan Nama: ")

# Masukkan nominal pembayaran
nominal_pembayaran = int(input("Masukkan Nominal Pembayaran: "))
kembalian = nominal_pembayaran - total_bayar

# Tampilkan kembalian
print(f"Kembalian: Rp. {kembalian}")
