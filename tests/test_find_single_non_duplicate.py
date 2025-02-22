import pytest
from src.find_single_non_duplicate import find_single_non_duplicate

def test_basic_cases():
    assert find_single_non_duplicate([1, 1, 2, 3, 3]) == 2
    assert find_single_non_duplicate([1, 1, 2, 2, 3, 4, 4]) == 3

def test_single_element():
    assert find_single_non_duplicate([5]) == 5

def test_first_element_unique():
    assert find_single_non_duplicate([1, 2, 2, 3, 3]) == 1

def test_last_element_unique():
    assert find_single_non_duplicate([1, 1, 2, 2, 3]) == 3

def test_large_array():
    assert find_single_non_duplicate([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 7]) == 6

def test_error_handling():
    with pytest.raises(TypeError):
        find_single_non_duplicate(None)
    
    with pytest.raises(TypeError):
        find_single_non_duplicate("not a list")
    
    with pytest.raises(ValueError):
        find_single_non_duplicate([])