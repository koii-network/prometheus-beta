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
    assert calculate_median([1, 3, 4, 6]) == 3.5
    assert calculate_median([-2, -1, 1, 2]) == 0.5

def test_median_single_element():
    """Test median for a single-element list"""
    assert calculate_median([42]) == 42

def test_float_inputs():
    """Test median with float inputs"""
    assert calculate_median([1.5, 2.5, 3.5]) == 2.5

def test_empty_list_raises_error():
    """Test that empty list raises a ValueError"""
    with pytest.raises(ValueError, match="Cannot calculate median of an empty list"):
        calculate_median([])

def test_non_numeric_inputs_raises_error():
    """Test that non-numeric inputs raise a TypeError"""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        calculate_median(['a', 'b', 'c'])
    
    with pytest.raises(TypeError):
        calculate_median([1, 2, '3'])

def test_mixed_numeric_types():
    """Test median calculation with mixed numeric types"""
    assert calculate_median([1, 2, 3.0, 4]) == 2.5
    assert calculate_median([-1, 0, 1.5]) == 0