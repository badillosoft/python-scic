# Práctica II - Integral aproximada

La integral definida en el intervalo cerrado de `a` a `b` para una función dependiente de una sola variable representa el área bajo la curva definida por la función. Para aproximar dicha integral (o área) podemos partir el intervalor en `n` partes de tal forma que se generen `n + 1` puntos equidistantes sobre el intervalo de `a` a `b`, siendo los puntos `x0`, `x1`, `x2`, ..., `xn` aquellos puntos que definen un lado derecho e izquierdo para un trapecio. 

El punto `x0` equivale al punto `a` sobre el eje de las `X` y el punto `xn` equivale al punto `b` sobre el mismo eje. Cada punto está separado por la misma distancia `Δ = (b - a) / n`, es decir, que la distancia entre `x0` y `x1` es `Δ`, lo mismo para cualquier otro `xi` y `xi+1`. Esto quiere decir que si trazamos un trapecio con su base en los extremos `xi` y `xi+1` en el eje `X` y de alturas `f(xi)` y `f(xi+1)` podemos calcular el área del trapecio mediante un rectángulo cuya altura es el promedio de `f(xi)` y `f(xi+1)` (`H = (f(xi) + f(xi+1)) / 2`) y de base la diferencia absoluta entre `xi` y `xi+1`, es decir, la distancia `B = Δ`. Por lo tanto, el área del trapecio es `Ai = Bi * Hi = Δ * (f(xi) + f(xi+1)) / 2`. Así la integral de la función `f(x)` en el intervalo de `a` a `b` puede aproximarse como la suma de las áreas `Ai` para `0 <= i < n`.

Analiza el siguiente programa que calcula la integral aproximada de la función `x ** 2 - 2 * x + 4` en el intervalor de `a = 0` y `b = 3`.

~~~py
# Definimos la función `f` que recibe a `x` y devuelve `x ** 2 - 2 * x + 4`
def f(x):
    return x ** 2 - 2 * x + 4

# Definimos las variables para el intervalor de `a` a `b`
a = 0
b = 3

# Definimos el número de particiones, que equivale al número de
# trapecios a formar.
n = 5

# Calculamos `Δ`
d = (b - a) / n

# Creamos un acumulador para almacenar la suma de las áreas que
# equivale a la integral aproximada
I = 0

# Recorremos 0 <= i < n
for i in range(0, n):
    # Calculamos xi y xi+1
    xi = a + i * d
    xii = a + (i + 1) * d

    # Obtenemos f(xi) y f(xi+1)
    fi = f(xi)
    fii = f(xii)

    # Calculamos Hi
    h = (fi + fii) / 2

    # Sabiendo que todas las bases son iguales a Δ calculamos Ai
    A = d * h

    # Acumulamos el área en la integral aproximada
    I += A

# Imprimimos el valor de la integral aproximada con 4 decimales
print("Integral de f(x)={:.4f}".format(I))
~~~

## Problemas

* Crea una función llamada Integral(f, a, b, n) que reciba los parámetros `f - función`, `a - número`, `b - número` y `n - número`.

* Dentro de la función `Integral` calcula la integral aproximada con los parámetros enviados y devuelve el dicho valor.

* Ejecuta el siguiente código poniendo antes la definición de la función `Integral` y corrobora que el resultado sea correcto:

~~~py
# TODO: Pon aqui la función Integral(f, a, b, n)

I = Integral(lambda x: x ** 2 - 2 * x + 4, 0, 3, 500)

print("Integral de f(x)={:.4f}".format(I))
~~~

* Comenta brevemente en tu código mediante un comentario en varias líneas (usando """) que significa `lambda x: x ** 2 - 2 * x + 4` y que uso tiene en este código.

<br><br>
<hr>
<small>
Diplomado de Java - Alan Badillo Salas (badillo.soft@hotmail.com)<br>
Instituto Politécnico Nacional - Centro de Investigación en Cómputo
</small>