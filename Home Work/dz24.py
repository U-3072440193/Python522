from math import sqrt


class Pair:
    def __init__(self, a, b):
        if isinstance(a, str) or isinstance(b, str):
            raise ValueError("Оба параметра должны быть числами.")
        elif a <= 0 or b <= 0:
            raise ValueError("Оба параметра должны быть не нулевыми и положительными.")
        else:
            self.__a = a
            self.__b = b

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    @a.setter
    def a(self, a):
        if a <= 0 or isinstance(a, str):
            raise ValueError("Значение a должно быть положительным и не строкой.")
        self.__a = a

    @b.setter
    def b(self, b):
        if b <= 0 or isinstance(b, str):
            raise ValueError("Значение b должно быть положительным и не строкой.")
        self.__b = b

    def calculate_sum(self):
        return f"Сумма : {self.__a + self.__b}"

    def calculate_ab(self):
        return f"Произведение : {self.__a * self.__b}"


class RightTriangle(Pair):
    def __init__(self, a, b):
        super().__init__(a, b)

    def calc_hypotenuse(self):
        return round(sqrt(self.a ** 2 + self.b ** 2), 2)

    def get_hypotenuse(self):
        return f"Гипотенуза треугольника АВС : {self.calc_hypotenuse()}"

    def area(self):
        return f"Площадь треугольника АВС : {round((self.a * self.b) / 2, 2)}"

    def triangle_info(self):
        return f"Прямоугольный треугольник АВС {self.a, self.b, self.calc_hypotenuse()}"


c1 = RightTriangle(2, 3)
print(c1.get_hypotenuse())
print(c1.triangle_info())
print(c1.area())
print(c1.calculate_sum())
print(c1.calculate_ab())

c2 = RightTriangle(15, 20)
print(c2.get_hypotenuse())
print(c2.triangle_info())
print(c2.area())
print(c2.calculate_sum())
print(c2.calculate_ab())

c2.a = 7
print(c2.triangle_info())
