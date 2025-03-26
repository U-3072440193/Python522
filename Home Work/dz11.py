num = int(input("Введите количество студентов "))
data_base = {}
for ind, n in enumerate(range(num), 1):
    print(ind, end="")
    key = str(input("-й студент, имя "))
    while True:
        try:
            value = int(input("Введите балл: "))
            if value < 0:
                print("Балл не может быть отрицательным")
                continue
            elif value == 0:
                print("Студент отправлен на пересдачу")
                break
            break
        except ValueError:
            print("Ошибка! Введите целое число.")
    data_base[key] = value
print("\nСписок студентов с баллами:", data_base)
counter = 0
average = 0
for i in data_base:
    if data_base[i] > counter:
        counter = data_base[i]
    average += data_base[i]
average /= num
print("Средний балл = ", average)
for key, value in data_base.items():
    if value == counter:
        print("Студенты с наивысшим баллом: ", key)
above_average = []
for key, value in data_base.items():
    if value > average:
        above_average.append(key)

print("Студенты с баллом выше среднего:", end=" ")
for i in range(len(above_average)):
    if i == len(above_average) - 1:
        print(above_average[i])
    else:
        print(above_average[i], end=", ")
