"""
    Homework 4: Exercise 2
    Name: Nick Waggoner
    Date: 10-24-2021
    Description: The program uses inheritance for the Square, Circle, and Rectangle classes, which all
        implement the abstract methods defined in the parent Shape class. Each class is capable of computing
        the shape's area, perimeter, and diagonal (diameter for the circle).
"""
import math


class Shape:

    # sets up the following classes as abstract classes to be inherited and overridden.
    def area(self):
        pass

    def diagonal(self):
        pass

    def perimeter(self):
        pass

    def toString(self):
        pass


class Rectangle(Shape):
    length = 0
    width = 0

    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return self.length * self.width

    def diagonal(self):
        return math.sqrt(pow(self.length, 2) + pow(self.width, 2))

    def perimeter(self):
        return 2 * (self.length + self.width)

    def toString(self):
        print("The rectangle's information:")
        print("Length: " + str(self.length) + " Width: " + str(self.width))
        print("Area: " + str(self.area()) + " Diagonal: " + str(self.diagonal()) + " Perimeter: " + str(self.perimeter()) + "\n")


class Circle(Shape):
    radius = 0

    def __init__(self, r):
        self.radius = r

    def area(self):
        return math.pi * pow(self.radius, 2)

    def diagonal(self):
        # This returns the diameter of the circle
        return 2 * self.radius

    def perimeter(self):
        return 2 * self.radius * math.pi

    def toString(self):
        print("The cirlce's information:")
        print("Radius: " + str(self.radius))
        print(
            "Area: " + str(self.area()) + " Diameter: " + str(self.diagonal()) + " Perimeter: " + str(self.perimeter())+ "\n")


class Square(Shape):
    sLength = 0

    def __init__(self, sl):
        self.sLength = sl

    def area(self):
        return math.sqrt(pow(self.sLength, 2))

    def diagonal(self):
        return math.sqrt(pow(self.sLength, 2) * 2)

    def perimeter(self):
        return self.sLength * 4

    def toString(self):
        print("The square's information:")
        print("Side Length: " + str(self.sLength))
        print(
            "Area: " + str(self.area()) + " Diagonal: " + str(self.diagonal()) + " Perimeter: " + str(self.perimeter())+ "\n")


# Driver code
rect = Rectangle(20, 10)
circle = Circle(int(rect.diagonal() / 2))
rect.toString()
circle.toString()
