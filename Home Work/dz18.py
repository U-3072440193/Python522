print("Домашнее задание")

with open(r"D:\Python522\dz18.txt", "w") as f:
    f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл\n")

pos1 = int(input("pos1 = "))
pos2 = int(input("pos2 = "))

with open(r"D:\Python522\dz18.txt", "r") as f:
    data = f.readlines()
data[pos1 - 1], data[pos2 - 1] = data[pos2 - 1], data[pos1 - 1]

with open(r"D:\Python522\dz18.txt", "w") as f:
    f.writelines(data)
    