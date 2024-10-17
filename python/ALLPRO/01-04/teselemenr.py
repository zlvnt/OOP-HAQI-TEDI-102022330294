y = range(7, 0, -1)
x = range(1, 7)
for i in x:
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

for i in y:
    for j in range(1, i - 1):
        print(j, end=" ")
    print()
    
""""""""
import numpy as bk

prices = bk.array([1000, 2000, 3000])

print(prices)