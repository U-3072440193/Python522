import json


class Country:
    def __init__(self):
        self.data = {}

    @staticmethod
    def info():
        print("*" * 22 + "\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных\n"
                         "4 - редактирование данных\n5 - просмотр данных\n6 - завершение работы\n" + "*" * 22)

    def add_country(self, countr, cap):
        self.data[countr] = cap

    def write_json(self):
        try:
            with open('country_dict.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {}

        data.update(self.data)

        with open('country_dict.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def delete_country(self, key):
        try:
            with open('country_dict.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            print("Файл не найден.")

        if key in data:
            del data[key]
            self.data = data
            with open('country_dict.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"Страна {key} удалена.")
        else:
            print(f"Страна {key} не найдена.")

    def edit_country(self, countr, cap):
        self.load_json()
        self.data[countr] = cap

    def print_file_data(self):
        try:
            with open('country_dict.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                for x, y in data.items():
                    print(f"{x}: {y}")
        except FileNotFoundError:
            print("Файл с данными не найден.")

    def load_json(self):
        try:
            with open('country_dict.json', 'r', encoding='utf-8') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            print("Файл с данными не найден. Начинаем с пустого.")

    def search_country(self, x):
        try:
            with open('country_dict.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
            if x in data:
                print(f"Найденные данные для {x}: {data[x]}")
            else:
                print("Такой страны нет в файле")
        except FileNotFoundError:
            print("Файл с данными не найден.")


obj = Country()

Country.info()
while True:
    try:
        num = int(input("Ввод: "))
        if num not in [1, 2, 3, 4, 5, 6]:
            raise ValueError("Недопустимый номер команды")
        elif num == 6:
            print("Завершение работы")
            break
        elif num == 1:
            country = input("Введите название страны(с заглавной буквы): ")
            capital = input("Введите название столицы(с заглавной буквы): ")
            obj.add_country(country, capital)
            obj.write_json()
        elif num == 2:
            obj.load_json()
            country = input("Введите название страны(с заглавной буквы): ")
            obj.delete_country(country)
            obj.write_json()
        elif num == 3:
            country = input("Введите название страны(с заглавной буквы): ")
            obj.search_country(country)
        elif num == 4:
            country = input("Введите название страны(с заглавной буквы): ")
            capital = input("Введите название столицы(с заглавной буквы): ")
            obj.edit_country(country, capital)
            obj.write_json()
        elif num == 5:
            obj.print_file_data()
    except ValueError:
        print("Ошибка ввода")
