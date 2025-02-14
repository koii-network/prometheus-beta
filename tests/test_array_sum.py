import pytest
from src.array_sum import calculate_array_sum

def test_sum_positive_integers():
    assert calculate_array_sum([1, 2, 3, 4, 5]) == 15

def test_sum_negative_integers():
    assert calculate_array_sum([-1, -2, -3]) == -6

def test_sum_mixed_numbers():
    assert calculate_array_sum([1.5, 2, -3.5, 4]) == 4

def test_sum_empty_array():
    assert calculate_array_sum([]) == 0

def test_sum_single_element():
    assert calculate_array_sum([42]) == 42

def test_invalid_input_not_list():
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_array_sum("not a list")

def test_invalid_input_non_numeric():
    with pytest.raises(TypeError, match="All elements must be numeric"):
        calculate_array_sum([1, 2, "three", 4])