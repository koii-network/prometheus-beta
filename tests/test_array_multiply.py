import pytest
from src.array_multiply import multiply

def test_basic_multiply():
    """Test basic multiplication of corresponding elements"""
    input_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected = [28, 80, 162]
    assert multiply(input_lists) == expected

def test_empty_input():
    """Test empty input returns empty list"""
    assert multiply([]) == []

def test_single_list():
    """Test multiplication with a single list"""
    input_lists = [[1, 2, 3]]
    assert multiply(input_lists) == [1, 2, 3]

def test_error_different_lengths():
    """Test error raised when sublists have different lengths"""
    with pytest.raises(ValueError, match="All input lists must have the same length"):
        multiply([[1, 2], [3, 4, 5]])

def test_error_invalid_input():
    """Test error raised with invalid input types"""
    with pytest.raises(ValueError, match="Input must be a list of lists"):
        multiply([1, 2, 3])
    with pytest.raises(ValueError, match="Input must be a list of lists"):
        multiply("not a list")

def test_multiply_with_zero():
    """Test multiplication when one list contains zero"""
    input_lists = [[1, 2, 3], [0, 5, 6], [7, 8, 9]]
    expected = [0, 80, 162]
    assert multiply(input_lists) == expected

def test_multiply_with_negative():
    """Test multiplication with negative numbers"""
    input_lists = [[1, -2, 3], [4, 5, -6], [7, -8, 9]]
    expected = [28, -80, -162]
    assert multiply(input_lists) == expected