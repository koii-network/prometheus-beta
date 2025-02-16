import pytest
from src.find_min import find_min_number

def test_find_min_positive_numbers():
    assert find_min_number([5, 2, 8, 1, 9]) == 1

def test_find_min_negative_numbers():
    assert find_min_number([-5, -2, -8, -1, -9]) == -9

def test_find_min_mixed_numbers():
    assert find_min_number([-5, 2, 0, 8, -1]) == -5

def test_find_min_single_element():
    assert find_min_number([42]) == 42

def test_find_min_float_numbers():
    assert find_min_number([3.14, 2.71, 1.41, 0.58]) == 0.58

def test_empty_list_raises_error():
    with pytest.raises(ValueError, match="Cannot find minimum of an empty list"):
        find_min_number([])

def test_non_list_input_raises_error():
    with pytest.raises(TypeError, match="Input must be a list"):
        find_min_number("not a list")

def test_non_numeric_list_raises_error():
    with pytest.raises(TypeError, match="List must contain only numeric elements"):
        find_min_number([1, 2, "three", 4])