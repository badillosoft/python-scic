n = 20

fi2 = 1 # f(i - 2)
fi1 = 1 # f(i - 1)

print("f(0) = 1")
print("f(1) = 1")

f = [1, 1]

for i in range(2, n + 1):
    fi = fi1 + fi2

    f.append(fi)

    print("f({}) = {}".format(i, fi))

    fi2 = fi1
    fi1 = fi

print(f)