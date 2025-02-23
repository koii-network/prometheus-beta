import pytest
from src.fibonacci import fibonacci_recursive

def test_fibonacci_zero_terms():
    """Test generating Fibonacci sequence with 0 terms."""
    assert fibonacci_recursive(0) == []

def test_fibonacci_one_term():
    """Test generating Fibonacci sequence with 1 term."""
    assert fibonacci_recursive(1) == [0]

def test_fibonacci_multiple_terms():
    """Test generating Fibonacci sequence with multiple terms."""
    assert fibonacci_recursive(5) == [0, 1, 1, 2, 3]
    assert fibonacci_recursive(7) == [0, 1, 1, 2, 3, 5, 8]

def test_fibonacci_large_sequence():
    """Test generating a larger Fibonacci sequence."""
    result = fibonacci_recursive(10)
    assert len(result) == 10
    assert result == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def test_fibonacci_negative_input():
    """Test that a negative input raises a ValueError."""
    with pytest.raises(ValueError, match="Number of terms must be non-negative"):
        fibonacci_recursive(-1)