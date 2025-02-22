import pytest
from src.array_digit_multiplication import multiply_digit_arrays

def test_basic_multiplication():
    # Basic multiplication test
    assert multiply_digit_arrays([1, 2, 3], [4, 5, 6]) == [5, 6, 0, 8, 8]

def test_zero_multiplication():
    # Test multiplication involving zeros
    assert multiply_digit_arrays([0, 0, 1], [1, 2, 3]) == [0, 0, 1, 2, 3]

def test_single_digit_multiplication():
    # Single digit test
    assert multiply_digit_arrays([9], [9]) == [8, 1]

def test_different_digit_lengths():
    # Test different combinations of digit arrays
    assert multiply_digit_arrays([1, 0], [1, 1]) == [1, 1, 0]

def test_input_validation_unequal_length():
    # Test that unequal length arrays raise ValueError
    with pytest.raises(ValueError, match="Input arrays must be of equal length"):
        multiply_digit_arrays([1, 2], [1, 2, 3])

def test_input_validation_non_digit():
    # Test that non-digit inputs raise ValueError
    with pytest.raises(ValueError, match="All elements must be single digits"):
        multiply_digit_arrays([1, 10], [2, 3])
    with pytest.raises(ValueError, match="All elements must be single digits"):
        multiply_digit_arrays([1, -1], [2, 3])