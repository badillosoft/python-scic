import random

puntos = []

for i in range(1000):
    p = {
        "x": random.uniform(-10, 10),
        "y": random.uniform(-10, 10),
    }
    puntos.append(p)

A = []

for p in puntos:
    d = ((p["x"] - 1) ** 2 + (p["y"] - 2) ** 2) ** 0.5
    
    if d < 2:
        A.append(p)

B = []

for p in puntos:
    if p["x"] < 0:
        B.append(p)

C = []

for p in puntos:
    q = {
        "x": p["y"],
        "y": p["x"]
    }

    C.append(q)
