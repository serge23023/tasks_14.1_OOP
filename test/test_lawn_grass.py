import pytest

if __name__ == '__main__':
    pytest.main()


def test_lawn_grass(lawn_grass_test):
    assert lawn_grass_test.country == "USA"
    assert lawn_grass_test.germination_period == "14 дней"
    assert lawn_grass_test.color == "Зеленый"
