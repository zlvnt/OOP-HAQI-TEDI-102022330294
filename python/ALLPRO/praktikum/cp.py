import pandas as pd

def muat_data():
    import pandas as pd
dt = pd.read_csv('sanitasi.csv')

def tampilkan_data_frame(data):
    print(dt)

def tampilkan_gambaran_umum(data):
    print('\nInformasi Data:')
    info = dt.info()
    dsc = dt.dsc()
    print(info)
    print(dsc)

def sepuluh_provinsi_teratas(data):
    print('\n10 Provinsi dengan performa terbaik tahun 2023:')
    sort = dt.sort_values('2023', ascending = False)
    pilih = sort[['Provinsi', '2023']]
    hed = pilih.head()
    print(hed)
    
def provinsi_dengan_peningkatan_terbesar(data):
    dt['a'] = dt['2022'] - dt['2021']
    dt['b'] = dt['2023'] - dt['2022']
    dt['c'] = dt['a'] + dt['b']
    pk = dt.sort_values('c')
    max = pk.max()
    pk1 = max['Provinsi']
    print(f'\nProvinsi dengan peningkatan terbesar dari tahun 2021 ke 2023: {pk1} (Peningkatan: {max}')

def analisis_korelasi(data):
    sanitasik = dt['2021', '2022', '2023']
    sanitasi = sanitasik.corr()
    print(sanitasi)


def kinerja_provinsi_tertentu(data, nama_provinsi):
    # Hint: Isi dengan fungsi untuk menampilkan kinerja provinsi tertentu (pakai data.loc dan kondisi jika data tidak ada)
    pass

def utama():
    data = muat_data()
    while True:
        print("=====================================")
        print("Menu Analisis Data:")
        # Hint: Tambahkan pilihan menu sesuai deskripsi soal
        print("=====================================")
        pilihan = int(input("Masukkan pilihan Anda: "))
        if pilihan == 1:
            tampilkan_data_frame(data)
        elif pilihan == 2:
            tampilkan_gambaran_umum(data)
        elif pilihan == 3:
            sepuluh_provinsi_teratas(data)
        elif pilihan == 4:
            provinsi_dengan_peningkatan_terbesar(data)
        elif pilihan == 5:
            analisis_korelasi(data)

            
            
            
            
            
        # Hint: Tambahkan if else untuk setiap pilihan menu sesuai deskripsi soal

if __name__ == "__main__":
    utama()


import pandas as pd

# Membaca data dari file CSV
data = pd.read_csv('pemain_bola.csv')

# Menambahkan kolom rata-rata
data['Average'] = (data['Speed'] + data['Stamina'] + data['Attack'] + data['Defense']) /4

# Mengurutkan data berdasarkan rata-rata tertinggi
data = data.sort_values('Average', ascending=False)

# Memfilter data berdasarkan umur antara 23 dan 28 tahun
data = data[(data['Umur']>= 23) & (data['Umur'] <= 28)]

# Mengambil 11 data teratas
data = data.head(11)

# Menghitung total harga
harga = data['Harga ($)'].sum()
print(f"\nTotal harga: ${harga}")

# Mencari nilai tertinggi dari setiap kolom ability beserta nama pemain
trtg = data['Attack'].max()
nm = trtg[['nama','Attack']]
print(nm)
# Menampilkan data
print(data)