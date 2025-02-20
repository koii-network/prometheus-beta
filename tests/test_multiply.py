import pytest
from src.multiply import multiply

def test_multiply_basic():
    """Test basic multiplication of arrays"""
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    assert multiply(arr1, arr2) == [4, 10, 18]

def test_multiply_with_zero():
    """Test multiplication including zero"""
    arr1 = [0, 2, 3]
    arr2 = [4, 0, 6]
    assert multiply(arr1, arr2) == [0, 0, 18]

def test_multiply_with_floats():
    """Test multiplication with floating point numbers"""
    arr1 = [1.5, 2.0, 3.5]
    arr2 = [2.0, 3.0, 2.0]
    assert multiply(arr1, arr2) == [3.0, 6.0, 7.0]

def test_different_length_arrays():
    """Test that an error is raised for arrays of different lengths"""
    arr1 = [1, 2, 3]
    arr2 = [4, 5]
    with pytest.raises(ValueError, match="Input arrays must have the same length"):
        multiply(arr1, arr2)

def test_non_numeric_elements():
    """Test that an error is raised for non-numeric elements"""
    arr1 = [1, 2, 'a']
    arr2 = [4, 5, 6]
    with pytest.raises(TypeError, match="All array elements must be numeric"):
        multiply(arr1, arr2)

def test_empty_arrays():
    """Test multiplication with empty arrays"""
    assert multiply([], []) == []