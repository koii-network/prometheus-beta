import pytest
from src.array_digit_multiplication import multiply_digit_arrays

def test_basic_multiplication():
    # Test a simple multiplication
    assert multiply_digit_arrays([1, 2], [3, 4]) == [4, 0, 8]

def test_zero_inputs():
    # Test multiplication with zeros
    assert multiply_digit_arrays([0, 0], [1, 2]) == [0]

def test_single_digit():
    # Test single digit multiplication
    assert multiply_digit_arrays([5], [6]) == [3, 0]

def test_different_lengths_raises_error():
    # Test that different length inputs raise an error
    with pytest.raises(ValueError, match="Input arrays must be of equal length"):
        multiply_digit_arrays([1, 2], [3, 4, 5])

def test_non_digit_inputs_raises_error():
    # Test that non-digit inputs raise an error
    with pytest.raises(ValueError, match="All elements must be single digits between 0 and 9"):
        multiply_digit_arrays([1, 10], [3, 4])
    
    with pytest.raises(ValueError, match="All elements must be single digits between 0 and 9"):
        multiply_digit_arrays([1, -1], [3, 4])

def test_large_number_multiplication():
    # Test multiplication of larger numbers
    assert multiply_digit_arrays([9, 9], [9, 9]) == [9, 8, 0, 1]