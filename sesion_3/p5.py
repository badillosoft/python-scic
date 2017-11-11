def linspace(a, b, n):
    d = (b - a) / (n - 1)

    X = []

    for i in range(0, n):
        xi = a + i * d
        X.append(xi)

    return X

X = linspace(1, 3, 11)

# ALTERNATIVA
a = 1
b = 3

X = []

for i in range(11):
    x = a + (b - a) / 10
    X.append(x)

print(X)

import math

def T(x):
    return math.sin(x)

Y = list(map(T, X))

print(Y)

import matplotlib.pyplot as plt

plt.plot(X, Y, "r--")

plt.show()