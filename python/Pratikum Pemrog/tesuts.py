# Saldo awal tabungan
saldo_tabungan = 1000

# Saldo minimum yang diizinkan
saldo_minimum = 100

while saldo_tabungan > saldo_minimum:
    try:
        # Meminta pengguna untuk memasukkan jumlah penarikan
        penarikan = float(input("Masukkan jumlah penarikan: "))
        
        if penarikan <= 0:
            print("Jumlah penarikan harus lebih dari 0.")
        elif penarikan > saldo_tabungan:
            print("Saldo tidak mencukupi untuk penarikan tersebut.")
        else:
            saldo_tabungan -= penarikan
            print(f"Penarikan sebesar {penarikan} berhasil. Saldo sekarang: {saldo_tabungan}")
    except ValueError:
        print("Masukkan jumlah penarikan yang valid.")
    
print("Saldo Anda telah mencapai saldo minimum. Transaksi selesai.")
