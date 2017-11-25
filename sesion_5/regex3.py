import re

text = """
Nombre: Analisis Levadura
Resultados:
* PH: 27%
* TEMPERATURA: 120.3C
* DILATACION: 5u
"""

pattern = "[\*\s]+(\w+)[\:\s]+([\d\.]+)"

experimento = {}

for m in re.finditer(pattern, text):
    print("{} {}".format(m.group(1), m.group(2)))
    k = m.group(1)
    v = float(m.group(2))
    experimento[k] = v

print(experimento)

print(experimento["DILATACION"] ** 2)