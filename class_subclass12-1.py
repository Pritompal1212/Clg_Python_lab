import math

# Base class
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement this method")

# Subclass for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# Subclass for Triangle
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        # Using Heron's formula
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

# Subclass for Square
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

# Example usage
if __name__ == "__main__":
    # Circle
    circle = Circle(5)
    print("Circle: Area =", circle.area(), ", Perimeter =", circle.perimeter())

    # Triangle
    triangle = Triangle(3, 4, 5)
    print("Triangle: Area =", triangle.area(), ", Perimeter =", triangle.perimeter())

    # Square
    square = Square(4)
    print("Square: Area =", square.area(), ", Perimeter =", square.perimeter())
