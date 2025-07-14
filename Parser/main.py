from pars.fetcher import Parser
from pars.check import Check
import logging



logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] [%(name)s] %(message)s',
    handlers=[
        logging.StreamHandler(),  # вывод в консоль
        # Можно добавить FileHandler для записи в файл, если нужно
    ]
)


def header(title="Выполняется"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("=" * 40)
            print('Введите url,если необходимо парсить несколько страниц, введите 1 ')
            print(f"== {title.upper()} ==")
            print("=" * 40)
            result = func(*args, **kwargs)
            print("=" * 40)
            print("== ГОТОВО ==")
            print("=" * 40)
            return result

        return wrapper

    return decorator


class Interface:
    def __init__(self):
        self.url = ''
        self.tag = ''
        self.pages = 1

    def main(self):
        self.ask()

    @header("Парсинг")
    def ask(self):
        url = input("Введите базовый URL для парсинга (или 1 для нескольких страниц): ").strip()

        if url == '1':
            url_first = input("Введите URL начальной страницы: ").strip()
            url_last_num = input("Введите количество страниц: ").strip()
            while not url_last_num.isdigit():
                print("Введите корректное число.")
                url_last_num = input("Введите количество страниц: ").strip()

            tag = input("Введите тег или CSS-селектор (например, 'div.article'): ").strip()

            self.url = url_first
            self.tag = tag
            self.pages = int(url_last_num)

        else:
            tag = input("Введите тег или CSS-селектор (например, 'div.article'): ").strip()
            self.url = url
            self.tag = tag
            self.pages = 1  # если пользователь ввёл один URL — парсим одну страницу


if __name__ == '__main__':
    interface = Interface()
    interface.main()
