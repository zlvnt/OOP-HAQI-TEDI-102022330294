x = [1,2,3,4,5,6]
y = [5,10]
z = []

z.append(x[0] * y[0]) ; z.append(x[1] * y[1])
z.append(x[2] * y[0]) ; z.append(x[3] * y[1])
z.append(x[4] * y[0]) ; z.append(x[1] * y[1])

print (z)