import pytest
from src.array_mashup import arrayMashup

def test_basic_mashup():
    """Test basic functionality of arrayMashup"""
    result = arrayMashup([1, 2, 3], [4, 5, 6])
    assert result == [5, 7, 9], "Should sum corresponding elements"

def test_single_element_arrays():
    """Test arrayMashup with single-element arrays"""
    result = arrayMashup([5], [7])
    assert result == [12], "Should work with single-element arrays"

def test_different_lengths_raises_error():
    """Test that different length arrays raise ValueError"""
    with pytest.raises(ValueError, match="Input arrays must have the same length"):
        arrayMashup([1, 2], [3, 4, 5])

def test_empty_arrays_raises_error():
    """Test that empty arrays raise ValueError"""
    with pytest.raises(ValueError, match="Input arrays cannot be empty"):
        arrayMashup([], [1, 2, 3])
    with pytest.raises(ValueError, match="Input arrays cannot be empty"):
        arrayMashup([1, 2, 3], [])

def test_non_positive_integers_raises_error():
    """Test that non-positive integers raise TypeError"""
    with pytest.raises(TypeError, match="All elements must be positive integers"):
        arrayMashup([1, 2, -3], [4, 5, 6])
    with pytest.raises(TypeError, match="All elements must be positive integers"):
        arrayMashup([1, 2, 3], [4, 5, 0])

def test_non_integer_inputs_raises_error():
    """Test that non-integer inputs raise TypeError"""
    with pytest.raises(TypeError, match="All elements must be positive integers"):
        arrayMashup([1, 2, '3'], [4, 5, 6])
    with pytest.raises(TypeError, match="Inputs must be lists"):
        arrayMashup(1, [4, 5, 6])
    with pytest.raises(TypeError, match="Inputs must be lists"):
        arrayMashup([1, 2, 3], 4)