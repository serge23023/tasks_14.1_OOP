import pytest

if __name__ == '__main__':
    pytest.main()


def test_smartphone(smartphone_test):
    assert smartphone_test.performance == "Флагман"
    assert smartphone_test.model == "C23 Ultra"
    assert smartphone_test.memory == "256GB"
    assert smartphone_test.color == "Серый"
