import pytest
from src.array_sum import calculate_array_sum

def test_sum_of_positive_integers():
    assert calculate_array_sum([1, 2, 3, 4, 5]) == 15

def test_sum_of_negative_integers():
    assert calculate_array_sum([-1, -2, -3, -4, -5]) == -15

def test_sum_of_mixed_numbers():
    assert calculate_array_sum([-1, 0, 1, 2.5]) == 2.5

def test_sum_of_empty_array():
    assert calculate_array_sum([]) == 0

def test_input_not_list():
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_array_sum("not a list")

def test_non_numeric_elements():
    with pytest.raises(TypeError, match="All elements must be numeric"):
        calculate_array_sum([1, 2, "three", 4])