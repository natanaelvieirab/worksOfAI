from enum import Enum

class Iris(Enum):
    Setosa = 0
    Versicolour = 1
    Virginica = 2

dict_iris = dict()
dict_iris[Iris.Setosa] = 'Iris-setosa'
dict_iris[Iris.Versicolour] = 'Iris-versicolor'
dict_iris[Iris.Virginica] = 'Iris-Virginica'
