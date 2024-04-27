import pytest

from src.read_file import open_json

if __name__ == '__main__':
    pytest.main()


def test_open_json():
    # Проверка, что функция open_json возвращает список
    assert isinstance(open_json('products.json'), list)

    # Проверка, что функция open_json вызывает исключение при пустой строке
    with pytest.raises(TypeError):
        open_json('')
