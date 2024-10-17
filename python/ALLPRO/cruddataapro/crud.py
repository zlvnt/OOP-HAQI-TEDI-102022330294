customers = [
    {
        "nama": "Lukas",
        "alamat": "Sukabirus",
        "nomor_telepon": "08123456789",
        "riwayat_pembelian": ["Pakaian", "Sepatu"]
    },
    {
        "nama": "Theo",
        "alamat": "Sukapura",
        "nomor_telepon": "087654321",
        "riwayat_pembelian": ["Buku", "Mainan"]
    }
]

#TAMBAHKAN PELANGGAN
def TAMBAH_PELANGGAN():
    nama = input("Masukkan nama pelanggan: ")
    alamat = input("Masukkan alamat pelanggan: ")
    nomor_telepon = input("Masukkan nomor telepon pelanggan: ")
    riwayat_pembelian = input("Masukkan riwayat pembelian pelanggan (pisahkan dengan koma): ").split(',')
    customer = {
        "nama": nama,
        "alamat": alamat,
        "nomor_telepon": nomor_telepon,
        "riwayat_pembelian": riwayat_pembelian
    }
    customers.append(customer)
    print("Pelanggan berhasil ditambahkan.")

#TAMPILkAN PELANGGAN
def SEMUA_PELANGGAN():
    if not customers:
        print("Belum ada pelanggan.")
    else:
        for idx, customer in enumerate(customers, start=1):
            print(f"{idx}. Nama: {customer['nama']}, Alamat: {customer['alamat']}, Nomor Telepon: {customer['nomor_telepon']}, {customer['riwayat_pembelian']}")

#CARI PELANGGAN (NAMA)
def MENCARI_NAMA():
    name = input("Masukkan nama pelanggan yang ingin Anda cari: ")
    for customen in customers:
        if customen["nama"].lower() == name.lower():
            print(f"Nama: {customen['nama']}, Alamat: {customen['alamat']}, Nomor Telepon: {customen['nomor_telepon']}, {customen['riwayat_pembelian']}")
            return customen
    return None
        
# HAPUS BERDASARKAN NAMA
def HAPUS():
    nama = input("Masukkan nama pelanggan yang ingin dihapus: ")
    global customers
    customers = [customer for customer in customers if customer['nama'].lower() != nama.lower()]
    print("Pelanggan berhasil dihapus.")

# UPDATE DATA PELANGGAN
def update():
    customer = MENCARI_NAMA()
    new_nama = input("Masukkan nama baru (kosongkan jika tidak ingin mengubah): ")
    new_alamat = input("Masukkan alamat baru (kosongkan jika tidak ingin mengubah): ")
    new_nomor_telepon = input("Masukkan nomor telepon baru (kosongkan jika tidak ingin mengubah): ")
    new_riwayat_pembelian = input("Masukkan riwayat pembelian baru (pisahkan dengan koma, kosongkan jika tidak ingin mengubah): ").split(',')
    
    if customer:
        if new_nama:
            customer['nama'] = new_nama
        if new_alamat:
            customer['alamat'] = new_alamat
        if new_nomor_telepon:
            customer['nomor_telepon'] = new_nomor_telepon
        if new_riwayat_pembelian:
            customer['riwayat_pembelian'] = new_riwayat_pembelian
        print("Data pelanggan berhasil diperbarui.")
    else:
        print("Pelanggan tidak ditemukan.")
        
while True:
    print("\nMenu:")
    print("1. TAMPILKAN PELANGGAN")
    print("2. CARI PELANGGAN")
    print("3. TAMBAHKAN PELANGGAN")
    print("4. UPDATE DATA PELANGGAN")
    print("5. HAPUS DATA PELANGGAN")
    print("6. Keluar program")
    opsi_0294 = input("\nPilih menu: ")

    if opsi_0294 == "1":
        SEMUA_PELANGGAN()
        
    elif opsi_0294 == "2":
        MENCARI_NAMA()
        
    elif opsi_0294 == "3":
        TAMBAH_PELANGGAN()
        
    elif opsi_0294 == "4":
        update()
        
    elif opsi_0294 == "5":
        HAPUS()
        
    elif opsi_0294 == "6":
        print("\nTerima kasih telah menggunakan Bank Program ini")
        print()
        break
    else:
        print("\nPilihan tidak tersedia, Silakan coba lagi.")
        print()
        
    