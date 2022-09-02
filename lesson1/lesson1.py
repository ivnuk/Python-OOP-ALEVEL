import math
import os
import datetime
from lesson3.lesson3_blank_lines import SOME_CONSTANT


class GeometricFigure:
    name = 'Rectangly'

    def __init__(self, width: int, height: int = None) -> None:
        self.width = width
        self.height = height
        if height is None:
            self.height = width
        self.precalculated_area = self.area()
        self.inner_circle = Circle()

    def diagonal(self) -> int:
        print(self.width)
        return 0

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def extend_width(self, size) -> None:
        self.width += size

    def zoom(self, times):
        self.width *= times
        self.height *= times


class Circle:
    pi = math.pi


class Auto:
    def move(self):
        pass

    def stop(self):
        pass

    def start_engine(self):
        pass


class ElectroCar(Auto):
    def move(self):
        """
        moving like electrocar
        :return:
        """


class Triangle:
    pass


# class Element:
#     def __init__(...):
#         pass
#
#     def check_agg_state(self, t, s='C') -> str:  # solid / liquid / vapour
#         pass
#
#     def convert(self, t, s) -> int:  # celsium

# aluminium = Element(660, 2470)

# aluminium.check_agg_state(1200) -> liquid
# aluminium.check_agg_state(18) -> solid
# aluminium.check_agg_state(18000) -> vapour

# chlorine = Element()

if __name__ == '__main__':
    some_string = "blahblah"
    rectangle = GeometricFigure(width=1, height=15)
    rectangle1 = GeometricFigure(12)
    rectangle2 = GeometricFigure(51, 250)
    print("W:", rectangle.width)
    print("H:", rectangle.height)
    GeometricFigure.name = "Not sure if its rectangly"
    # rectangle.width = 12
    # rectangle.height = 39
    # rectangle2.type = 'sedan'
    # rectangle.perimeter = 4
    # print(rectangle.perimeter)
    rectangle.perimeter()
    rectangle1.perimeter()
    rectangle.area()

    rectangle2.extend_width(15)
    print(rectangle2.width)


