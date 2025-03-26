print("Домашнее задание")

data_hub = {
    "John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
    "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
    "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
    "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}
}
while True:
    output_name = input("Введите имя: ")
    if output_name == "" or output_name == " ":
        print("Ошибка! Вы ничего не ввели, попробуйте снова.")
        continue
    elif output_name in data_hub:
        break
    else:
        print("Такого имени нет в списках, попробуйте еще раз.")

while True:
    output_region = input("Введите регион: ")
    if output_region == "n":
        output_region = "N"
    elif output_region == "s":
        output_region = "S"
    elif output_region == "e":
        output_region = "E"
    elif output_region == "w":
        output_region = "W"
    if output_region in ["N", "S", "E", "W"]:
        break
    else:
        print("Такого региона не существует, попробуйте еще раз.")
if output_name in data_hub and output_region in data_hub[output_name]:
    while True:
        try:
            new_sales = int(input("Введите новый объем продаж: "))

            if new_sales < 0:
                print("Ошибка! Объем продаж не может быть отрицательным. Попробуйте снова.")
            else:
                break

        except ValueError:
            print("Ошибка! Введите целое число без запятых, точек, букв и прочего.")

    data_hub[output_name][output_region] += new_sales
    print(data_hub[output_name])
