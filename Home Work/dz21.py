class Car:
    def __init__(self, model, year, manufacturer, power, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.power = power
        self.color = color
        self.price = price

    def display_info(self):
        print(" Данные автомобиля ".center(40, "*"))
        print(f"Название модели: {self.model}")
        print(f"Год выпуска: {self.year}")
        print(f"Производитель: {self.manufacturer}")
        print(f"Мощность двигателя: {self.power} лс")
        print(f"Цвет машины: {self.color}")
        print(f"Цена: {self.price} руб.")
        print("=" * 40)

    def set_model(self, model):
        self.model = model

    def get_model(self):
        return self.model

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def get_manufacturer(self):
        return self.manufacturer

    def set_power(self, power):
        self.power = power

    def get_power(self):
        return self.power

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price


g1 = Car("Экскаватор", "1976", "MAN", "19646000", "whity", "7600")
g1.set_color("black")
g1.display_info()
print(g1.get_price())