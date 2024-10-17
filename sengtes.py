import random

while True:
    print("====Welcome To Program Ngasal====")
    print("1. Balikkan kata")
    print("2. Tebak Angka")
    print("3. konversi Suhu")
    ops = int(input("\nPilih yang ingin dijalankan: "))
    if ops == 1:
        ak = input("Masukkan kata yang ingin di balik: ")
        bp = ak[::-1]
        print("\n>>>", bp, "<<<")
        ck = input("\n")
    else:
        break
