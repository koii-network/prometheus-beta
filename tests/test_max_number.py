import pytest
from src.max_number import find_max_number

def test_find_max_number_positive_numbers():
    assert find_max_number([1, 2, 3, 4, 5]) == 5

def test_find_max_number_negative_numbers():
    assert find_max_number([-1, -2, -3, -4, -5]) == -1

def test_find_max_number_mixed_numbers():
    assert find_max_number([-10, 0, 5, 3, -5]) == 5

def test_find_max_number_float_numbers():
    assert find_max_number([1.5, 2.7, 0.3, 4.1]) == 4.1

def test_find_max_number_single_element():
    assert find_max_number([42]) == 42

def test_find_max_empty_list():
    with pytest.raises(ValueError, match="Cannot find maximum of an empty list"):
        find_max_number([])

def test_find_max_non_list_input():
    with pytest.raises(TypeError, match="Input must be a list"):
        find_max_number("not a list")

def test_find_max_non_numeric_elements():
    with pytest.raises(TypeError, match="All elements must be numeric"):
        find_max_number([1, 2, "three", 4])