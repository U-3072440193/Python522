from math import pi

print("Домашнее задание")
res = {
    "circle": (lambda r: 2 * pi * r)(2),
    "rectangle": (lambda a, b: a * b)(10, 13),
    "trapezoid": (lambda a, b, h: 0.5 * (a + b) * h)(7, 5, 3)
}

print("Площади фигур", res)
