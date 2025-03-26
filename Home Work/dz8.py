from math import pi, sqrt
print("Домашнее задание")

def triangle_area(fa, fb, fc):
    if fa + fb > fc and fa + fc > fb and fb + fc > fa:
        s = (fa + fb + fc) / 2
        return round(sqrt(s * (s - fa) * (s - fb) * (s - fc)), 2)
    else:
        return "Такой треугольник не существует"


def rectangle_area(fa, fb):
    return round(fa * fb)


def circle_area(fr):
    return round(pi * (fr ** 2))


while True:
    try:
        x = int(input("Выберите фигуру: \n1 - треугольник \n2 - прямоугольник \n3 - круг \n: "))

        if x == 1:
            while True:
                try:
                    a = int(input("Введите сторону а: "))
                    b = int(input("Введите сторону b: "))
                    c = int(input("Введите сторону c: "))

                    if a > 0 and b > 0 and c > 0:
                        if a + b > c and a + c > b and b + c > a:
                            print(": ", triangle_area(a, b, c))
                            break
                        else:
                            print("Такой треугольник не существует, повторите ввод")
                    else:
                        print("Ошибка! Все стороны должны быть положительными числами.")
                except ValueError:
                    print("Ошибка! Некорректный ввод данных. Попробуйте снова.")

        elif x == 2:
            while True:
                try:
                    a = int(input("Введите сторону а: "))
                    b = int(input("Введите сторону b: "))

                    if a > 0 and b > 0:
                        print(": ", rectangle_area(a, b))
                        break
                    else:
                        print("Ошибка! Длины сторон должны быть положительными числами.")
                except ValueError:
                    print("Ошибка! Введите корректные значения. Попробуйте снова.")

        elif x == 3:
            while True:
                try:
                    r = int(input("Введите радиус окружности: "))

                    if r > 0:
                        print(": ", circle_area(r))
                        break
                    else:
                        print("Ошибка! Радиус должен быть положительным числом.")
                except ValueError:
                    print("Ошибка!  Введите корректные значения. Попробуйте снова.")

        else:
            print("Вы ввели некорректные данные, пожалуйста повторите.")
            continue

        break

    except ValueError:
        print("Ошибка! Нужно ввести число 1, 2 или 3.")
