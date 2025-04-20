import requests
from bs4 import BeautifulSoup

base_url = "https://metalarea.org"
group_name = input("Название группы: ").lower()
album_name = input("Название альбома: ").lower()

start_page = f"{base_url}/forum/index.php?showforum=6"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

try:
    response = requests.get(start_page, headers=headers, timeout=30)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    # Ищем все ссылки <a> на странице
    topic_links = soup.find_all("a", href=True)

    print("\nТемы, где может быть альбом:")
    found_links = []

    # Обрабатываем каждую ссылку
    for link in topic_links:
        href = link["href"]
        text = link.text.lower()

        # Ищем совпадения по группе и альбому в тексте ссылки
        if group_name in text and album_name in text and "showtopic=" in href:
            full_link = href if href.startswith("http") else base_url + "/" + href.lstrip("/")
            print(full_link)
            found_links.append(full_link)

except requests.exceptions.RequestException as e:
    print(f"Ошибка при подключении: {e}")
