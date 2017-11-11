def T(x):
    if x % 2 == 0:
        return -1
    else:
        return 1

A = [1, 5, 9, 28, 32, 48, 54, 99, 101]

B = map(T, A)