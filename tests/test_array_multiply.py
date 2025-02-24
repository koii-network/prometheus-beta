import pytest
from src.array_multiply import multiply

def test_multiply_positive_integers():
    """Test multiplication with positive integers."""
    assert multiply([1, 2, 3]) == [1, 4, 9]

def test_multiply_mixed_numbers():
    """Test multiplication with mixed positive and negative numbers."""
    assert multiply([-1, 2, -3]) == [1, 4, 9]

def test_multiply_floating_point():
    """Test multiplication with floating point numbers."""
    assert multiply([1.5, 2.0, 3.5]) == [2.25, 4.0, 12.25]

def test_multiply_zero():
    """Test multiplication with zero."""
    assert multiply([0, 1, 2]) == [0, 1, 4]

def test_invalid_input_type():
    """Test error handling for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        multiply("not a list")

def test_empty_list():
    """Test error handling for empty list."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        multiply([])

def test_non_numeric_elements():
    """Test error handling for non-numeric elements."""
    with pytest.raises(TypeError, match="List must contain only numeric elements"):
        multiply([1, 2, "three"])