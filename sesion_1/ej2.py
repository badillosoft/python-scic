"""
Alan Badillo Salas
badillo.soft@hotmail.com

Promedio de una lista
"""

# Creamos una lista de números
A = [3, 5, 8, 17, 22, 44, 99]

# Creamos una variable para acumalar la suma
s = 0

# Recorremos cada elemento de la lista A
for x in A:
    # Acumulamos el valor de x en la suma
    s += x

# Obtenemos el número de elementos de la lista A
n = len(A)

# Obtenemos el promedio
p = s / n

# Imprimimos el promedio
print(p)