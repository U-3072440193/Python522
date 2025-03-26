import re
print("Домашнее задание")

text = str(input('Введите дату в формате дд-мм-гггг:'))
pattern = r'(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19[0-9]{2}|20[0-2][0-9])'

dates = re.findall(pattern, text)
print(dates)
