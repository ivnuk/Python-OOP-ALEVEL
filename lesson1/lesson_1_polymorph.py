import math


class Square:
    width: int = 0

    def area(self):
        return self.width ** 2


class Circle:
    radius: int = 0

    def area(self):
        return math.pi * self.radius ** 2
