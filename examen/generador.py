nombres_h = [
    "Andres", "Beto", "Carlos", "Daniel", "Eduardo", "Franco", "Gerardo",
    "Hugo", "Ivan", "Juan", "Kevin", "Luis", "Mauricio", "Nacho", "Oscar",
    "Pablo", "Raul", "Saul", "Teo", "Ulises"
]

nombres_m = [
    "Ana", "Bety", "Carmen", "Diana", "Edna", "Franca", "Gaby",
    "Hilda", "Ilse", "Juana", "Karen", "Lucha", "Maria", "Nancy", "Olga",
    "Paty", "Rachel", "Sandy", "Tania", "Ursula"
]

apellidos = [
    "Godinez", "Gomez", "Sanchez", "Camacho", "Rodriguez", "Martinez",
    "Perez", "Lopez", "Villareal", "Hernandez", "Gutierrez", "Guevara"
]

import random

personas = []

for i in range(200):
    persona = {}

    apellido = random.choice(apellidos)
    
    if random.randint(1, 100) % 2 == 0:
        nombre = random.choice(nombres_h)
        persona["nombre"] = "{} {}".format(nombre, apellido)
        persona["sexo"] = "H"
    else:
        nombre = random.choice(nombres_m)
        persona["nombre"] = "{} {}".format(nombre, apellido)
        persona["sexo"] = "M"

    persona["edad"] = random.randint(18, 80)
    persona["salario"] = random.randint(2500, 30000)

    if random.randint(1, 100) <= 13:
        persona["discapacitado"] = True
    else:
        persona["discapacitado"] = False

    if random.randint(1, 100) <= 30:
        persona["desempleado"] = True
    else:
        persona["desempleado"] = False

    personas.append(persona)
        
import json

json.dump(personas, open("estudio.json", "w"))