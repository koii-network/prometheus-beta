import pytest
from src.list_sorted_checker import is_list_sorted

def test_empty_list():
    assert is_list_sorted([]) == True

def test_single_element_list():
    assert is_list_sorted([42]) == True

def test_sorted_ascending_list():
    assert is_list_sorted([1, 2, 3, 4, 5]) == True

def test_sorted_descending_list():
    assert is_list_sorted([5, 4, 3, 2, 1], reverse=True) == True

def test_unsorted_list_ascending():
    assert is_list_sorted([1, 3, 2, 4, 5]) == False

def test_unsorted_list_descending():
    assert is_list_sorted([5, 3, 4, 2, 1], reverse=True) == False

def test_list_with_duplicates_ascending():
    assert is_list_sorted([1, 2, 2, 3, 4]) == True

def test_list_with_duplicates_descending():
    assert is_list_sorted([5, 4, 4, 3, 2], reverse=True) == True

def test_invalid_input_type():
    with pytest.raises(TypeError):
        is_list_sorted("not a list")

def test_mixed_type_list():
    assert is_list_sorted([1, 2, 3, 'a', 'b']) == True
    assert is_list_sorted(['a', 'b', 'c']) == True