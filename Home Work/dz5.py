print("Домашнее задание")
a = [int(input("Введите значение ")) for i in range(int(input("введите количество ")))]
print(a)
num = 0
for x in a:
    if x < 0:
        num += x
print(num)
