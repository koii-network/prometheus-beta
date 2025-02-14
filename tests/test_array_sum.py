import pytest
from src.array_sum import sum_array_elements

def test_sum_array_elements_positive_integers():
    assert sum_array_elements([1, 2, 3, 4, 5]) == 15

def test_sum_array_elements_negative_integers():
    assert sum_array_elements([-1, -2, -3]) == -6

def test_sum_array_elements_mixed_numbers():
    assert sum_array_elements([1.5, 2, -3.5, 4]) == 4

def test_sum_array_elements_empty_list():
    assert sum_array_elements([]) == 0

def test_sum_array_elements_invalid_input_type():
    with pytest.raises(TypeError, match="Input must be a list"):
        sum_array_elements("not a list")

def test_sum_array_elements_non_numeric_elements():
    with pytest.raises(TypeError, match="All elements must be numeric"):
        sum_array_elements([1, 2, "three", 4])