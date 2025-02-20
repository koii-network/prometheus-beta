import pytest
from src.fibonacci import fibonacci_recursive

def test_fibonacci_zero_terms():
    """Test generating Fibonacci sequence with 0 terms."""
    assert fibonacci_recursive(0) == []

def test_fibonacci_one_term():
    """Test generating Fibonacci sequence with 1 term."""
    assert fibonacci_recursive(1) == [0]

def test_fibonacci_two_terms():
    """Test generating Fibonacci sequence with 2 terms."""
    assert fibonacci_recursive(2) == [0, 1]

def test_fibonacci_multiple_terms():
    """Test generating Fibonacci sequence with multiple terms."""
    assert fibonacci_recursive(6) == [0, 1, 1, 2, 3, 5]

def test_fibonacci_negative_input():
    """Test that a negative input raises a ValueError."""
    with pytest.raises(ValueError, match="Number of terms must be non-negative"):
        fibonacci_recursive(-1)