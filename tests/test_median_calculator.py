import pytest
from src.median_calculator import calculate_median

def test_median_odd_length():
    """Test median calculation for odd-length list"""
    assert calculate_median([1, 3, 5]) == 3
    assert calculate_median([1, 2, 3, 4, 5]) == 3
    assert calculate_median([-1, 0, 1]) == 0

def test_median_even_length():
    """Test median calculation for even-length list"""
    assert calculate_median([1, 2, 3, 4]) == 2.5
    assert calculate_median([1, 3, 5, 7]) == 4
    assert calculate_median([-2, -1, 1, 2]) == 0.5

def test_single_element():
    """Test median with a single element"""
    assert calculate_median([42]) == 42

def test_float_numbers():
    """Test median with floating point numbers"""
    assert calculate_median([1.5, 2.5, 3.5]) == 2.5

def test_empty_list_raises_error():
    """Test that empty list raises a ValueError"""
    with pytest.raises(ValueError, match="Cannot calculate median of an empty list"):
        calculate_median([])

def test_non_list_input_raises_error():
    """Test that non-list input raises a TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_median("not a list")

def test_non_numeric_list_raises_error():
    """Test that list with non-numeric values raises a TypeError"""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        calculate_median([1, 2, "three"])
        calculate_median([1, 2, None])