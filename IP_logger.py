import requests
from bs4 import BeautifulSoup
import subprocess
import re
import platform

def get_public_ip():
    url = "https://illustrators.ru"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; 64)"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, "html.parser")
        span = soup.find("div", {"class": "ip"})
        if span:
            ip = span.get_text(strip=True)
            print(f"Public IP: {ip}")
            return ip
        else:
            print("IP не найден")
    else:
        print("Ошибка при запросе")

def get_win_ip():
    try:
        res = subprocess.run(['ipconfig'], capture_output=True, text=True)
        if res.returncode == 0:
            out = res.stdout
            ip_pattern = re.compile(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b')  # Исправлено на \d{1,3}
            for line in out.splitlines():
                match = ip_pattern.search(line)
                if match:
                    ip = match.group()
                    return ip
        else:
            print("Ошибка при выполнении ipconfig")
    except Exception as e:
        print(f"Ошибка: {e}")
    return None

def get_ip():
    os_name = platform.system()
    if os_name == "Windows":
        print("Windows IP:", get_win_ip())
    else:
        print("Не поддерживается для данной операционной системы")
        return None

get_ip()
