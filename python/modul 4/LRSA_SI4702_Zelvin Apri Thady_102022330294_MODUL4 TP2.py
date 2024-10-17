def penjumlahan(a, b):
    return a + b

def pengurangan(a, b):
    return a - b

def perkalian(a, b):
    return a * b

def pembagian(a, b):
    if b == 0:
        raise ZeroDivisionError("Tidak dapat melakukan pembagian dengan bilangan 0")
    return a / b


try:
    print("===Kalkulator Pintar===")
    a1 = int(input("Masukkan angka pertama: "))
    a2 = int(input("Masukkan angka kedua: "))

    print("Pilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    opsi = int(input("Masukkan nomor operasi (1/2/3/4): "))

    if opsi == 1:
        jwb = penjumlahan(a1, a2)
        print("Hasil penjumlahan:", jwb)
    elif opsi == 2:
        jwb = pengurangan(a1, a2)
        print("Hasil pengurangan:", jwb)
    elif opsi == 3:
        jwb = perkalian(a1, a2)
        print("Hasil perkalian:", jwb)
    elif opsi == 4:
        jwb = pembagian(a1, a2)
        print("Hasil pembagian:", jwb)
    else:
        print("Pilihan tidak valid")

except ValueError:
    print("Program ini hanya menerima jenis nilai integer!")
except ZeroDivisionError as e:
    print(e)

finally:
    print("Terima kasih sudah menggunakan kalkulator pintar!")