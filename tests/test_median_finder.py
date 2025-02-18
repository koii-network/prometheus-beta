import pytest
from src.median_finder import find_median

def test_median_odd_length():
    """Test median for a list with odd number of elements"""
    assert find_median([1, 3, 5]) == 3
    assert find_median([1, 2, 3, 4, 5]) == 3
    assert find_median([-1, 0, 1]) == 0

def test_median_even_length():
    """Test median for a list with even number of elements"""
    assert find_median([1, 2, 3, 4]) == 2.5
    assert find_median([2, 4, 6, 8]) == 5
    assert find_median([-2, -1, 1, 2]) == 0.5

def test_single_element():
    """Test median for a single element list"""
    assert find_median([42]) == 42

def test_unsorted_input():
    """Test that input order doesn't affect result"""
    assert find_median([5, 1, 3]) == 3
    assert find_median([4, 2, 6, 1]) == 3

def test_floating_point_numbers():
    """Test median with floating point numbers"""
    assert find_median([1.5, 2.5, 3.5]) == 2.5

def test_empty_list_raises_error():
    """Test that empty list raises a ValueError"""
    with pytest.raises(ValueError, match="Cannot find median of an empty list"):
        find_median([])

def test_non_list_input_raises_error():
    """Test that non-list input raises a TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_median("not a list")

def test_non_numeric_input_raises_error():
    """Test that list with non-numeric elements raises a TypeError"""
    with pytest.raises(TypeError, match="All list elements must be numeric"):
        find_median([1, 2, "three"])
    with pytest.raises(TypeError, match="All list elements must be numeric"):
        find_median([1, None, 3])