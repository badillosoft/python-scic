import math

A = 10
j = 1
k = 3
m = 1

def xf(t):
    w = (k / m) ** 0.5
    return A * math.sin(w * t + j)

f = open("resorte.csv", "w")

n = 100
t_min = 0
t_max = 4

for i in range(n):
    t = t_min + (t_max - t_min) / (n - 1) * i
    x = xf(t)
    f.write("{}, {}\n".format(t, x))

f.close()