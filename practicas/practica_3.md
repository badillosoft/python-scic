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

f.close()
~~~

Observa que mandamos a llamar al método `close` para cerrar el archivo.

## Escribir una lista de valores en un archivo

El siguiente ejemplo muestra como escribir una lista de valores en un archivo con el formato *CSV* que simplemente es cada valor separarlo por coma.

~~~py
A = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

f = open("datos2.txt", "w")

for x in A:
    f.write("{}, ".format(x))

f.close()
~~~

## Problemas

* Crear un programa que lea cada línea de un archivo e indique cuánto mide cada línea.

* Crear un programa que almacene los primeros 20 números de la sucesión de Fibonacci en formato *csv*.

<br><br>
<hr>
<small>
Python Científico - Alan Badillo Salas (badillo.soft@hotmail.com)<br>
Instituto Politécnico Nacional - Centro de Investigación en Cómputo
</small>