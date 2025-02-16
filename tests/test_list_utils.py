import pytest
from src.list_utils import flatten_nested_list

def test_flatten_simple_list():
    input_list = [1, 2, 3]
    assert flatten_nested_list(input_list) == [1, 2, 3]

def test_flatten_nested_list():
    input_list = [1, [2, 3], 4]
    assert flatten_nested_list(input_list) == [1, 2, 3, 4]

def test_flatten_deeply_nested_list():
    input_list = [1, [2, [3, 4]], 5, [6, [7, 8]]]
    assert flatten_nested_list(input_list) == [1, 2, 3, 4, 5, 6, 7, 8]

def test_flatten_empty_list():
    input_list = []
    assert flatten_nested_list(input_list) == []

def test_flatten_list_with_mixed_types():
    input_list = [1, 'a', [2, 'b'], [3, [4, 'c']]]
    assert flatten_nested_list(input_list) == [1, 'a', 2, 'b', 3, 4, 'c']

def test_flatten_invalid_input():
    with pytest.raises(TypeError):
        flatten_nested_list("not a list")
    with pytest.raises(TypeError):
        flatten_nested_list(123)