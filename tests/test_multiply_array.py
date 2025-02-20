import pytest
from src.multiply_array import multiply

def test_multiply_basic():
    """Test basic multiplication of two lists"""
    result = multiply([[1, 2, 3], [4, 5, 6]])
    assert result == [4, 10, 18]

def test_multiply_multiple_lists():
    """Test multiplication of multiple lists"""
    result = multiply([[1, 2, 3], [4, 5, 6], [2, 2, 2]])
    assert result == [8, 20, 36]

def test_multiply_negative_numbers():
    """Test multiplication with negative numbers"""
    result = multiply([[-1, 2, -3], [4, -5, 6]])
    assert result == [-4, -10, -18]

def test_multiply_floating_point():
    """Test multiplication with floating-point numbers"""
    result = multiply([[1.5, 2.5], [2.0, 4.0]])
    assert result == [3.0, 10.0]

def test_empty_lists():
    """Test multiplication with empty lists"""
    result = multiply([])
    assert result == []

def test_invalid_input_not_list():
    """Test that non-list input raises ValueError"""
    with pytest.raises(ValueError, match="Input must be a list of lists"):
        multiply("not a list")

def test_different_length_lists():
    """Test that lists of different lengths raise ValueError"""
    with pytest.raises(ValueError, match="All input lists must have the same length"):
        multiply([[1, 2], [3, 4, 5]])