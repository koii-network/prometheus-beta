import pytest
from src.string_sorter import sort_strings_by_length

def test_sort_strings_by_length_default():
    input_list = ['apple', 'banana', 'cat', 'dog', 'elephant']
    expected = ['cat', 'dog', 'apple', 'banana', 'elephant']
    assert sort_strings_by_length(input_list) == expected

def test_sort_strings_by_length_reverse():
    input_list = ['apple', 'banana', 'cat', 'dog', 'elephant']
    expected = ['elephant', 'banana', 'apple', 'cat', 'dog']
    assert sort_strings_by_length(input_list, reverse=True) == expected

def test_sort_strings_by_length_empty_list():
    assert sort_strings_by_length([]) == []

def test_sort_strings_by_length_invalid_input():
    with pytest.raises(TypeError):
        sort_strings_by_length("not a list")
    with pytest.raises(TypeError):
        sort_strings_by_length(123)