jenis_barang = {
    "sepatu": 200000,
    "baju": 95000,
    "celana": 120000,
    "topi": 70000,
    "jaket":170000,
    "gelang": 50000 }

barang_pertama = input("barang pertama: ")
barang_kedua = input("barang kedua: ")

if barang_pertama in jenis_barang and barang_kedua in jenis_barang:
   
    total_pembelian = jenis_barang[barang_pertama] + jenis_barang[barang_kedua]

    if total_pembelian >= 271000:
        potongan = 0.2 * total_pembelian
    else:
        potongan = 0

    jumlah_dibayar = total_pembelian - potongan

    print("Total: Rp.", total_pembelian)
    print("Potongan harga: Rp.", potongan)
    print("Jumlah yang harus dibayar: Rp.", jumlah_dibayar)
else:
    print("Barang tidak tersedia")
