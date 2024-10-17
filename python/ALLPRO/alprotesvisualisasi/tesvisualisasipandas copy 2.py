import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

iris = pd.read_csv('iris.csv', names=['panjang_sepal', 'lebar_sepal', 'panjang_petal', 'lebar_petal', 'class'])

print(iris.head())

colors = {'Iris-setosa':'r', 'Iris-versicolor':'g', 'Iris-virginica':'b'}

plt.subplot(211)

plt.hist(iris[iris['class'] == 'Iris-setosa']['panjang_sepal'], color='r', alpha=0.5, label='Iris-setosa')
plt.hist(iris[iris['class'] == 'Iris-versicolor']['panjang_sepal'], color='g', alpha=0.5, label='Iris-versicolor')
plt.hist(iris[iris['class'] == 'Iris-virginica']['panjang_sepal'], color='b', alpha=0.5, label='Iris-virginica')

plt.legend()
plt.title('Histogram Panjang Sepal')
plt.xlabel('Panjang Sepal')
plt.ylabel('Frekuensi')

# Menampilkan plot
plt.show()
