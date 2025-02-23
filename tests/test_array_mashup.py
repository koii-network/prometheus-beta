import pytest
from src.array_mashup import arrayMashup

def test_arrayMashup_basic_functionality():
    """Test basic array mashup with positive integers"""
    result = arrayMashup([1, 2, 3], [4, 5, 6])
    assert result == [5, 7, 9]

def test_arrayMashup_single_element_arrays():
    """Test array mashup with single-element arrays"""
    result = arrayMashup([10], [20])
    assert result == [30]

def test_arrayMashup_zero_arrays():
    """Test array mashup with zeros"""
    result = arrayMashup([0, 1, 2], [3, 4, 5])
    assert result == [3, 5, 7]

def test_arrayMashup_different_length_arrays():
    """Test that different length arrays raise a ValueError"""
    with pytest.raises(ValueError, match="Input arrays must have the same length"):
        arrayMashup([1, 2], [1, 2, 3])

def test_arrayMashup_non_integer_input():
    """Test that non-integer inputs raise a TypeError"""
    with pytest.raises(TypeError, match="All elements must be positive integers"):
        arrayMashup([1, 2, 'a'], [3, 4, 5])

def test_arrayMashup_negative_integers():
    """Test that non-positive integers raise a TypeError"""
    with pytest.raises(TypeError, match="All elements must be positive integers"):
        arrayMashup([1, 2, -3], [3, 4, 5])