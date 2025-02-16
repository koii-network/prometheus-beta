import pytest
from src.list_sorting_checker import is_sorted

def test_sorted_ascending_integers():
    assert is_sorted([1, 2, 3, 4, 5]) == True

def test_sorted_descending_integers():
    assert is_sorted([5, 4, 3, 2, 1], ascending=False) == True

def test_unsorted_integers():
    assert is_sorted([1, 3, 2, 4, 5]) == False

def test_empty_list():
    assert is_sorted([]) == True

def test_single_element_list():
    assert is_sorted([42]) == True

def test_list_with_duplicates_ascending():
    assert is_sorted([1, 2, 2, 3, 4]) == True

def test_list_with_duplicates_descending():
    assert is_sorted([5, 4, 4, 3, 2], ascending=False) == True

def test_invalid_input_type():
    with pytest.raises(TypeError):
        is_sorted("not a list")

def test_list_with_mixed_types():
    assert is_sorted([1, 2, 3.14, 4]) == True
    assert is_sorted(['a', 'b', 'c']) == True