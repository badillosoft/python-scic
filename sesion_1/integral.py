def f(x):
    return x ** 2 - 2 * x + 4

a = 0
b = 3

n = 5

d = (b - a) / n

I = 0

for i in range(0, n):
    xi = a + i * d
    xii = a + (i + 1) * d
    
    fi = f(xi)
    fii = f(xii)

    h = (fi + fii) / 2

    A = d * h

    I += A

print("Integral de f(x)={:.4f}".format(I))