import pytest
from src.fibonacci_reverse import fibonacci_reverse

def test_fibonacci_reverse_zero():
    """Test generating Fibonacci sequence with 0 elements."""
    assert fibonacci_reverse(0) == []

def test_fibonacci_reverse_one():
    """Test generating Fibonacci sequence with 1 element."""
    assert fibonacci_reverse(1) == [0]

def test_fibonacci_reverse_two():
    """Test generating Fibonacci sequence with 2 elements."""
    assert fibonacci_reverse(2) == [1, 0]

def test_fibonacci_reverse_five():
    """Test generating Fibonacci sequence with 5 elements."""
    assert fibonacci_reverse(5) == [3, 2, 1, 1, 0]

def test_fibonacci_reverse_six():
    """Test generating Fibonacci sequence with 6 elements."""
    assert fibonacci_reverse(6) == [5, 3, 2, 1, 1, 0]

def test_fibonacci_reverse_negative_input():
    """Test that a negative input raises a ValueError."""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        fibonacci_reverse(-1)

def test_fibonacci_reverse_non_integer_input():
    """Test that a non-integer input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_reverse("3")
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_reverse(3.14)
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_reverse(None)