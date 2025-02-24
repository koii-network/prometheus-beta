import pytest
from src.max_number import find_max_number

def test_find_max_number_positive_integers():
    assert find_max_number([1, 2, 3, 4, 5]) == 5

def test_find_max_number_negative_integers():
    assert find_max_number([-1, -2, -3, -4, -5]) == -1

def test_find_max_number_mixed_numbers():
    assert find_max_number([-10, 0, 5, 3.14, 2.5]) == 5

def test_find_max_number_single_element():
    assert find_max_number([42]) == 42

def test_find_max_number_all_same_values():
    assert find_max_number([7, 7, 7, 7]) == 7

def test_find_max_number_empty_array_raises_error():
    with pytest.raises(ValueError, match="Cannot find maximum of an empty array"):
        find_max_number([])

def test_find_max_number_non_numeric_array_raises_error():
    with pytest.raises(TypeError, match="Array must contain only numeric elements"):
        find_max_number([1, 2, 'three', 4, 5])

def test_find_max_number_floating_point():
    assert find_max_number([1.1, 2.2, 3.3, 4.4, 5.5]) == 5.5