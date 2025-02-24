import pytest
from src.array_mashup import arrayMashup

def test_basic_array_mashup():
    """Test basic element-wise array summing"""
    result = arrayMashup([1, 2, 3], [4, 5, 6])
    assert result == [5, 7, 9]

def test_single_element_arrays():
    """Test arrays with single elements"""
    result = arrayMashup([1], [2])
    assert result == [3]

def test_zero_arrays():
    """Test arrays with single elements"""
    result = arrayMashup([10], [20])
    assert result == [30]

def test_invalid_input_not_list():
    """Test that non-list inputs raise ValueError"""
    with pytest.raises(ValueError, match="Inputs must be lists"):
        arrayMashup("not a list", [1, 2, 3])

def test_different_length_arrays():
    """Test that arrays of different lengths raise ValueError"""
    with pytest.raises(ValueError, match="Input arrays must have the same length"):
        arrayMashup([1, 2], [1, 2, 3])

def test_non_positive_integers():
    """Test that non-positive integers raise ValueError"""
    with pytest.raises(ValueError, match="must contain only positive integers"):
        arrayMashup([1, 2, -3], [4, 5, 6])

def test_non_integer_inputs():
    """Test that non-integer inputs raise ValueError"""
    with pytest.raises(ValueError, match="must contain only positive integers"):
        arrayMashup([1, 2, 3.5], [4, 5, 6])

def test_empty_arrays():
    """Test empty arrays"""
    result = arrayMashup([], [])
    assert result == []