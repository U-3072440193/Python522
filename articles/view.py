def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f"{title}".center(50, "="))
            output = func(*args, **kwargs)
            print("=" * 50)
            return output

        return wrap

    return wrapper


class UserInterface:
    @add_title("Ввод польз данных")
    def wait_user_answer(self):
        # print("Ввод пользовательских данных".center(50, "="))
        print("Действия со статьями")
        print("1 - создание статьи"
              "\n3 - просмотр опр статьи"
              "\n2 - просмотр статьи"
              "\nq = выход из проги")
        user_answer = input('Выберите вариант действия ')
        # print("=" * 50)
        return user_answer

    @add_title("Название статьи")
    def add_user_article(self):
        dict_article = {
            "название": None,
            "автор": None,
            "колич страниц": None,
            "описание": None
        }
        # print("Создание статьи".center(50, "="))
        for key in dict_article:
            dict_article[key] = input(f"Введите {key} статьи: ")
        # print("=" * 50)
        return dict_article

    @add_title("Показать")
    def shaw_all_articles(self, articles):
        # print("Список статей".center(50, "="))
        for ind, article in enumerate(articles, 1):
            print(f" {ind} {article}")
        # print("=" * 50)

    @add_title("Ввод названия статьи")
    def get_user_article(self):
        user_article = input("Введи назв статьи ")
        return user_article

    def get_single_article(self, user_title):
        article = self.articles[user_title]
