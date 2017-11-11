f = open("resorte.csv", "r")

X = []
Y = []

for linea in f:
    srow = linea.split(",")
    row = list(map(lambda s: float(s), srow))
    x = row[0]
    y = row[1]
    X.append(x)
    Y.append(y)

f.close()

import matplotlib.pyplot as plt

plt.plot(X, Y)

plt.show()
