import pytest
from src.array_sum import calculate_array_sum

def test_calculate_array_sum_positive_numbers():
    assert calculate_array_sum([1, 2, 3, 4, 5]) == 15

def test_calculate_array_sum_negative_numbers():
    assert calculate_array_sum([-1, -2, -3]) == -6

def test_calculate_array_sum_mixed_numbers():
    assert calculate_array_sum([-1, 0, 1]) == 0

def test_calculate_array_sum_floating_point():
    assert calculate_array_sum([1.5, 2.5, 3.0]) == 7.0

def test_calculate_array_sum_empty_list():
    assert calculate_array_sum([]) == 0

def test_calculate_array_sum_invalid_input_not_list():
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_array_sum("not a list")

def test_calculate_array_sum_invalid_input_non_numeric():
    with pytest.raises(TypeError, match="All elements must be numeric"):
        calculate_array_sum([1, 2, "three"])