import pytest
from src.array_minmax import find_highest_lowest

def test_basic_array():
    """Test with a basic array of integers"""
    assert find_highest_lowest([1, 2, 3, 4, 5]) == (1, 5)

def test_array_with_negative_numbers():
    """Test array containing negative numbers"""
    assert find_highest_lowest([-1, -5, 0, 5, 10]) == (-5, 10)

def test_array_with_floats():
    """Test array with floating-point numbers"""
    assert find_highest_lowest([1.5, 2.3, -0.5, 10.1]) == (-0.5, 10.1)

def test_single_element_array():
    """Test array with a single element"""
    assert find_highest_lowest([42]) == (42, 42)

def test_empty_array_raises_error():
    """Test that an empty array raises a ValueError"""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_highest_lowest([])

def test_non_numeric_array_raises_error():
    """Test that an array with non-numeric values raises a TypeError"""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        find_highest_lowest([1, 2, 'three', 4])