# Leer el archivo mat.csv
f = open("mat.csv", "r")

# Definir una función de transformación
# que recibe una cadena y devuelve
# la cadena convertida en entero
def T(s):
    return int(s)

# Crear una lista para contener las
# listas números de cada fila
mat = []

# Iteramos línea por línea del archivo
for linea in f:
    # Partimos la línea (cadena)
    # en varías cadenas por el separador ,
    srow = linea.split(",")
    # Transformar la lista srow (lista de cadenas)
    # en una lista de números
    row = map(T, srow)
    # Agreagar el mapeo convertido en lista
    # en la lista de listas (la matriz)
    mat.append(list(row))

print(mat)

f.close()