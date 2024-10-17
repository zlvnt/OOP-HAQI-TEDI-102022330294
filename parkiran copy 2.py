import math
import datetime

data_parkiran = []

while True:
    print("\n======== Parkiran Telkom ========")
    print("1.\tMasuk Area Parkir")
    print("2.\tKeluar Area Parkir")
    print("3.\tAdmin mode")
    print("4.\tSelesai")
    try:
        mode = int(input("Pilih mode yang ingin dipilih (1 / 2 / 3 / 4): "))
        if mode == 1:
            print("\n======== Masuk Area Parkir ========")
            data_plat = input("Masukkan Plat Nomor Anda: ")
            data_masuk = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            data_entry = {"data_plat": data_plat, "data_masuk": data_masuk, "data_keluar": None, "date_time": 0, "data_biaya": 0}
            data_parkiran.append(data_entry)
            print("Kendaraan Telah Tercatat!")
            print("Silahkan masuk")

        elif mode == 2:

            if not data_parkiran:
                print("Tidak ada kendaraan di parkiran")
                
            else:
                plat_nomor = input("\nMasukkan Plat Nomor Anda: ")
                found = False
                for entry in data_parkiran:
                    if plat_nomor == entry['data_plat']:
                        if entry ['data_keluar'] is None:
                            data_keluar = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            entry['data_keluar'] = data_keluar
                            found = True

                            masuk_time = datetime.datetime.strptime(entry['data_masuk'], "%Y-%m-%d %H:%M:%S")
                            keluar_time = datetime.datetime.strptime(entry['data_keluar'], "%Y-%m-%d %H:%M:%S")

                            time = keluar_time - masuk_time
                            entry['data_time'] = math.ceil(time.total_seconds())
                            
                            data_biaya_per_60_detik = 10000

                            if entry['data_time'] <= 60:
                                entry['data_biaya'] = data_biaya_per_60_detik
                            elif entry['data_time'] <= 240:
                                rounded_time = ((entry['data_time'] - 1) // 60 + 1) * 60
                                entry['data_biaya'] = data_biaya_per_60_detik * (rounded_time // 60)
                            elif entry ['data_time'] <= 360:
                                entry['data_biaya'] = data_biaya_per_60_detik * 4
                                entry['data_biaya'] += entry['data_biaya'] * 0.1
                            else:
                                entry['data_biaya'] = data_biaya_per_60_detik * 4
                                entry['data_biaya'] += entry['data_biaya'] * 0.25

                            while True:
                                print(f"Waktu yang anda habiskan adalah {entry['data_time']} detik !")
                                print(f"Total Biaya\t\t: {entry['data_biaya']}")
                                nominal = int(input("Masukkan Nominal\t: "))
                                kembalian = nominal - entry['data_biaya']

                                if kembalian < 0:
                                    print("Uang anda tidak cukup! Silakan masukkan nominal yang lebih besar.")
                                elif kembalian == 0:
                                    print("Gerbang Keluar telah Terbuka. Terima Kasih!")
                                    break
                                else:
                                    print(f"Kembalian\t\t: {kembalian}")
                                    print("Gerbang Keluar telah Terbuka")
                                    print("Terima Kasih!")
                                    break 

                        else:
                            print("Kendaraan sudah keluar sebelumnya.")
                            found = True
                            break

                if not found:
                    print("Tidak ada Plat Nomor tersebut di parkiran!")
        elif mode == 3:
                input_pin = int(input("Masukkan PIN: "))
                if input_pin == 1:
                    print("\nData parkiran:")
                    for entry in data_parkiran:
                        print(f" Plat Nomor: {entry['data_plat']}\n Masuk: {entry['data_masuk']}\n Keluar: {entry['data_keluar']}\n")
                else:
                    print("PIN Salah, Kamu tidak dapat mengakses fitur Admin!")
        elif mode == 4:
            break
        else:
            print("Pilihan tidak tersedia!")
        input("\nPress Enter to continue...\n")
    except ValueError:
        print("Mode tidak tersedia")
