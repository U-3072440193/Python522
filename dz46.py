from bs4 import BeautifulSoup
import requests
import logging
import csv

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s'
)
logger = logging.getLogger(__name__)


class Dz46:
    def __init__(self, url):
        self.url = url
        self.html = None
        self.data = []

    def get_html(self):
        logger.info('Отправляю запрос на получение html-страницы')
        r = requests.get(self.url)
        self.html = r.text
        logger.info(self.html)
        return self.html

    def get_data(self, tag_name, class_name):
        if not self.html:
            logger.error("Ошибка, документ не загружен")
            return

        soup = BeautifulSoup(self.html, 'lxml')
        logger.info(f'начало поиска элементов по имени {tag_name} и классу {class_name}')
        elements = soup.find_all(tag_name, class_=class_name)
        self.data = []
        for el in elements:
            text = el.text.strip()
            logger.info(text)
            self.data.append(text)
        return self.data

    def write(self, filename='data.csv'):
        if not self.data:
            logger.warning("Нет данных для записи")
            return
        try:
            with open(filename, 'a', encoding='utf-8', newline='') as csvfile:
                writer = csv.writer(csvfile)
                for row in self.data:
                    writer.writerow([row])
            logger.info(f"Записано {len(self.data)} строк в файл {filename}")
        except Exception as error:
            logger.error(f"Ошибка при записи в CSV: {error}")


parser = Dz46('https://webref.ru')
parser.get_html()
parser.get_data('div', 'w-category-grid-descr')
parser.write()
aa = Dz46('https://www.wildberries.ru')
aa.get_html()
aa.get_data('div', 'product-card__wrapper')
aa.write()
