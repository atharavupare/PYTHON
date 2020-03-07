#!/usr/local/bin/python3.7

import math

class Rectangle:
    def __init__(self, color, filled, length, breadth):
        self.__color = color
        self.__filled = filled
        self.__length = length
        self.__breadth = breadth

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def is_filled(self):
        return self.__filled

    def set_filled(self, filled):
        self.__filled = filled

    def get_length(self):
        return self.__length

    def set_length(self, length):
        self.__length = length

    def get_breadth(self):
        return self.__breadth

    def set_breadth(self, breadth):
        self.__breadth = breadth

    def get_area(self):
        return self.__length * self.__breadth

    def get_perimeter(self):
        return 2 * (self.__length + self.__breadth)

class Circle:
    def __init__(self, color, filled, radius):
        self.__color = color
        self.__filled = filled
        self.__radius = radius

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def is_filled(self):
        return self.__filled

    def set_filled(self, filled):
        self.__filled = filled

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    def get_area(self):
        return math.pi * self.__radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.__radius

if __name__ == '__main__':

    r1 = Rectangle('black', False, 10, 2)

    print("Area of rectangle r1:", r1.get_area())
    print("Perimeter of rectangle r1:", r1.get_perimeter())
    print("Color of rectangle r1:", r1.get_color())
    print("Is rectangle r1 filled ? ", r1.is_filled())
    r1.set_filled(True)
    print("Is rectangle r1 filled ? ", r1.is_filled())
    r1.set_color("orange")
    print("Color of rectangle r1:", r1.get_color())

    c1 = Circle('black', False, 10)

    print("\nArea of circle c1:", format(c1.get_area(), "0.2f")) #THE LAST PART IN THIS LINE IS USED TO DENOTE HOW MANY DECIMAL POINTS TO SHOW, IN THIS CASE IT WILL SHOW 2 DECIMAL POINTS AFTER .
    print("Perimeter of circle c1:", format(c1.get_perimeter(), "0.2f"))
    print("Color of circle c1:", c1.get_color())
    print("Is circle c1 filled ? ", c1.is_filled())
    c1.set_filled(True)
    print("Is circle c1 filled ? ", c1.is_filled())
    c1.set_color("blue")
    print("Color of circle c1:", c1.get_color())
