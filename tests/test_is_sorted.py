import pytest
from src.is_sorted import is_sorted

def test_empty_list():
    assert is_sorted([]) == True

def test_single_element_list():
    assert is_sorted([42]) == True

def test_ascending_sorted_list():
    assert is_sorted([1, 2, 3, 4, 5]) == True

def test_descending_sorted_list():
    assert is_sorted([5, 4, 3, 2, 1], ascending=False) == True

def test_unsorted_list_ascending():
    assert is_sorted([1, 3, 2, 4, 5]) == False

def test_unsorted_list_descending():
    assert is_sorted([5, 3, 4, 2, 1], ascending=False) == False

def test_list_with_duplicates_ascending():
    assert is_sorted([1, 2, 2, 3, 4]) == True

def test_list_with_duplicates_descending():
    assert is_sorted([5, 4, 4, 3, 2], ascending=False) == True

def test_invalid_input_type():
    with pytest.raises(TypeError):
        is_sorted("not a list")
    with pytest.raises(TypeError):
        is_sorted(123)
    with pytest.raises(TypeError):
        is_sorted(None)