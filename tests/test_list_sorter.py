import pytest
from src.list_sorter import is_sorted

def test_empty_list_ascending():
    assert is_sorted([]) == True

def test_single_element_list_ascending():
    assert is_sorted([42]) == True

def test_sorted_list_ascending():
    assert is_sorted([1, 2, 3, 4, 5]) == True

def test_unsorted_list_ascending():
    assert is_sorted([1, 3, 2, 4, 5]) == False

def test_sorted_list_descending():
    assert is_sorted([5, 4, 3, 2, 1], ascending=False) == True

def test_unsorted_list_descending():
    assert is_sorted([5, 3, 4, 2, 1], ascending=False) == False

def test_list_with_duplicates_ascending():
    assert is_sorted([1, 2, 2, 3, 3, 4]) == True

def test_list_with_duplicates_descending():
    assert is_sorted([4, 3, 3, 2, 2, 1], ascending=False) == True

def test_non_numeric_sorted_list():
    assert is_sorted(['a', 'b', 'c']) == True
    assert is_sorted(['c', 'b', 'a'], ascending=False) == True

def test_mixed_type_list_raises_error():
    with pytest.raises(TypeError):
        is_sorted([1, 'a', 2])

def test_non_list_input_raises_error():
    with pytest.raises(TypeError):
        is_sorted("not a list")
    with pytest.raises(TypeError):
        is_sorted(123)