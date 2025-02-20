import pytest
from src.array_multiplication import multiply_array_elements

def test_multiply_numeric_arrays():
    """Test multiplication of numeric arrays"""
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    assert multiply_array_elements(arr1, arr2) == [4, 10, 18]

def test_multiply_mixed_numeric_arrays():
    """Test multiplication of mixed numeric types"""
    arr1 = [1.5, 2, 3]
    arr2 = [2, 3.0, 4]
    assert multiply_array_elements(arr1, arr2) == [3.0, 6.0, 12]

def test_multiply_mixed_type_arrays():
    """Test multiplication of mixed type arrays"""
    arr1 = [2, 'a', 3]
    arr2 = [3, 2, 4]
    assert multiply_array_elements(arr1, arr2) == [6, 'aa', 12]

def test_empty_arrays():
    """Test multiplication of empty arrays"""
    assert multiply_array_elements([], []) == []

def test_unequal_length_arrays():
    """Test that an error is raised for arrays of different lengths"""
    with pytest.raises(ValueError, match="Input arrays must have the same length"):
        multiply_array_elements([1, 2], [1, 2, 3])

def test_multiply_boolean_arrays():
    """Test multiplication of boolean arrays"""
    arr1 = [True, False, True]
    arr2 = [False, True, True]
    assert multiply_array_elements(arr1, arr2) == [False, False, True]