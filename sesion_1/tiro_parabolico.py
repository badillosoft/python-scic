xo = 10
yo = 20

vox = 20
voy = 15

g = 9.81

for i in range(0, 31):
    t = i / 10
    x = vox * t + xo
    y = -g * t ** 2 / 2 + voy * t + yo

    f = "{:.2f} {:.2f} {:.2f}".format(t, x, y)

    print(f)