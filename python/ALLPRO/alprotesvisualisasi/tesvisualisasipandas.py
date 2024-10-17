import matplotlib.pyplot as plt
import pandas as pd
iris = pd.read_csv('iris.csv', names=['panjang_sepal', 'lebar_sepal', 'panjang_petal','lebar_petal', 'class'])
print(iris.head())

plt.scatter(iris['panjang_sepal'], iris['lebar_sepal'])
plt.title('iris dataset')
plt.xlabel('panjang_sepal')
plt.ylabel('lebar_sepal')
plt.show()