import json

personas = json.load(open("estudio.json", "r"))

# Contar cuantas personas son hombres
H = len(list(filter(lambda p: p["sexo"] == "H", personas)))
# Contar cuantas personas son mujeres
M = len(list(filter(lambda p: p["sexo"] == "M", personas)))
# Contar cuantas personas son discapacitados
DI = len(list(filter(lambda p: p["discapacitado"], personas)))
# Contar cuantas personas son desempleados
DE = len(list(filter(lambda p: p["desempleado"], personas)))
# Contar cuantas personas son discapacitados y desempleados
DIDE = len(list(filter(lambda p: p["discapacitado"] and p["desempleado"], personas)))

print ("Hay {} hombres y {} mujeres".format(H, M))
print ("Hay {} discapacitados".format(DI))
print ("Hay {} desempleados".format(DE))
print ("Hay {} discapacitados y desempleados".format(DIDE))
