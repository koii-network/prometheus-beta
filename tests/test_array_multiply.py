import pytest
from src.array_multiply import multiply

def test_multiply_basic():
    """Test basic multiplication of two lists."""
    input_lists = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    assert multiply(input_lists) == [4, 10, 18]

def test_multiply_multiple_lists():
    """Test multiplication of multiple lists."""
    input_lists = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert multiply(input_lists) == [28, 80, 162]

def test_multiply_floats():
    """Test multiplication with floating point numbers."""
    input_lists = [
        [1.5, 2.0],
        [2.0, 3.0]
    ]
    assert multiply(input_lists) == [3.0, 6.0]

def test_empty_input_raises_error():
    """Test that empty input raises a ValueError."""
    with pytest.raises(ValueError, match="Input must be a non-empty list of lists"):
        multiply([])

def test_non_list_input_raises_error():
    """Test that non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list of lists"):
        multiply(42)

def test_lists_with_different_lengths_raises_error():
    """Test that lists with different lengths raise a ValueError."""
    with pytest.raises(ValueError, match="All input lists must have the same length"):
        multiply([[1, 2], [3]])

def test_empty_sublist_raises_error():
    """Test that empty sublists raise a ValueError."""
    with pytest.raises(ValueError, match="All input lists must be non-empty"):
        multiply([[1, 2], []])

def test_non_numeric_elements_raises_error():
    """Test that non-numeric elements raise a TypeError."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        multiply([[1, 2], ['a', 'b']])

def test_single_list_input():
    """Test multiplication with a single list."""
    input_lists = [[1, 2, 3]]
    assert multiply(input_lists) == [1, 2, 3]