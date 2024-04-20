import json
import os


def open_json(file_name: str) -> list:
    """
    Открывает и загружает JSON-файл.
    """
    with open(find_file(file_name), 'r', encoding='utf-8') as f:
        return json.load(f)


def find_file(filename):
    """
    Поиск файла по наименованию
    :return: Путь до файла
    """
    for root, dirs, files in os.walk(os.path.dirname(os.getcwd())):
        if filename in files:
            return os.path.join(root, filename)
    return None
