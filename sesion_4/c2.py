from sklearn.neural_network import MLPClassifier

X = [
    [1, 1, 8, 1], # 1
    [2, 2, 8, 2], # 2
    [2, 3, 10, 2], # 3
    [2, 1, 8, 2], # 2
    [2, 1, 8, 2] # 4
]

Y = [ 
    1,
    2, 
    3,
    2, 
    4
]

clf = MLPClassifier()

clf.fit(X, Y)

R = clf.predict([[2, 1, 8, 1]])

print(R)