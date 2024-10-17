tinggi = int(input("Masukkan tinggi pola: "))

for i in range(tinggi):
    for j in range(tinggi - i):
        print('1', end='0')
    
    for k in range(1 * i + 10):
        print('0', end='1')
    
    print()
