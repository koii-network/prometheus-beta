import pytest
from src.fibonacci import generate_fibonacci

def test_fibonacci_zero_terms():
    """Test generating Fibonacci sequence with zero terms."""
    assert generate_fibonacci(0) == []

def test_fibonacci_one_term():
    """Test generating Fibonacci sequence with one term."""
    assert generate_fibonacci(1) == [0]

def test_fibonacci_two_terms():
    """Test generating Fibonacci sequence with two terms."""
    assert generate_fibonacci(2) == [0, 1]

def test_fibonacci_multiple_terms():
    """Test generating Fibonacci sequence with multiple terms."""
    assert generate_fibonacci(6) == [0, 1, 1, 2, 3, 5]

def test_fibonacci_ten_terms():
    """Test generating Fibonacci sequence with ten terms."""
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert generate_fibonacci(10) == expected

def test_fibonacci_negative_input():
    """Test that negative input raises a ValueError."""
    with pytest.raises(ValueError, match="Number of terms must be non-negative"):
        generate_fibonacci(-1)

def test_fibonacci_non_integer_input():
    """Test that non-integer input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_fibonacci(3.14)
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_fibonacci("5")