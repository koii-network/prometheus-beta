import pytest
from src.is_sorted import is_sorted

def test_empty_list():
    assert is_sorted([]) == True

def test_single_element_list():
    assert is_sorted([42]) == True

def test_sorted_list_integers():
    assert is_sorted([1, 2, 3, 4, 5]) == True

def test_sorted_list_with_duplicates():
    assert is_sorted([1, 2, 2, 3, 4]) == True

def test_unsorted_list_integers():
    assert is_sorted([5, 4, 3, 2, 1]) == False
    assert is_sorted([1, 3, 2, 4, 5]) == False

def test_sorted_list_strings():
    assert is_sorted(['a', 'b', 'c']) == True

def test_unsorted_list_strings():
    assert is_sorted(['c', 'a', 'b']) == False

def test_invalid_input_type():
    with pytest.raises(TypeError):
        is_sorted("not a list")
    with pytest.raises(TypeError):
        is_sorted(123)

def test_incomparable_elements():
    with pytest.raises(TypeError):
        is_sorted([1, 'a', 2])  # Mixed types that can't be compared