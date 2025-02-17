import pytest
from src.array_sum import calculate_array_sum

def test_calculate_array_sum_positive_integers():
    assert calculate_array_sum([1, 2, 3, 4, 5]) == 15

def test_calculate_array_sum_mixed_numbers():
    assert calculate_array_sum([1.5, 2, -3, 4.5]) == 5

def test_calculate_array_sum_empty_list():
    assert calculate_array_sum([]) == 0

def test_calculate_array_sum_single_element():
    assert calculate_array_sum([42]) == 42

def test_calculate_array_sum_invalid_input():
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_array_sum("not a list")

def test_calculate_array_sum_non_numeric():
    with pytest.raises(TypeError, match="All elements must be numeric"):
        calculate_array_sum([1, 2, "three", 4])