import json
import logging
from random import choice

logger = logging.getLogger("Test_logs for dz30")


def logging_config():
    logging.basicConfig(
        level=logging.DEBUG,
        datefmt='%Y-%m-%d %H:%M:%S',
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )


logging_config()


def gen_person():
    logger.info("Начало генерации данных")
    name1 = ''
    tel = ''

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'k', 'l', 'm', 'n']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name1) != 7:
        name1 += choice(letters)
        logger.info(f"name1 на данный момент: {name1}")
    if len(name1) == 7:
        logger.info(f"Цикл name1 завершен с конечным результатом переменной: {name1}")

    while len(tel) != 10:
        tel += choice(nums)
        logger.info(f"name1 на данный момент: {tel}")
    if len(tel) == 10:
        logger.info(f"Цикл tel завершен с конечным результатом переменной: {tel}")
    for_log = {name1: {'name': name1, 'tel': tel}}
    logger.info(f"Сформирован словарь:{for_log}")
    return {name1: {'name': name1, 'tel': tel}}


def write_json(person_dict, n):
    logger.info(f"Функция write_json вызвана, итерация № {n}")
    try:
        data = json.load(open("persons.json"))
        logger.info(f"Итерация {n}, текущее значение data: {data}")
    except FileNotFoundError:
        logger.error("ФАЙЛ НЕ НАЙДЕН")
        data = {}
    logger.info(f"Обновление данных: {person_dict}")
    data.update(person_dict)
    logger.info(f"ВНИМАНИЕ! Активирована команда записи в файл persons.json!!!!")
    with open('persons.json', 'w') as f:
        json.dump(data, f, indent=2)


for i in range(5):
    write_json(gen_person(), i + 1)
    logger.info(f"Вызов write_json, итерация № {i}")

persons = {}
for i in range(5):
    persons.update(gen_person())
print(persons)
