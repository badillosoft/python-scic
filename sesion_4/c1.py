# pip install sklearn scipy
from sklearn.tree import DecisionTreeClassifier

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

clf = DecisionTreeClassifier()

clf.fit(X, Y)

R = clf.predict([[2, 1, 8, 1]])

print(R)

from sklearn import tree
import graphviz

dot_data = tree.export_graphviz(clf, out_file=None) 

graph = graphviz.Source(dot_data)

graph.render("frutas")