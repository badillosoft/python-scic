mat = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

f = open("mat2.csv", "w")

def T(x):
    return str(x)

for row in mat:
    srow = map(T, row)
    linea = ", ".join(srow) + "\n"
    f.write(linea)

f.close()

print(":".join(["a", "b", "c"])) # a:b:c
print("-*-".join(["a", "b", "c"])) # a-*-b-*-c