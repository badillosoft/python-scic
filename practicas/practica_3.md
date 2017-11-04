# Práctica III - Manejo de archivos

Un archivo es una secuencia de bytes que almacena información y puede ser manipulado como un archivo binario (byte por byte) o un archivo de texto (caracter por caracter). Los archivos de texto serán de mayor importancia ya que son más manipulables y legibles.

En Python podemos recuperar el contenido de un archivo mediante la función `open(name, mode)` que devuelve un cursor al archivo con ruta `name` y modo de apertura `mode`.

La ruta del archivo consiste simplemente en el nombre del archivo ubicado en el lugar donde ejecutemos nuestro *script* o la ruta absoluta si comienza por `C:/` o `/` dependiendo el sistema operativo.

El modo de apertura le provee al cursor diversos métodos para escribir o leer, los principales modos son `"r"` que provee el método `read()` para leer el contenido del archivo y `"w"` que provee el método `write(...)` que permite escribir una cadena en el archivo.

Finalmente cabe decir que el cursor es iterable, por lo que si va dentro de un `for` itera cada línea del archivo.

## Leer el contenido de un archivo

En el siguiente ejemplo se muestra como leer un archivo ubicado en el mismo directorio de ejecución.

~~~py
f = open("datos.txt", "r")

for linea in f:
    print("Contenido: {}".format(linea))
~~~

## Escribir una lista de valores en un archivo

El siguiente ejemplo muestra como escribir una lista de valores en un archivo con el formato *CSV* que simplemente es cada valor separarlo por coma.

~~~py
~~~

## Problemas

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
Python Científico - Alan Badillo Salas (badillo.soft@hotmail.com)<br>
Instituto Politécnico Nacional - Centro de Investigación en Cómputo
</small>