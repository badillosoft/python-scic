# Práctica VIII - Procesamiento de lenguaje natural y textos

~~~py
import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download()
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
