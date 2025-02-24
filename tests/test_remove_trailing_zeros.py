import pytest
from src.remove_trailing_zeros import remove_trailing_zeros

def test_remove_trailing_zeros_basic():
    """Test removing trailing zeros from various numbers."""
    assert remove_trailing_zeros(10200) == 102
    assert remove_trailing_zeros(123000) == 123
    assert remove_trailing_zeros(45600) == 456

def test_remove_trailing_zeros_edge_cases():
    """Test edge cases for the function."""
    assert remove_trailing_zeros(0) == 0
    assert remove_trailing_zeros(100) == 1
    assert remove_trailing_zeros(123) == 123

def test_remove_trailing_zeros_negative_input():
    """Test that a negative input raises a ValueError."""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        remove_trailing_zeros(-100)

def test_remove_trailing_zeros_large_number():
    """Test the function with a large number with multiple trailing zeros."""
    assert remove_trailing_zeros(10000000) == 1