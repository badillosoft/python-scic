# Práctica V - Graficación en MatPlotLib (Parte I)

Uno de los reportes más utilizados para exponer los resultados de un análisis son las gráficas. En Python podemos dibujar gráficas mediante la librería `matplotlib` la cual provee diversas formas de graficar figuras.

## Instalar `matplotlib`

Para instalar `matplotlib` basta con ejecutar el comando:

> `$ pip install matplotlib`

Si no encuentra el comando pip, reinstale python.

## Dibjar una gráfica de valores X y Y

La gráfica más sencilla es aquella que grafica puntos X y Y, para lograrlo deberemos proporcionar la lista de valores en X y la lista de valores en Y. Luego mediante la función `plot` podremos graficar y mostrar la gráfica. Ejecuta el siguiente código y analizalo:

~~~py
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])

plt.show()
~~~

## Ajustar el color y tipo de la gráfica

Podemos especificar el color de gráfica mediante la primer letra del color en inglés y el tipo de gráfica mediante un caracter, por ejemplo, `r*` muestra asteríscos de color rojo, `k-` muestra una línea consecutiva de color negro, `b+` muestra símbolos `+` de color azul.

~~~py
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], 'g--')

plt.show()
~~~

## Dibujar varias subgráficas (axis) en una sola gráfica

Podemos establecer varias gráficas en una sola mediante `subplots` indicando cuántas filas y columnas deseamos mostrar. El método `subplots` siempre devuelve la figura y una matriz de `axis`, cada `axis` nos permitirá dibujar una gráfica independiente:

~~~py
import matplotlib.pyplot as plt

fig, axis = plt.subplots(3, 2)

axis[0, 0].plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], 'r+')
axis[0, 1].plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], 'b*')

axis[1, 0].plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], 'g+')
axis[1, 1].plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], 'y*')

axis[2, 0].plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], 'k+')
axis[2, 1].plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], 'r-')

plt.show()
~~~

## Problemas

* Generar `11` valores equidistantes en el intervalo de `[a, b]`. Por ejemplo, si a = 1 y b = 3 el resultado sería [1, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3].

* Generar una lista Y que aplique la función `sen(x)` para cada `x` en la lista anterior.

* Graficar X y Y para las listas anteriores en color rojo punteado `r--`. 

<br><br>
<hr>
<small>
Python Científico - Alan Badillo Salas (badillo.soft@hotmail.com)<br>
Instituto Politécnico Nacional - Centro de Investigación en Cómputo
</small>
