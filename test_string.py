import pytest

strings_for_testing = [('abc', 'ABC'), ('abc', 'abc'), ('', ''), (' ', ' ')]


# Позитивный тест
def test_is_uppercase(input_str):
    assert input_str.isupper()


# Негативный тест, не вызывает ошибку
def test_is_lowercase(input_str):
    try:
        assert input_str.isupper()
    except AssertionError:
        pass


# Тест с параметризацией
@pytest.mark.parametrize('input_str, output_str', strings_for_testing)
def test_is_equal(input_str, output_str):
    try:
        assert input_str.upper() == output_str
    except AssertionError:
        assert input_str == output_str

