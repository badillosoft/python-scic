# Práctica IV - Diccionarios

Los diccionarios son quizás una de las estructuras más utilizadas dentro del procesamiento de datos en el ámbito científico, debido a que son colecciones que nos permiten almacenar valores como en un lista con la diferencia que en lugar de esperar índices automáticos para cada valor almacenado, colocamos manualmente una clave.

## Crear un diccionario

Para crear un diccionario debemos utilizar las llaves `{}` y dentro de ellas colocar una clave y un valor separados por dos puntos `:`, como se muestra en el siguiente código que almacena en un diccionario los datos de una persona:

~~~py
persona = {
    "nombre": "Alan B",
    "edad": 100,
    "genero": "H"
}
~~~

Recordemos que lo que cabe en una variable puede ser un `número`, una `cadena`, un `booleano`, un `None` o una colección (`lista []`, `tupla ()`, `diccionario {}`). Por lo tanto, podemos almacenar un diccionario dentro de otro o una lista dentro de un diccionario para formar datos complejos como se muestra:

~~~py
persona = {
    "nombre": "Alan B",
    "edad": 100,
    "lenguajes": ["es", "us", "it", "ru"],
    "direccion": {
        "calle": "Av. Siempre Viva",
        "no_ext": 123,
        "no_int": 0,
        "colonia": "Del Valle",
        "delegacion": "Venustiano Carranza",
        "ciudad": "Ciudad de México"
    }
}
~~~

Además de esto, las listas igual pueden contener diccionarios como se muestra a continuación:

~~~py
puntos = [
    { "x": 1, "y": 3 },
    { "x": 2, "y": 6 },
    { "x": 3, "y": 9 },
    { "x": 4, "y": 12 },
    { "x": 5, "y": 15 }
]

for p in puntos:
    print("%d, %d".format(p["x"], p["y"]))
~~~

## Problemas

* Crear un diccionario que almacene los valores de un producto (nombre, marca, descripción, costo, etc).

* Crear un diccionario que almacene los datos de un experimento (nombre, tiempo, PH, temperatura, etc).

* Generar una lista de diccionarios con 1000 puntos aleatorios en el intervalor (-10, 10) en ambos ejes.

* De la lista de puntos anterior, filtrar los puntos que se ubican a máximo 2 unidades del punto (1, 2).

* De la lista de puntos anterior, filtrar los puntos que tienen un X negativo.

* De la lista anterior, generar otra lista donde se intercambien los valores de las X y las Y.

<br><br>
<hr>
<small>
Python Científico - Alan Badillo Salas (badillo.soft@hotmail.com)<br>
Instituto Politécnico Nacional - Centro de Investigación en Cómputo
</small>