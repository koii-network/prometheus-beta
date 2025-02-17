import pytest
from src.find_single_non_duplicate import find_single_non_duplicate

def test_single_non_duplicate_at_start():
    arr = [1, 2, 2, 3, 3, 4, 4]
    assert find_single_non_duplicate(arr) == 1

def test_single_non_duplicate_in_middle():
    arr = [1, 1, 2, 3, 3, 4, 4]
    assert find_single_non_duplicate(arr) == 2

def test_single_non_duplicate_at_end():
    arr = [1, 1, 2, 2, 3, 3, 4]
    assert find_single_non_duplicate(arr) == 4

def test_single_element_array():
    arr = [5]
    assert find_single_non_duplicate(arr) == 5

def test_large_array():
    arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 7, 8, 8]
    assert find_single_non_duplicate(arr) == 6

def test_empty_array_raises_error():
    with pytest.raises(ValueError):
        find_single_non_duplicate([])

def test_none_input_raises_error():
    with pytest.raises(TypeError):
        find_single_non_duplicate(None)

def test_non_list_input_raises_error():
    with pytest.raises(TypeError):
        find_single_non_duplicate("not a list")