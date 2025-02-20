import pytest
from src.array_mashup import arrayMashup

def test_arrayMashup_basic():
    """Test basic functionality of arrayMashup"""
    assert arrayMashup([1, 2, 3], [4, 5, 6]) == [5, 7, 9]

def test_arrayMashup_empty_arrays():
    """Test with empty arrays"""
    assert arrayMashup([], []) == []

def test_arrayMashup_single_element():
    """Test with single-element arrays"""
    assert arrayMashup([10], [20]) == [30]

def test_arrayMashup_different_lengths():
    """Test that different length arrays raise a ValueError"""
    with pytest.raises(ValueError, match="Input arrays must have the same length"):
        arrayMashup([1, 2], [1, 2, 3])

def test_arrayMashup_zero_values():
    """Test arrays with zero values"""
    assert arrayMashup([0, 0, 0], [1, 2, 3]) == [1, 2, 3]

def test_arrayMashup_large_numbers():
    """Test with large numbers"""
    assert arrayMashup([1000, 2000], [3000, 4000]) == [4000, 6000]