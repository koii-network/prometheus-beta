import pytest
from src.triangular_numbers import count_triangular_numbers

def test_count_triangular_numbers():
    """Test the count_triangular_numbers function."""
    # Test some known cases
    assert count_triangular_numbers(0) == 0  # No triangular numbers <= 0
    assert count_triangular_numbers(1) == 1  # First triangular number
    assert count_triangular_numbers(3) == 2  # First two triangular numbers (1, 3)
    assert count_triangular_numbers(6) == 3  # First three triangular numbers (1, 3, 6)
    assert count_triangular_numbers(10) == 4  # First four triangular numbers (1, 3, 6, 10)
    assert count_triangular_numbers(15) == 5  # First five triangular numbers (1, 3, 6, 10, 15)

def test_large_input():
    """Test with a larger input."""
    assert count_triangular_numbers(100) == 13  # First 13 triangular numbers

def test_negative_input():
    """Test that negative inputs raise a ValueError."""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        count_triangular_numbers(-5)

def test_non_integer_input():
    """Test that non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        count_triangular_numbers(3.14)
    with pytest.raises(TypeError, match="Input must be an integer"):
        count_triangular_numbers("10")