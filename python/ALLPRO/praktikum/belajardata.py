import pandas as pd

data = pd.read_csv('datad.csv')
urut = pd.DataFrame(data)

data_info = data.info()
print(data_info)

desc = data.describe()
print("\nDeskripsi Statistik Dasar:")
print(desc)

num_rows, num_columns = data.shape
print(f"Jumlah Baris: {num_rows}")
print(f"Jumlah Kolom: {num_columns}")

data['Peningkatan_2021_2022'] = data['Sanitasi_2022'] - data['Sanitasi_2021']
data['Peningkatan_2022_2023'] = data['Sanitasi_2023'] - data['Sanitasi_2022']

data['Total_Peningkatan'] = data['Peningkatan_2021_2022'] + data['Peningkatan_2022_2023']

provinsi_tertinggi = data.loc[data['Total_Peningkatan'].idxmax(), 'Provinsi']
nilai_tertinggi = data['Total_Peningkatan'].max()

kolom_sanitasi = ['Sanitasi_2021', 'Sanitasi_2022', 'Sanitasi_2023']

correlation_sanitasi = data[kolom_sanitasi].corr()

detail_provinsi = data[data['Provinsi'] == provinsi]
    if not detail_provinsi.empty:
        print(f"Detail Performa Sanitasi untuk Provinsi {provinsi}:")
        print(detail_provinsi)
    else:
        print("Provinsi tidak tersedia dalam data.")

def main():
    while True:
        provinsi = input("Masukkan nama provinsi: ")

        detail_performa_sanitasi(provinsi)

        if not detail_performa_sanitasi(provinsi).empty:
            break