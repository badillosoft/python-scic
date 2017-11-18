# Práctica VI - Clasificadores (Parte I)

Un clasificador es un programa que puede ser entrenado para predecir valores en base a una lista de ejemplos. Los clasificadores sirven para tomar decisiones automáticas que aprende a tráves de ejemplos y son muy útiles cuando es díficil incluso para una persona predecir un valor. Algunas aplicaciones de los clasificadores son poder predecir fallos en experimentos, concluir análisis médicos, aprender a manejar automóviles, aprender comportamientos en la bolsa de valores para decidir si es bueno invertir, entre otros.

Para clasificar un sistema, este debe poder representarse mediante características y se debe poseer una tabla de entrenamiento que contenga los datos para entrenar el clasificador, por ejemplo:

> Tabla de entrenamiento, clasificar frutas

~~~txt
Peso    Altura  Forma   Fruta
60        15      C     Naranja
80        10      C     Manzana
30        8       NC    Platano
10        3       C     Uva
~~~

Los datos anteriores representan los datos para entrenar un clasificador y que este aprenda a determinar que fruta es basado en su peso, altura y forma. Por ejemplo, que fruta debería ser si el peso es 70, la altura 14 y la forma C. Entre más datos de entrenamiento poseamos, mejor debería aprender el clasificador, sin embargo, esto no es cierto para todos los tipos de clasificadores.

Para hacer clasificación en python debemos utilizar un módulo llamado `sklearn` el cual nos va a proveer de una gran variedad de clasficadores que pueden ser consultados en http://scikit-learn.org/stable/supervised_learning.html#supervised-learning

> Instalar sklearn: `pip install sklearn scipy`

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
