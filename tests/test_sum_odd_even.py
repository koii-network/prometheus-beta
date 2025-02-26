import pytest
from src.sum_odd_even import sum_odd_even_numbers

def test_mixed_array():
    """Test an array with mixed odd and even numbers."""
    result = sum_odd_even_numbers([1, 2, 3, 4, 5, 6])
    assert result == (9, 12)

def test_empty_array():
    """Test an empty array returns (0, 0)."""
    result = sum_odd_even_numbers([])
    assert result == (0, 0)

def test_only_odd_numbers():
    """Test an array with only odd numbers."""
    result = sum_odd_even_numbers([1, 3, 5, 7])
    assert result == (16, 0)

def test_only_even_numbers():
    """Test an array with only even numbers."""
    result = sum_odd_even_numbers([2, 4, 6, 8])
    assert result == (0, 20)

def test_negative_numbers():
    """Test an array with negative odd and even numbers."""
    result = sum_odd_even_numbers([-1, -2, -3, -4, -5, -6])
    assert result == (-9, -12)

def test_zero_included():
    """Test an array that includes zero."""
    result = sum_odd_even_numbers([0, 1, 2, 3])
    assert result == (4, 2)

def test_invalid_input_type():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        sum_odd_even_numbers("not a list")

def test_invalid_element_type():
    """Test that TypeError is raised for non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        sum_odd_even_numbers([1, 2, "3", 4])