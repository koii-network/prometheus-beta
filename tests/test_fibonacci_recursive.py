import pytest
from src.fibonacci_recursive import fibonacci_recursive

def test_fibonacci_recursive_zero_terms():
    """Test generating Fibonacci sequence with 0 terms."""
    assert fibonacci_recursive(0) == []

def test_fibonacci_recursive_one_term():
    """Test generating Fibonacci sequence with 1 term."""
    assert fibonacci_recursive(1) == [0]

def test_fibonacci_recursive_two_terms():
    """Test generating Fibonacci sequence with 2 terms."""
    assert fibonacci_recursive(2) == [0, 1]

def test_fibonacci_recursive_multiple_terms():
    """Test generating Fibonacci sequence with multiple terms."""
    assert fibonacci_recursive(6) == [0, 1, 1, 2, 3, 5]

def test_fibonacci_recursive_negative_input():
    """Test that a negative input raises a ValueError."""
    with pytest.raises(ValueError, match="Number of terms must be a non-negative integer"):
        fibonacci_recursive(-1)

def test_fibonacci_recursive_large_input():
    """Test generating Fibonacci sequence with a larger number of terms."""
    result = fibonacci_recursive(10)
    assert len(result) == 10
    assert result == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]