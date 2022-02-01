from iris import Iris

class Centroid:
    def __init__(self, iris: Iris, positionInitial: list) -> None:
        self._iris = iris
        self._position = positionInitial
    
    def __str__(self):
        return f'Iris: {self._iris}, Position: {self._position}'

    @property
    def iris(self):
        return self._iris

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value
