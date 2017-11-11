# Hay un archivo CSV que almacena en la primer línea
# los valores del eje X y en la segunda línea
# los valores del eje Y

# * Se requiere un programa que le solicite al usuario
# el nombre del archivo
# * Abrir el archivo en modo lectura
# * Extraer las primeras líneas Xs, Ys
# * Partir la línea en una lista de cadenas
# con el separador coma `,`
# * Recuperar los valores de tipo float
# de las listas X, Y
# * Graficar las listas X, Y

nombre = input("Dame el nombre del archivo: ")

f = open(nombre, "r")

Xs = f.readline()
Ys = f.readline()

f.close()

Xs = Xs.split(",")
Ys = Ys.split(",")

print(Xs)
print(Ys)

def T(s):
    return float(s)

X = list(map(T, Xs))
Y = list(map(T, Ys))

import matplotlib.pyplot as plt

plt.plot(X, Y, "r-")

plt.show()
