import pandas as pd

data = pd.read_csv('datad.csv')
urut = pd.DataFrame(data)

def pendter():
    sort = data.sort_values('Tingkat_Penyelesaian_Pendidikan', ascending=False)
    pilih = sort[['Provinsi', 'Tingkat_Penyelesaian_Pendidikan']]
    h5 = pilih.head()
    print('5 Kota dengan Tingkat Penyelesaian Pendidikan Tertinggi:')
    print()
    print(h5)
    
def ngangter():
    sort1 = data.sort_values('Tingkat_Setengah_Pengangguran', ascending=False)
    pilih1 = sort1[['Provinsi', 'Tingkat_Setengah_Pengangguran']]
    h5 = pilih1.head()
    print('5 Kota dengan Tingkat Pengangguran Tertinggi:')
    print()
    print(h5)
    
def pendterend():
    sort = data.sort_values('Tingkat_Penyelesaian_Pendidikan', ascending=True)
    pilih2 = sort[['Provinsi', 'Tingkat_Penyelesaian_Pendidikan']]
    h5 = pilih2.head()
    print('5 Kota dengan Tingkat Penyelesaian Pendidikan Terendah:')
    print()
    print(h5)

def ngangterend():
    sort1 = data.sort_values('Tingkat_Setengah_Pengangguran', ascending=True)
    pilih1 = sort1[['Provinsi', 'Tingkat_Setengah_Pengangguran']]
    h5 = pilih1.head()
    print('5 Kota dengan Tingkat Pengangguran Terendah:')
    print()
    print(h5)

while True:
    print('\nMenu Analisis Data:')
    print('\n1. 5 Kota dengan Tingkat Penyelesaian Pendidikan Tertinggi')
    print('2. 5 Kota dengan Tingkat Pengangguran Tertinggi')
    print('3. 5 Kota dengan Tingkat Penyelesaian Pendidikan Terendah')
    print('4. 5 Kota dengan Tingkat Pengangguran Terendah')
    print('5. Tampilkan Keseluruhan Data Frame')
    print('0. Keluar')
    i1 = int(input('\nMasukkan Pilihan Anda: '))
    if i1 == 1:
        pendter()
        next = input('\nEnter untuk lanjut....')
        print('========================================================')
    elif i1 == 2:
        ngangter()
        next = input('\nEnter untuk lanjut....')
        print('========================================================')
    elif i1 == 3:
        pendterend()
        next = input('\nEnter untuk lanjut....')
        print('========================================================')
    elif i1 == 4:
        ngangterend()
        next = input('\nEnter untuk lanjut....')
        print('========================================================')
    elif i1 == 5:
        print('\nKeseluruhan Data Frame: ')
        print()
        print(data)
        next = input('\nEnter untuk lanjut....')
        print('========================================================')
    elif i1 == 0:
        print('Terima Kasih Telah Menggunakan Program ini!!')
        print()
        break
    else:
        print('Pilihan Tidak Tersedia')
        next = input('\nEnter untuk lanjut....')
        print('========================================================')