import pytest

from src.read_file import open_json


def test_open_json():
    # Проверка, что функция open_json возвращает список
    assert type(open_json('products.json')) is list
    with pytest.raises(TypeError):
        open_json('')
