import pytest
from src.array_mashup import arrayMashup

def test_array_mashup_basic():
    """Test basic functionality of arrayMashup"""
    result = arrayMashup([1, 2, 3], [4, 5, 6])
    assert result == [5, 7, 9]

def test_array_mashup_single_element():
    """Test arrayMashup with single-element arrays"""
    result = arrayMashup([10], [20])
    assert result == [30]

def test_array_mashup_zero_values():
    """Test arrayMashup with zero values"""
    result = arrayMashup([0, 1, 2], [3, 0, 4])
    assert result == [3, 1, 6]

def test_array_mashup_different_lengths_error():
    """Test that an error is raised for arrays of different lengths"""
    with pytest.raises(ValueError, match="Input arrays must have the same length"):
        arrayMashup([1, 2], [1, 2, 3])

def test_array_mashup_non_integer_error():
    """Test that an error is raised for non-integer inputs"""
    with pytest.raises(TypeError, match="All elements must be positive integers"):
        arrayMashup([1, 2, 3], [4, '5', 6])

def test_array_mashup_negative_integer_error():
    """Test that an error is raised for negative integers"""
    with pytest.raises(TypeError, match="All elements must be positive integers"):
        arrayMashup([1, 2, 3], [4, -5, 6])