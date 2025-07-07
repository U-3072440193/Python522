# f = open('index.html').read()
# soup = BeautifulSoup(f, "html.parser")
# # row = soup.find('div', class_="row")
# # row = soup.find_all('div', class_="row")[2].find('div', class_='name').text
# # row = soup.find_all('div', class_="row")[2].find('div', {'data-set': 'salary'}).text
# # row = soup.find('div', string='Alena').find_parent(class_='row')
# row = soup.find('div', id='whois3').find_previous_sibling()
# print(row)
#
# def get_copywriter(tag):
#     whois = tag.find('div', class_="whois").text
#     if 'copywriter' in whois:
#         return tag
#     return None
#
#
# f = open('index.html').read()
# soup = BeautifulSoup(f, "html.parser")
#
# copywriter = []
# row = soup.find_all("div", class_='row')
# for i in row:
#     cw = get_copywriter(i)
#     if cw:
#         copywriter.append(cw)
#
# print(copywriter)
# r = requests.get('https://ru.wordpress.org/')
# print(r.text)


from bs4 import BeautifulSoup
import requests


def get_html(url):
    r = requests.get(url)
    return r.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    p1 = soup.find_all('section', class_="plugin-section")[2]
    plugins = p1.find_all('li')
    for plugin in plugins:
        name = plugin.find('h3', class_='entry-title').find('a').get('href')
        print(name)


def main():
    url = 'https://ru.wordpress.org/plugins/'
    get_data(get_html(url))


if __name__ == '__main__':
    main()
