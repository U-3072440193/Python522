import re
import requests
import logging

logger = logging.getLogger(__name__)


class Check:
    def __init__(self, url):
        self.url = url

    def check_url(self):
        pattern = re.compile(
            r'^(https?://)'  # http:// или https://
            r'([\w.-]+)'  # домен
            r'(:\d+)?'  # необязательный порт
            r'(/\S*)?$',  # путь
            re.IGNORECASE
        )
        return bool(pattern.match(self.url))

    def check_encoding(self):
        try:
            response = requests.get(self.url, timeout=5)
            content_type = response.headers.get('Content-Type', '')

            # Проверяем, есть ли в Content-Type указание кодировки
            if 'charset=' in content_type.lower():
                charset = content_type.lower().split('charset=')[-1]
                return charset.strip()

            # Если кодировка не указана, попробуем проверить, можно ли декодировать в utf-8
            response.encoding = 'utf-8'  # явно ставим utf-8
            text = response.text  # при обращении может возникнуть исключение, если декодировать нельзя

            return 'utf-8 (принята)'

        except Exception as e:
            return f'Ошибка при проверке кодировки: {e}'
