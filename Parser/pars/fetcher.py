from bs4 import BeautifulSoup
import requests
import logging

logger = logging.getLogger(__name__)


class Parser:
    def __init__(self, url, path):
        self.url = url
        self.path = path
        self.html = None
        self.res = []

    def get_html(self):
        response = requests.get(self.url)
        response.encoding = 'utf-8'  # ставим кодировку у объекта Response
        self.html = BeautifulSoup(response.text, 'lxml')  # парсим текст страницы
