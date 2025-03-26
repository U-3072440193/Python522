print('Домашнее задание')


def decor(func):
    def wrapper(*args):
        average = func(*args) / len(args)
        print('Среднее арифметическое =', average)
        return average

    return wrapper


@decor
def calculate_summ(*args):
    total = sum(args)
    print('Сумма всех элементов =', total)
    return total


calculate_summ(2, 3, 3, 4)
