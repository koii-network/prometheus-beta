import pytest
from src.max_subarray import kadane_max_subarray

def test_basic_positive_array():
    assert kadane_max_subarray([1, 2, 3, 4]) == 10

def test_mixed_array():
    assert kadane_max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_all_negative_array():
    assert kadane_max_subarray([-1, -2, -3, -4]) == -1

def test_single_element_array():
    assert kadane_max_subarray([5]) == 5

def test_invalid_input_empty_list():
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        kadane_max_subarray([])

def test_invalid_input_type():
    with pytest.raises(TypeError, match="Input must be a list"):
        kadane_max_subarray("not a list")
        
def test_large_numbers():
    assert kadane_max_subarray([10000, -5000, 8000]) == 13000