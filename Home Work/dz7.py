from math import pi, sqrt

while True:
    try:
        x = int(input("Выберите фигуру: \n1 - треугольник \n2 - прямоугольник \n3 - круг \n: "))

        if x == 1:
            while True:
                try:
                    a = int(input("Введите сторону а: "))
                    b = int(input("Введите сторону b: "))
                    c = int(input("Введите сторону c: "))


                    def triangle_area(a, b, c):
                        if a + b > c and a + c > b and b + c > a:
                            s = (a + b + c) / 2
                            return round(sqrt(s * (s - a) * (s - b) * (s - c)), 2)
                        else:
                            return "Такой треугольник не существует"

                    if a + b > c and a + c > b and b + c > a:
                        print(": ", triangle_area(a, b, c))
                        break
                    else:
                        print("Такой треугольник не существует, повторите ввод")
                except ValueError:
                    print("Ошибка! Нужно вводить только положительные числа. Попробуйте снова.")

        elif x == 2:
            while True:
                try:
                    a = int(input("Введите сторону а: "))
                    b = int(input("Введите сторону b: "))


                    def rectangle_area(a, b):
                        return round(a * b)

                    print(": ", rectangle_area(a, b))
                    break
                except ValueError:
                    print("Ошибка! Нужно вводить только положительные числа. Попробуйте снова.")

        elif x == 3:
            while True:
                try:
                    a = int(input("Введите радиус окружности: "))


                    def circle_area(r):
                        return round(pi * (r ** 2))


                    print(": ", circle_area(a))
                    break
                except ValueError:
                    print("Ошибка! Нужно вводить только положительные числа. Попробуйте снова.")

        else:
            print("Вы ввели некорректные данные, пожалуйста повторите.")
            continue

        break

    except ValueError:
        print("Ошибка! Нужно ввести число 1, 2 или 3.")
