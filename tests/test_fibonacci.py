import pytest
from src.fibonacci import fibonacci_recursive

def test_fibonacci_sequence():
    """Test basic Fibonacci sequence generation."""
    assert fibonacci_recursive(0) == []
    assert fibonacci_recursive(1) == [0]
    assert fibonacci_recursive(2) == [0, 1]
    assert fibonacci_recursive(5) == [0, 1, 1, 2, 3]
    assert fibonacci_recursive(7) == [0, 1, 1, 2, 3, 5, 8]

def test_fibonacci_large_sequence():
    """Test generation of a larger Fibonacci sequence."""
    result = fibonacci_recursive(10)
    assert len(result) == 10
    assert result == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def test_fibonacci_negative_input():
    """Test that a negative input raises a ValueError."""
    with pytest.raises(ValueError, match="Number of terms must be non-negative"):
        fibonacci_recursive(-1)