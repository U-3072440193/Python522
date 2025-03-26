print("Домашнее задание")

a = 10
b = 2
print(id(a))
print(id(b))
a = b
print(id(a))
b = a * 5
print(id(b))
print("a:", a)
print("b:", b)
a, b = b, a  # этот вариант мне подсказали
print("a:", a)
print("b:", b)