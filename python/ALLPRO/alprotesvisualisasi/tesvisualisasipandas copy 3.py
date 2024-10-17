import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

iris = pd.read_csv('iris.csv', names=['panjang_sepal', 'lebar_sepal', 'panjang_petal', 'lebar_petal', 'class'])

print(iris.head())

colors = {'Iris-setosa':'r', 'Iris-versicolor':'g', 'Iris-virginica':'b'}

def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2))

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2))
plt.show()