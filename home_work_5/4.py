class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def print_self(self):
        print('Width is:', self.width)
        print('Height is:', self.height)

class Triangle(Shape):
    def area(self):
        return 0.5 * self.width * self.height


class Rectangle(Shape):
    def area(self):
        return self.width * self.height
        


print('площадь треугольника')
Triangle(2, 3).print_self()
print(Triangle(2, 3).area())
print('площадь прямоугольника')
Rectangle(2, 2).print_self()
print(Rectangle(2, 3).area())

