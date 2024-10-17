import numpy as np
from scipy import stats

def hitung_range(data):
    return np.max(data) - np.min(data)

def hitung_persentil(data, p):
    sorted_data = np.sort(data)
    position = (len(sorted_data) - 1) * p / 100
    floor = int(np.floor(position))
    remainder = position - floor
    if floor == len(sorted_data) - 1:
        return sorted_data[floor]
    else:
        return sorted_data[floor] + remainder * (sorted_data[floor + 1] - sorted_data[floor])

def hitung_quartil(data):
    return np.percentile(data, [25, 50, 75])

def hitung_simpangan_baku(data):
    return np.std(data)

def hitung_koefisien_variasi(data):
    return (np.std(data) / np.mean(data)) * 100

def hitung_mean(data):
    return np.mean(data)

def hitung_median(data):
    return np.median(data)

def hitung_interquartile_range(data):
    quartiles = np.percentile(data, [25, 75])
    return quartiles[1] - quartiles[0]

def main():
    data = input("Masukkan data (pisahkan dengan koma): ").split(',')
    data = [float(x.strip()) for x in data]
    
    print("\n1. Range: ", hitung_range(data))
    
    p = float(input("\nMasukkan persentil yang ingin dihitung (0-100): "))
    print("2. Persentil ke-{0}: {1}".format(p, hitung_persentil(data, p)))
    
    quartiles = hitung_quartil(data)
    print("\n3. Quartil 1: ", quartiles[0])
    print("   Quartil 2 (Median): ", quartiles[1])
    print("   Quartil 3: ", quartiles[2])
    
    print("\n4. Simpangan Baku: ", hitung_simpangan_baku(data))
    
    print("\n5. Koefisien Variasi: ", hitung_koefisien_variasi(data))
    
    print("\n6. Mean: ", hitung_mean(data))
    
    print("\n7. Median: ", hitung_median(data))
    
    print("\n9. Interquartile Range: ", hitung_interquartile_range(data))

if __name__ == "__main__":
    main()
