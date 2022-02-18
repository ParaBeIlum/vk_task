import pytest

dicts_for_testing = [({'test1': 1, 'test2': 2}, {1: 'test1', 2: 'test2'}), ({}, {}),
                     ({1: 1, 'test': 'test'}, {1: 1, 'test': 'test'})]


def reverse_elements_dict(dct):
    return {i: j for j, i in dct.items()}


# Позитивный тест
def test_keys_sort(input_dict):
    new_dict = {}
    list_keys = list(input_dict.keys())
    list_keys.sort()
    for i in list_keys:
        new_dict.update({i: input_dict[i]})
    assert new_dict == input_dict


# Негативный тест, не вызывает ошибку
def test_is_not_empty_dict(input_dict):
    try:
        assert input_dict == {}
    except AssertionError:
        pass


# Тест с параметризацией
@pytest.mark.parametrize('dict_input, dict_expected', dicts_for_testing)
def test_reverse_elements(dict_input, dict_expected):
    assert reverse_elements_dict(dict_input) == dict_expected
