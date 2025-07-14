import os
from parsers import Parser
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s')

logger = logging.getLogger(__name__)


def main():
    path = 'news.txt'
    if os.path.exists(path):
        logger.warning("Существующий файл будет удалён!")
        os.remove(path)

    for i in range(2, 958):
        logger.info(f"Парсинг страницы {i}")
        pars = Parser(f'https://www.ixbt.com/live/index/news/page{i}/', path)
        pars.run()


if __name__ == '__main__':
    main()
