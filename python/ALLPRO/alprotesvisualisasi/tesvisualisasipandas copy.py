import matplotlib.pyplot as plt
import pandas as pd

iris = pd.read_csv('iris.csv', names=['panjang_sepal', 'lebar_sepal', 'panjang_petal', 'lebar_petal', 'class'])

print(iris.head())

colors = {'Iris-setosa':'r', 'Iris-versicolor':'g', 'Iris-virginica':'b'}

for i in range(len(iris['panjang_sepal'])):
    plt.scatter(iris['panjang_sepal'][i], iris['lebar_sepal'][i],color=colors[iris['class'][i]])

plt.title('Iris Dataset')
plt.xlabel('panjang_sepal')
plt.ylabel('lebar_sepal')
plt.show()