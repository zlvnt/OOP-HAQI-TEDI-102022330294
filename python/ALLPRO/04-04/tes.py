import numpy as np

matriks = np.random.rand(6, 6)

rws = matriks[(matriks[:, 1] > 0.4) & (matriks[:, 1] < 0.6)]

print("Matriks Random:")
print(matriks)
print("\nBaris dengan nilai kolom 2 di antara 0.4 dan 0.6:")
print(rws)
