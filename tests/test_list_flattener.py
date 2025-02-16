import pytest
from src.list_flattener import flatten_nested_list

def test_flatten_simple_list():
    assert flatten_nested_list([1, 2, 3]) == [1, 2, 3]

def test_flatten_nested_list():
    assert flatten_nested_list([1, [2, 3], 4]) == [1, 2, 3, 4]

def test_flatten_deeply_nested_list():
    assert flatten_nested_list([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]

def test_flatten_empty_list():
    assert flatten_nested_list([]) == []

def test_flatten_complex_nested_list():
    assert flatten_nested_list([1, [2, 3, [4, 5]], [6, 7], 8]) == [1, 2, 3, 4, 5, 6, 7, 8]

def test_flatten_non_list_raises_error():
    with pytest.raises(TypeError):
        flatten_nested_list(123)
    
    with pytest.raises(TypeError):
        flatten_nested_list("not a list")