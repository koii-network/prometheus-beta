import pytest
from src.median_finder import find_median

def test_median_odd_length():
    """Test median calculation for odd-length list."""
    assert find_median([1, 3, 5]) == 3
    assert find_median([1, 2, 3, 4, 5]) == 3

def test_median_even_length():
    """Test median calculation for even-length list."""
    assert find_median([1, 2, 3, 4]) == 2.5
    assert find_median([2, 4, 6, 8]) == 5

def test_single_element():
    """Test median with a single element list."""
    assert find_median([42]) == 42

def test_float_numbers():
    """Test median with floating point numbers."""
    assert find_median([1.5, 2.5, 3.5]) == 2.5

def test_error_empty_list():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot find median of an empty list"):
        find_median([])

def test_error_non_list_input():
    """Test that non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_median(42)
    with pytest.raises(TypeError, match="Input must be a list"):
        find_median("not a list")

def test_error_non_numeric_list():
    """Test that a list with non-numeric values raises a TypeError."""
    with pytest.raises(TypeError, match="All list elements must be numeric"):
        find_median([1, 2, "three"])
    with pytest.raises(TypeError, match="All list elements must be numeric"):
        find_median([1, None, 3])