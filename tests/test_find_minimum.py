import pytest
from src.find_minimum import find_minimum

def test_find_minimum_positive_numbers():
    assert find_minimum([1, 2, 3, 4, 5]) == 1
    assert find_minimum([5, 4, 3, 2, 1]) == 1
    assert find_minimum([10, 5, 8, 3, 7]) == 3

def test_find_minimum_with_negatives():
    assert find_minimum([-1, -2, -3, -4, -5]) == -5
    assert find_minimum([-5, 0, 5]) == -5

def test_find_minimum_mixed_numbers():
    assert find_minimum([-10, 0, 10, 5, -5]) == -10

def test_find_minimum_float_numbers():
    assert find_minimum([1.5, 2.3, 0.1, 4.7]) == 0.1

def test_find_minimum_single_element():
    assert find_minimum([42]) == 42

def test_empty_list_raises_error():
    with pytest.raises(ValueError, match="Cannot find minimum of an empty list"):
        find_minimum([])

def test_non_list_input_raises_error():
    with pytest.raises(TypeError, match="Input must be a list"):
        find_minimum("not a list")

def test_non_numeric_list_raises_error():
    with pytest.raises(TypeError, match="All elements must be numeric"):
        find_minimum([1, 2, "three", 4])
    with pytest.raises(TypeError, match="All elements must be numeric"):
        find_minimum([1, 2, None, 4])