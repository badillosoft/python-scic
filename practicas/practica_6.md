# Práctica VI - Mapeo de datos

Una estructura muy potente para manipular datos en python es crear listas de diccionarios, esta estructura nos permite almacenar información de entidades mediante diccionarios, cada diccionario en la lista será considerada una entidad y cada clave del diccionario será considerado un campo de la entidad.

El siguiente ejemplo muestra una lista de diccionarios que almacena los datos de personas:

~~~py
personas = [
    { "Nombre": "Ana", "Edad": 21, "Genero", "Mujer" },
    { "Nombre": "Beto", "Edad": 13, "Genero", "Hombre" },
    { "Nombre": "Pepe", "Edad": 18, "Genero", "Hombre" },
    { "Nombre": "Laura", "Edad": 29, "Genero", "Mujer" },
]
~~~

Como podemos observar, cada diccionario posee las mismas claves (`Nombre`, `Edad`, `Genero`) y en cada clave se almacenan los datos de la entidad en cuestión.

Algo muy importante que tenemos que aprender al manipular listas de diccionarios es poder extraer información y crear nuevos campos, de forma tal que manipulemos la información sin problemas.

## Extraer los valores de una columna

Para extraer los datos de una columna dentro de nuestra lista de diccionarios, debemos recorrer cada entidad (diccionario) de la lista y extraer el valor almacenado en cierta clave, esto se puede hacer de dos formas y dependerá de ti usar la que se te haga más fácil.

> Extraer los datos de una columna con un `for-in`

~~~py
# personas como está definido arriba
column = "Edad"
values = []

for dic in personas:
    values.append(dic[column])

print(values)
~~~

Observa que `dic[column]` extrae el valor en cada diccionario de la columna deseada (si no existe fallará).

> Extraer los datos de una columna con un mapeo

~~~py
column = "Edad"

values = list(map(lambda dic: dic[column], personas))
~~~

La forma anterior es más compleja, pero recordando que `lambda dic: dic[column]` equivale a definir la función de mapeo que recibe el diccionario y devuelve el valor en tal clave no es del todo díficil.

## Agregar un campo nuevo a cada entidad

Podemos especificar nuevos campos a cada entidad de la lista, simplemente con un mapeo que altere el diccionario original y agregue o modifique campos, pero hay que tener cuidado de no modificar los campos originales a menos que así se desee. Supongamos que en nuestra lista `personas` definida arriba queremos agregar el campo `Mayor_Edad` el cual se construye determinando si el campo `Edad` convertido a entero es mayor o igual a 18.

~~~py
# personas como se define arriba

def T(dic):
    edad = int(dic["Edad"])
    if edad >= 18:
        dic["Mayor_Edad"] = "SI"
    else:
        dic["Mayor_Edad"] = "NO"
    return dic

personas = list(map(T, personas))
~~~

## Problemas

* Generar un archivo CSV con valores aleatorios que almacene los datos de un experimento ficticio que consta de los campos `Tiempo`, `Dilatacion`, `Temperatura`, `Densidad`.

* Cargar los datos con la función `scic.load_data_csv(...)` e imprimirlos.

* Generar el dato categórico `Invalido` el cual se determina si la temperatura es mayor a `60` (`SI` o `NO`).

* Generar el dato categórico `Sobredilatado` el cual se determina si la dilatación es mayor a `4`.

* Graficar la columna `Invalido` y la columna `Sobredilatado` en dos gráficas de pastel (en ventanas distintas).

<br><br>
<hr>
<small>
Python Científico - Alan Badillo Salas (badillo.soft@hotmail.com)<br>
Instituto Politécnico Nacional - Centro de Investigación en Cómputo
</small>
