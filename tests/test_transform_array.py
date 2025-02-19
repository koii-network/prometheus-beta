import pytest
from src.transform_array import transform_integers

def test_transform_integers_basic():
    """Test basic transformation of integers"""
    input_array = [0, 1, 2, 3]
    expected = [0, 2, 5, 10]
    assert transform_integers(input_array) == expected

def test_transform_integers_empty_array():
    """Test transformation of an empty array"""
    assert transform_integers([]) == []

def test_transform_integers_zero_only():
    """Test array with only zeros"""
    assert transform_integers([0, 0, 0]) == [0, 0, 0]

def test_transform_integers_non_zero_only():
    """Test array with only non-zero integers"""
    input_array = [1, 2, 3]
    expected = [2, 5, 10]
    assert transform_integers(input_array) == expected

def test_transform_integers_invalid_input():
    """Test that function raises ValueError for negative integers"""
    with pytest.raises(ValueError, match="Input must be a list of non-negative integers"):
        transform_integers([-1, 2, 3])

def test_transform_integers_invalid_type():
    """Test that function raises ValueError for non-integer inputs"""
    with pytest.raises(ValueError, match="Input must be a list of non-negative integers"):
        transform_integers([1, 2, 'a'])