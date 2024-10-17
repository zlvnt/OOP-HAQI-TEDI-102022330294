
print("anda memiliki 3x kesempatan untuk menebak")

kw = 'dasprokece'
t = 1

while t < 4:
    print(f"Percobaan ke-{t}")
    t += 1
    mp = input("Masukkan keyword: ")
    if mp != kw:
        if t == 4:
            print("Anda gagal")
        elif t == 3:
            print("Coba lagi")
        elif t == 2:
            print("Coba lagi")
        elif t == 1:
            print("Coba lagi")
    
    elif mp == kw:
        print("anda beerhasil!")
        break

print("\n === TRANSAKSI PENJUALAN ===")

jp = int(input("\nJumlah Produk: "))
rbb = []

for i in range(1, jp +1):
    ad = i + 1
    rb = int(input(f"Harga barang {i}: "))
    rbb.append(rb)

tp = sum(rbb)
print("\nTotal pembayaran: ", tp)
print()
    


    






