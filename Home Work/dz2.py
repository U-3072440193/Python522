print("Домашнее задание 2")
name = int(input("Введите пятизначное число:"))
for_print = name
n5 = name % 10
name //= 10
n4 = name % 10
name //= 10
n3 = name % 10
name //= 10
n2 = name % 10
name //= 10
n1 = name % 10
name //= 10
print(n1, n2, n3, n4, n5, sep="")  # проверка
s = int((n1 + n2 + n3 + n4 + n5) / 5)
print("Среднее арифметическое цифр числа", for_print, "=", s)
x = n1 * n2 * n3 * n4 * n5
print("Произведение цифр числа", for_print, "=", x)
