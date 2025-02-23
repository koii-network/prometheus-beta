import pytest
from src.median_finder import find_median

def test_median_odd_length_list():
    """Test median calculation for odd-length list."""
    assert find_median([1, 3, 5]) == 3.0
    assert find_median([1, 2, 3, 4, 5]) == 3.0

def test_median_even_length_list():
    """Test median calculation for even-length list."""
    assert find_median([1, 2, 3, 4]) == 2.5
    assert find_median([2, 4, 6, 8]) == 5.0

def test_median_single_element():
    """Test median calculation for single-element list."""
    assert find_median([42]) == 42.0

def test_median_floating_point():
    """Test median calculation with floating-point numbers."""
    assert find_median([1.5, 2.5, 3.5]) == 2.5

def test_input_type_error():
    """Test error handling for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_median(42)
    with pytest.raises(TypeError, match="Input must be a list"):
        find_median("not a list")

def test_empty_list_error():
    """Test error handling for empty list."""
    with pytest.raises(ValueError, match="Cannot find median of an empty list"):
        find_median([])

def test_non_numeric_list_error():
    """Test error handling for lists with non-numeric elements."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        find_median([1, 2, "three"])
    with pytest.raises(TypeError, match="All elements must be numeric"):
        find_median([1, 2, None])