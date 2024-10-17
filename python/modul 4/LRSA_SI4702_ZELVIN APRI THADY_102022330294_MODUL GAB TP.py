#PROGRAM BMI

def hitung_BMI(berat_badan, tinggi_badan):
    return (berat_badan / tinggi_badan / tinggi_badan) * 10000

def kategori_BMI(BMI):
    if BMI < 18.5:
        return "Underweight"
    elif 18.5 <= BMI < 25:
        return "Healthy weight"
    elif 25 <= BMI < 30:
        return "Overweight"
    else:
        return "Obesity"
    
list_pasien = []

while True:
    print("\n=====Kalkulator BMI=====")
    print("Menu:")
    print("1. Input Data Pasien")
    print("2. Pilih Pasien dan Hitung BMI Pasien")
    print("3. Exit")

    try:
        opsi = int(input("Pilih menu (1/2/3): "))
        
        if opsi == 1:
            nama = input("Masukkan Nama: ")
            while True:
                try: 
                    berat = float(input("Masukkan Berat Badan (kg): "))
                    tinggi = float(input("Masukkan Tinggi Badan (cm): "))
                    list_pasien.append({"Nama": nama, "Berat": berat, "Tinggi": tinggi})
                    print("Data berhasil di input")
                    break
                except ValueError:
                    print("Input tidak valid. Hanya bisa memasukkan angka!")
        
        elif opsi == 2:
            if not list_pasien:
                print("Belum ada data pasien yang tersimpan.")
            else:
                print("Daftar Pasien: ")
                jarak_nama = max(len(pasien['Nama']) for pasien in list_pasien)
                jarak_berat = max(len(str(pasien['Berat'])) for pasien in list_pasien)
                jarak_tinggi = max(len(str(pasien['Tinggi'])) for pasien in list_pasien)
                for i, pasien in enumerate(list_pasien, start=1):
                    nama = pasien['Nama']
                    berat = int(pasien['Berat'])
                    tinggi = int(pasien['Tinggi'])
                    print(f"{i}. {nama.ljust(jarak_nama)} \t | {str(berat).ljust(jarak_berat)}kg\t | {str(berat).ljust(jarak_berat)}cm") 
                try:
                    index_pasien = int(input("Pilih nomor pasien yang ingin dihitung BMI: ")) - 1
                    pasien_terpilih = list_pasien[index_pasien]

                    if pasien_terpilih['Berat'] == 0:
                        print("Berat badan tidak boleh nol.")
                    elif pasien_terpilih['Tinggi'] == 0:
                        print("Tinggi badan tidak boleh nol.")
                    else:
                        BMI = hitung_BMI(pasien_terpilih['Berat'], pasien_terpilih['Tinggi'])
                        kategori = kategori_BMI(BMI)
                        print(f"\n{pasien_terpilih['Nama']} memiliki BMI {BMI:.2f} dan termasuk dalam kategori {kategori}")
                except (ValueError, IndexError):
                    print("Nomor pasien tidak valid.")


        
        elif opsi == 3:
            print("*** Terimakasih Sudah Menggunakan Kalkulator BMI ***")
            break
        else:
            print("Pilihan tidak valid, silakan pilih menu yang valid.")
    
    except (IndexError, ValueError):
        print("Nomor pasien tidak valid.")




#PROGRAM KALKULATOR PINTAR

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
    print("\n===Kalkulator Pintar===")
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