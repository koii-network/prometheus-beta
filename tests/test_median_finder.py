import pytest
from src.median_finder import find_median

def test_median_odd_length():
    """Test median for a list with odd number of elements"""
    assert find_median([1, 3, 5]) == 3.0
    assert find_median([1, 2, 3, 4, 5]) == 3.0

def test_median_even_length():
    """Test median for a list with even number of elements"""
    assert find_median([1, 2, 3, 4]) == 2.5
    assert find_median([1, 3, 5, 7]) == 4.0

def test_median_single_element():
    """Test median for a list with a single element"""
    assert find_median([42]) == 42.0

def test_median_with_floats():
    """Test median with floating point numbers"""
    assert find_median([1.5, 2.5, 3.5]) == 2.5

def test_empty_list_error():
    """Test that an empty list raises a ValueError"""
    with pytest.raises(ValueError, match="Cannot find median of an empty list"):
        find_median([])

def test_non_list_input_error():
    """Test that non-list input raises a TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_median(42)
    with pytest.raises(TypeError, match="Input must be a list"):
        find_median("not a list")

def test_non_numeric_list_error():
    """Test that a list with non-numeric elements raises a TypeError"""
    with pytest.raises(TypeError, match="List must contain only numeric elements"):
        find_median([1, 2, 'three'])
    with pytest.raises(TypeError, match="List must contain only numeric elements"):
        find_median([1, 2, None])