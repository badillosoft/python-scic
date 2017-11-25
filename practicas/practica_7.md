# Práctica VII - Clasificadores (Parte I)

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

## Clasificar datos en python

Para poder clasificar datos lo haremos a través de la librería `Sklearn` de `Sci-kit`, la estructura básica consiste en formar una matriz con los datos de entrenamiento para las características deseadas y un vector de prueba que muestra un valor real de entrenamiento para la matriz de prueba, la matriz debe ser codificada numéricamente, por ejemplo, si la caracterísitca es de tipo categórica como `C`, `NC` entonces podemos asignar valores `C = 1`, `NC = 2`, de forma que si el resultado es 1 sabremos que se refiere a `C` y si es dos lo traduciremos como `NC`.

> Ejemplo de un clasificador genérico (solo demostración, código no funcional)

~~~py
# Importamos el clasificador
from sklearn.TIPOCLASIFICADOR import CLASIFICADOR

# Construimos la matriz de datos para las características observables
# C = 1, NC = 2
X = [
    [60, 15, 1],
    [80, 10, 1],
    [30, 8, 2],
    [10, 3, 1]
]

# Construimos el vector de resultados para las características a predecir
# Naranja = 1, Manzana = 2, Plátano = 3, Uva = 4
Y = [
    1,
    2,
    3,
    4
]

# Creamos un clasificador de la clase CLASIFICADOR
clf = CLASIFICADOR()

# Ajustamos el clasificador a los datos de entrenamiento
# después de esto el clasificador ya aprendió como se comportan los datos
# y pueden predecir que pasaría con otro conjunto de datos
clf.fit(X, Y)

# Creamos pruebas para predecir que fruta es
Xp = [
    [50, 12, 1],
    [90, 11, 1],
    [30, 15, 2],
    [10, 4, 1]
]

# Obtenemos el vector que predice las frutas, recordando la codificación
Yp = clf.predict(Xp)
~~~

## Clasificadores de Árbol

Un clasificador de árbol se basa en construir un árbol binario el cual toma decisiones sobre las características de los datos, por ejemplo, si se quisiera entrenar un clasificador a partir de las características `x`, `y`, `z` para predecir la variable `w`, entonces podríamos construir un árbol que prediga por ejemplo, si `x <= 3` y `y > 2` entonces `w = 2`. Este tipo de comparaciones forman una jerarquía de decisiones las cuales son aplicadas una a una a los datos para poder predecir en base a esas decisiones que debería ser nuestra variable a predecir.

> Ejemplo de un clasificador por árbol de decisión.

~~~py
from sklearn.tree import DecisionTreeClassifier

X = [
    [60, 15, 1],
    [80, 10, 1],
    [30, 8, 2],
    [10, 3, 1],
]

Y = [
    1,
    2,
    3,
    4
]

clf = DecisionTreeClassifier()

clf.fit(X, Y)

Xp = [
    [50, 12, 1],
    [90, 11, 1],
    [30, 15, 2],
    [10, 4, 1]
]

Yp = clf.predict(Xp)
~~~

Podemos extraer el árbol de decisión en un archivo PDF mediante `graphviz`. Intenta instalarlo y buscar la documentación para instalarlo y ejecuta el siguiente programa que debería generar un archivo PDF con el diagrama del árbol.

~~~py
from sklearn.datasets import load_iris
from sklearn import tree
import graphviz 

iris = load_iris()

clf = tree.DecisionTreeClassifier()

clf = clf.fit(iris.data, iris.target)

dot_data = tree.export_graphviz(clf, out_file=None) 

graph = graphviz.Source(dot_data)

graph.render("iris")
~~~

## Clasificadores por Redes Neuronales

Un clasificador por Redes Neuronales se basa en unidades lógicas llamas neuronas o perceptrones las cuales toman un conjunto entradas para mediante una función de activación determinar si se activa o no la neurona. La activación esta dada por pesos ajustables y el ajuste correcto de los pesos en un monton de neuronas generan un sistema sensible a la entrada y que genera una salida esperada.

~~~py
from sklearn.neural_network import MLPClassifier

X = [
    [60, 15, 1],
    [80, 10, 1],
    [30, 8, 2],
    [10, 3, 1],
]

Y = [
    1,
    2,
    3,
    4
]

clf = MLPClassifier()

clf.fit(X, Y)

Xp = [
    [50, 12, 1],
    [90, 11, 1],
    [30, 15, 2],
    [10, 4, 1]
]

Yp = clf.predict(Xp)
~~~

## Problemas

* Crea una matriz de experimentos aleatoria, donde se midan al menos 8 características de un experimento, por ejemplo, temperatura, presión, humedad, densidad, etc.

* Separar la matriz en X y Y, donde X son las caracterísitcas observables y Y son resultados experimentales.

* Crear un Clasificador (el que desee) y predecir algunos valores similarares a los de su tabla.

<br><br>
<hr>
<small>
Python Científico - Alan Badillo Salas (badillo.soft@hotmail.com)<br>
Instituto Politécnico Nacional - Centro de Investigación en Cómputo
</small>
