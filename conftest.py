import pytest


@pytest.fixture
def input_str():
    string = 'ABC'
    return string


@pytest.fixture
def input_dict():
    dictionary = {'a': 1,
                  'b': 2,
                  'c': 3}
    return dictionary
