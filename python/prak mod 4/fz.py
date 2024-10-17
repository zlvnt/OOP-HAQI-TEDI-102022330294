hasil_perhitungan = []
try:
    while True:

        angka = input("Masukkan angka (ketik 'keluar' untuk selesai): ")
        if angka == 'keluar':
            break
        else:
            angka = int(angka)
            hasil_perhitungan.append((angka)) 

    hasil_perhitungan.sort(reverse=True)
    print(hasil_perhitungan)

except ValueError:
    print('Masukkan angka yang valid!')

