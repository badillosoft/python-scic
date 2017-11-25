# Crear un programa que defina la función criba(m, A)
# que ajusta a 0 todos los multiplos de m comenzando en
# el índice m

def criba(m, A):
    for i in range(m + 1, len(A)):
        if (i + 1) % m == 0:
            A[i] = 'X'
    return A

print (criba(3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
print (criba(5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))

A = list(range(1, 1001))
print (A)
A = criba(2, A)
print (A)
A = criba(3, A)
print (A)
A = criba(5, A)
print (A)