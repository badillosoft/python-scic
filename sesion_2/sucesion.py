# f(0) = 0 => f(n - 3) => fi3
# f(1) = 4 => f(n - 2) => fi2
# f(2) = 3 => f(n - 1) => fi1

fi3 = 0
fi2 = 4
fi1 = 3

f = [0, 4, 3]

for i in range(3, 21):
    # Calculamos el i-ésimo elemento de la sucesión
    fi = 2 * fi2 - fi1 + fi3

    # Agregamos el i-ésimo elemento a la lista
    f.append(fi)

    print("f({}) = {}".format(i, fi))

    # Recorremos los elementos anteriores una posición
    # Nota: Ten cuidado de hacerlo al revés
    fi3 = fi2
    fi2 = fi1
    fi1 = fi

print(f)

g = []

for x in f:
    if x % 7 == 0:
        print(x)
        g.append(x)

print(g)