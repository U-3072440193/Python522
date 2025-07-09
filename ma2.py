from bs4 import BeautifulSoup
import requests


class Parser:
    html = ''
    res = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, 'lxml')

    def parsing(self):
        news = self.html.find_all('td', class_='row1')
        for item in news:
            title = item.find('h3', class_='topic-title').text
            href = item.find('a')['href']
            author = item.find('div', class_='desc').text.strip()
            self.res.append({
                'title': title,
                'href': href,
                'author': author
            })
        print(self.res)
