import random

f = open("experimento.csv", "w")

f.write("tiempo,dilatacion,temperatura,densidad\n")

for t in range(0, 10):
    dilatacion = random.uniform(0, 10)
    temperatura = random.uniform(0, 100)
    densidad = random.uniform(0, 10)
    f.write("{},{:.2f},{:.2f},{:.2f}\n".format(t, dilatacion, temperatura, densidad))

f.close()

import scic

datos = scic.load_data_csv("experimento.csv")

print(datos)