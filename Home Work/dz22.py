print("Домашнее задание")


class PoundsConverter:
    def __init__(self):
        self.__kgs = 0

    @staticmethod
    def __check_value(x):
        if isinstance(x, int) or isinstance(x, float):
            return True
        return False

    @property
    def pounds(self):
        return f"{self.__kgs}кг => {self.__kgs * 2.205} фунтов"

    @pounds.setter
    def pounds(self, value):
        if PoundsConverter.__check_value(value):
            self.__kgs = value
        else:
            print("Должны быть введены только числовые значения")

    # pounds = property(__get_pounds, __set_data)


p1 = PoundsConverter()
p1.pounds = 12
print(p1.pounds)

p2 = PoundsConverter()
p2.pounds = 41
print(p2.pounds)

p3 = PoundsConverter()
p3.pounds = "abcx"
