import pytest
from src.array_multiplier import multiply_arrays

def test_multiply_numeric_arrays():
    """Test multiplication of numeric arrays"""
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    expected = [4, 10, 18]
    assert multiply_arrays(arr1, arr2) == expected

def test_multiply_float_arrays():
    """Test multiplication of float arrays"""
    arr1 = [1.5, 2.0, 3.5]
    arr2 = [2.0, 3.0, 4.0]
    expected = [3.0, 6.0, 14.0]
    assert multiply_arrays(arr1, arr2) == expected

def test_multiply_mixed_numeric_arrays():
    """Test multiplication of mixed numeric arrays"""
    arr1 = [1, 2.5, 3]
    arr2 = [4, 2, 6]
    expected = [4, 5.0, 18]
    assert multiply_arrays(arr1, arr2) == expected

def test_empty_arrays():
    """Test multiplication of empty arrays"""
    assert multiply_arrays([], []) == []

def test_mismatched_array_lengths():
    """Test that ValueError is raised for arrays of different lengths"""
    with pytest.raises(ValueError, match="Input arrays must have the same length"):
        multiply_arrays([1, 2], [1, 2, 3])

def test_zero_multiplication():
    """Test multiplication involving zero"""
    arr1 = [0, 5, -3]
    arr2 = [10, 0, 2]
    expected = [0, 0, -6]
    assert multiply_arrays(arr1, arr2) == expected