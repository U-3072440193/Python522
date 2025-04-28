from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, length, h, color):
        self.length = length
        self.height = h
        self.color = color

    @abstractmethod
    def get_shape_name(self):
        pass

    @abstractmethod
    def area(self):
        ...

    @abstractmethod
    def perimetr(self):
        ...

    @abstractmethod
    def draw_figure(self):
        ...

    def print_info(self):
        shape_name = self.get_shape_name()
        print(shape_name.center(40, "="))
        print(
            f"Длинна: {self.length} \nШирина: {self.height} \nЦвет: {self.color} "
            f"\nПлощадь: {self.area()} \nПериметр: {round(self.perimetr(), 2)}")
        self.draw_figure()
        print()


class Square(Shape):
    def __init__(self, length, color):
        super().__init__(length, length, color)

    def area(self):
        return self.length ** 2

    def perimetr(self):
        return self.length * 4

    def draw_figure(self):
        for _ in range(self.length):
            print("*" * self.length)

    def get_shape_name(self):
        return "Квадрат"


class Rectangle(Shape):
    def __init__(self, length, height, color):
        super().__init__(length, height, color)

    def area(self):
        return self.length * self.height

    def perimetr(self):
        return 2 * (self.length + self.height)

    def draw_figure(self):
        for i in range(self.height):
            print("*" * self.length)

    def get_shape_name(self):
        return "Прямоугольник"


class Triangle(Shape):

    def __init__(self, length, height, color):
        super().__init__(length, height, color)

    def area(self):
        return 0.5 * self.length * self.height

    def perimetr(self):
        side = (self.length ** 2 + self.height ** 2) ** 0.5
        return self.length + 2 * side

    def draw_figure(self):
        for i in range(1, self.height + 1):
            print(" " * (self.height - i) + "*" * (2 * i - 1))

    def get_shape_name(self):
        return "Треугольник"


c = Square(5, "черный")
c.print_info()

d = Rectangle(5, 8, "синий")
d.print_info()

e = Triangle(8, 9, "gray")
e.print_info()
