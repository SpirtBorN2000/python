class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calcofmass(self):
        return f"{self._length}м * {self._width}м * 25кг * 5см = {self._length * self._width * 25 * 5 / 1000} тонн"


a = Road(500, 20)
print(a.calcofmass())
