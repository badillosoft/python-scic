# Práctica VIII - Expresiones regulares

Muchas veces necesitamos trabajar con textos y más aún extraer datos de ellos. Cuando analizamos el contenido de un mensaje, notamos que la información contenida sigue ciertos patrones repetitivos, por ejemplo, si leyeramos el mensaje "Hola soy Ana, mi correo es ana@gmail.com y mi número es 551 234 5678, me puedes depositar $100.00 en mi tarjeta, es Banamex, el número de plástico es 5213 4567 8901 2345" podríamos notar que dicho mensaje contiene un nombre de persona "Ana", un correo electrónico "ana@gmail.com", un número telefónico "551 234 5678", un valor monetario "$100.00", el nombre de un banco "Banamex", y un número bancario "5213 4567 8901 2345". Esto es debido a que poseemos técnicas avanzadas para encontrar patrones, sin embargo, para un programa computacional es simplemente una cadena de texto.

Para poder extrar dichos patrones del mensaje haremos uso de las *Expresiones Regulares*, las cuales consisten en definir secuencias finitas o infinitas de caracteres consecutivos llamados *tokens*. Un *token* es un conjunto posible de caracteres válidos para cumplir un patrón, por ejemplo `[a-zA-Z0-9]` representa el token capaz de detectar caracteres que van de la `a` a la `z`, de la `A` a la `Z` y del `0` al `9`, dicho token valida cualquier cadena que tenga uno de esos caracteres.

Un token puede ser repetido varias veces para validar patrones más complejos, por ejemplo, si tenemos el patrón `aba` valida todas las cadenas que tengan los tokens `a`, `b` y `a` consecutivamente, por ejemplo, algunas cadenas validas serían "abanico", "cabal", "acababa" donde las coincidencias serían "(aba)nico", "c(aba)l", "ac(aba)ba". Un token más complejo como `[ab][0-5]` validaría todas las cadenas que empiezan con los caracteres `a` o `b`, seguidos de un dígito del `0` al `5`, por ejemplo, algunas cadenas válidas en ese patrón serían "a4", "b3", "a0", "xwb290", sin embargo, algunas cadenas no válidas serían "x1", "c4", "ad3a".

Algunos tokens comunes son `\w` que es contracción de `[A-Za-z0-9]`, `\d` contracción de `[0-9]` y `\s` que representa un espacio en blanco. Puedes encontrar más información aquí https://es.wikipedia.org/wiki/Expresi%C3%B3n_regular

Finalmente, si quisieramos construir un patrón que detecte correos electronicos haríamos `[\w\_\-\.]+@\w+\.\w{2,3}` que se refiere a todos los caracteres alfanuméricos, incluyendo punto y guines repetidos al menos una vez, seguido del caracter arroba seguido de al menos un alfanumérico, seguido de un punto y de dos a tres alfanuméricos. Si no puedes leer correctamente dicho patrón intenta revisar los operadores de repetición `+`, `*` y `{n,m}` de las expresiones regulares.

## Expresiones Regulares en Python

Para hacer uso de expresiones regulares en python, debemos usar la libería `re` y el método `finditer` que creara un iterador de coincidencias dentro de un texto, el cual podremos iterar y obtener la posición del caracter inicial dentro del texto.

~~~py
import re

pattern = "[\w\_\-\.]+@\w+(\.\w{2,3}){1,2}"

text = "Hola soy Ana, mi correo es ana@gmail.com y mi número es 551 234 5678, me puedes depositar $100.00 en mi tarjeta, es Banamex, el número de plástico es 5213 4567 8901 2345"

for m in re.finditer(pattern, text):
    email = m.group(0)
    n = len(email)
    i = m.start(0)
    context = "..." + text[i-10:i+n+10] + "..."
    print("Se encontró <{}> con longitud {} en la posición {} [{}]".format(email, n, i, context))
~~~

Problemas

* Crear un patrón de una expresión regular que detecte números telefónicos de 10 dígitos con al menos los siguientes formatos: "XXXXXXXXXX", "XXX-XXX-XXXX", "XXX XXX XXXX".

* Crear un programa que extraíga todos los números telefónicos de un archivo y los guarde en un segundo archivo (sólo el número telefónico). 

<br><br>
<hr>
<small>
Python Científico - Alan Badillo Salas (badillo.soft@hotmail.com)<br>
Instituto Politécnico Nacional - Centro de Investigación en Cómputo
</small>
