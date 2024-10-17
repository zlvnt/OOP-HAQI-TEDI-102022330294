def l_b(sisi):
    luas = 6 * sisi *2
    return luas

pj = 4
lp = l_b(pj)
print(f"lb {lp}")


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




def luas_persegi(b):
    return b * b

def luas_persegpan(a, b):
    a = int(input("Masukkan panjang persegi panjang: "))
    b = int(input("Masukkan lebar persegi panjang: "))
    return a * b

def luas_segitiga(a, t):
    a = int(input("Masukkan alas segitiga: "))
    t = int(input("Masukkan tinggi segitiga: "))
    return a * t / 2

def luas_lingkaran(r):
    t = int(input("Masukkan jari-jari lingkaran: "))
    return float(3.14 * r * r)

try:
    print('\nPROGRAM MENGHTUNG LUAS BANGUN DATAR')
    print('=====================================')
    print('1. Persegi')
    print('2. Persegi Panjang')
    print('3. Segitiga')
    print('4.Lingkaran')
    print('0. Exit')
    plh = int(input('Pilih bangun datar yang tersedia: '))
    print('\n=====================================')
    if plh == 1:
        luas_persegi()
    elif plh == 2:
        a = int(input("Masukkan panjang persegi panjang: "))
        b = int(input("Masukkan lebar persegi panjang: "))
        jwb = luas_persegpan(a, b)
        print("Luas bangun persegi panjang adalah: ", jwb)

    elif plh == 3:
        luas_segitiga()
    elif plh == 4:
        luas_lingkaran()
    elif plh == 0:
        print('Sampai bertemu kembali!\t :)')







except IndexError:
    print("Input diluar jangkauan")
except ValueError:
    print("Inputan Harus berupa angka")




