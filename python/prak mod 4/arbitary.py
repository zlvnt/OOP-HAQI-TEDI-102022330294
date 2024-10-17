def jumlahkan(*args):
    total = 0
    for angka in args:
        total += angka
    return total

print(jumlahkan(1, 2, 3, 4))