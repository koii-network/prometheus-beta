import pytest
from src.digit_multiplication import multiply_digit_arrays

def test_basic_multiplication():
    assert multiply_digit_arrays([1, 2], [3, 4]) == [4, 0, 8]
    assert multiply_digit_arrays([9, 9], [9, 9]) == [9, 8, 0, 1]

def test_zero_multiplication():
    assert multiply_digit_arrays([0, 0], [1, 2]) == [0]
    assert multiply_digit_arrays([1, 2], [0, 0]) == [0]

def test_single_digit_multiplication():
    assert multiply_digit_arrays([5], [7]) == [3, 5]

def test_equal_length_requirement():
    with pytest.raises(ValueError, match="Input arrays must be of equal length"):
        multiply_digit_arrays([1, 2], [3, 4, 5])

def test_digit_validation():
    with pytest.raises(ValueError, match="All elements must be single digits"):
        multiply_digit_arrays([1, 10], [3, 4])
    
    with pytest.raises(ValueError, match="All elements must be single digits"):
        multiply_digit_arrays([1, -1], [3, 4])

def test_large_number_multiplication():
    assert multiply_digit_arrays([9, 9, 9], [9, 9, 9]) == [9, 9, 8, 0, 0, 1]