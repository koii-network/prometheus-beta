import pytest
from src.fibonacci import fibonacci_sequence

def test_fibonacci_zero_elements():
    """Test generating 0 Fibonacci sequence elements."""
    assert fibonacci_sequence(0) == []

def test_fibonacci_one_element():
    """Test generating 1 Fibonacci sequence element."""
    assert fibonacci_sequence(1) == [0]

def test_fibonacci_multiple_elements():
    """Test generating multiple Fibonacci sequence elements."""
    assert fibonacci_sequence(5) == [0, 1, 1, 2, 3]
    assert fibonacci_sequence(7) == [0, 1, 1, 2, 3, 5, 8]

def test_fibonacci_large_input():
    """Test generating a larger Fibonacci sequence."""
    result = fibonacci_sequence(10)
    assert len(result) == 10
    assert result == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def test_fibonacci_negative_input():
    """Test that a negative input raises a ValueError."""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        fibonacci_sequence(-1)

def test_fibonacci_invalid_input_type():
    """Test that non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_sequence(3.14)
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_sequence("5")