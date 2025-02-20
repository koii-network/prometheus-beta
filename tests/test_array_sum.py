import pytest
from src.array_sum import sum_array

def test_sum_array_positive_numbers():
    assert sum_array([1, 2, 3, 4, 5]) == 15

def test_sum_array_negative_numbers():
    assert sum_array([-1, -2, -3, -4, -5]) == -15

def test_sum_array_mixed_numbers():
    assert sum_array([-1, 0, 1, 2, 3]) == 5

def test_sum_array_empty_list():
    assert sum_array([]) == 0

def test_sum_array_single_element():
    assert sum_array([42]) == 42

def test_sum_array_invalid_input_non_list():
    with pytest.raises(TypeError, match="Input must be a list"):
        sum_array(42)

def test_sum_array_invalid_input_non_integers():
    with pytest.raises(TypeError, match="All elements must be integers"):
        sum_array([1, 2, '3', 4, 5])