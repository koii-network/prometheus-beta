import pytest
from src.array_mashup import arrayMashup

def test_basic_mashup():
    """Test basic functionality of arrayMashup"""
    result = arrayMashup([1, 2, 3], [4, 5, 6])
    assert result == [5, 7, 9], "Should sum corresponding elements"

def test_single_element_arrays():
    """Test arrayMashup with single-element arrays"""
    result = arrayMashup([10], [20])
    assert result == [30], "Should work with single-element arrays"

def test_different_length_arrays_raises_error():
    """Test that different length arrays raise ValueError"""
    with pytest.raises(ValueError, match="Input arrays must have equal length"):
        arrayMashup([1, 2], [1, 2, 3])

def test_non_list_input_raises_error():
    """Test that non-list inputs raise TypeError"""
    with pytest.raises(TypeError, match="Inputs must be lists"):
        arrayMashup(123, [1, 2, 3])
    with pytest.raises(TypeError, match="Inputs must be lists"):
        arrayMashup([1, 2, 3], 123)

def test_non_positive_integer_raises_error():
    """Test that non-positive or non-integer inputs raise TypeError"""
    with pytest.raises(TypeError, match="All elements must be positive integers"):
        arrayMashup([1, 2, -3], [4, 5, 6])
    with pytest.raises(TypeError, match="All elements must be positive integers"):
        arrayMashup([1, 2, 3], [4, 5, 6.5])

def test_zero_is_not_allowed():
    """Test that zero is not considered a valid input"""
    with pytest.raises(TypeError, match="All elements must be positive integers"):
        arrayMashup([0, 1, 2], [3, 4, 5])

def test_large_numbers():
    """Test arrayMashup with large positive integers"""
    result = arrayMashup([1000000, 2000000], [3000000, 4000000])
    assert result == [4000000, 6000000], "Should handle large positive integers"