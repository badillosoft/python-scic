# Crear un programa que defina la función multiplos(m, n)
# y devuelve una lista con los primero n multiplos 
# del número m comenzando en 1.

def multiplos(m, n):
    A = [1]

    for i in range(1, n):
        p = i * m
        A.append(p)

    return A

print(multiplos(3, 5))
print(multiplos(7, 10))

def multiplos2(m, n):
    A = list(range(1, n))
    B = [1] + list(map(lambda i: i * m, A))
    return B

print(multiplos2(3, 5))
print(multiplos2(7, 10))