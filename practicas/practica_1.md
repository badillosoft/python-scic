# Práctica I - Dominio de listas

Existen distintos tipos de datos que pueden ser almacenados en la memoria mediante variables, los más importantes son `números`, `cadenas`, `booleanos`, `None` y las colecciones de datos. Dentro de las colecciones se encuentran las `listas [·,·]` (arreglos de elementos variable), las `tuplas (·,·)` (arreglos de elementos fijos) y los `diccionarios {·:·,·:·}`.

Para almacenar un valor basta con nombrar una memoria mediante una variable y asignar el valor literal, una copia de otro o una referencia a un dato complejo, por ejemplo, `a = 123` almacena el valor literal `123` que posee un tipo de dato implícito `número`; `x = a` crea una copia del valor contenido en `a` sólo si este es un tipo de dato primitivo (`número`, `cadena`, `booleano` o `None`), sin embargo, si hacemos `b = [1, 2, 3]` contendrá una lista literal con los tres elementos, por lo que, si `y = b`, entonces `y` contiene una referencia a la misma lista de `b`, dado que las colecciones y los objetos son tipos de datos complejos (no primitivos) por lo que se almacenará la referencia y no una copia, esto quiere decir que si por ejemplo hacemos `b.append(4)`, tanto `b` como `y` ahora tendrán un elemento más dado que comparten la misma lista.

## Llenar una lista con los primeros `n` números de la sucesión de Fibonacci

Un número de *Fibonacci* se define como `f(0) = 1`, `f(1) = 1` y `f(n) = f(n - 1) + f(n - 2)` para `n >= 2`. Podemos calcular el número de *Fibonacci* de muchas formas, pero analiza el siguiente código que lo hace mediante un ciclo `for`.

~~~py
n = 20

fi2 = 1 # f(i - 2)
fi1 = 1 # f(i - 1)

print("f(0) = 1")
print("f(1) = 1")

f = [1, 1]

for i in range(2, n + 1):
    fi = fi1 + fi2

    f.append(fi)

    print("f({}) = {}".format(i, fi))

    fi2 = fi1
    fi1 = fi

print(f)
~~~

## Filtro de datos

Supongamos que queremos filtrar los números de *Fibonacci* generados anteriormente de forma que queden sólo aquellos que son pares. Para conseguirlo, deberíamos crear una lista vacía y recorrer número por número de la lista, si este es un número par, deberíamos guardarlos en la lista secundaria. Analiza el siguiente código:

~~~py
f = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946]

g = []

for x in f:
    if x % 2 == 0:
        g.append(x)

print(g)
~~~

Observa del código anterior `x % 2 == 0` que significa `x módulo 2 congruente con 0`, es decir, `Si el residuo de quitarle a x tantos números 2 como quepan es cero`, lo cual significa que si por ejemplo `x = 21`, le podemos quitar `10` veces `2`, sobrando `1` por lo que la condición no se cumple, pero si `x = 34`, le podemos quitar `17` veces `2`, sobrando `0`, entonces, el módulo `2` indica si un número es par si el residuo (módulo) es `0` o impar si es `1`.

## Problemas

* Crea un programa que genere los primero 20 números definidos por la sucesión `f(0) = 0`, `f(1) = 4`, `f(2) = 3` y `f(n) = 2 * f(n - 2) - f(n - 1) + f(n - 3)` para `n >= 3`

* Crea un filtro para la sucesión anterior que almacene todos los números que son multiplos de 7 (x módulo 7 congruente con 0).

<br><br>
<hr>
<small>
Python Científico - Alan Badillo Salas (badillo.soft@hotmail.com)<br>
Instituto Politécnico Nacional - Centro de Investigación en Cómputo
</small>