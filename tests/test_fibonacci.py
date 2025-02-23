import pytest
from src.fibonacci import generate_fibonacci_sequence

def test_fibonacci_zero_terms():
    """Test generating Fibonacci sequence with 0 terms."""
    assert generate_fibonacci_sequence(0) == []

def test_fibonacci_one_term():
    """Test generating Fibonacci sequence with 1 term."""
    assert generate_fibonacci_sequence(1) == [0]

def test_fibonacci_two_terms():
    """Test generating Fibonacci sequence with 2 terms."""
    assert generate_fibonacci_sequence(2) == [0, 1]

def test_fibonacci_multiple_terms():
    """Test generating Fibonacci sequence with multiple terms."""
    assert generate_fibonacci_sequence(5) == [0, 1, 1, 2, 3]
    assert generate_fibonacci_sequence(7) == [0, 1, 1, 2, 3, 5, 8]

def test_fibonacci_negative_input():
    """Test that a negative input raises a ValueError."""
    with pytest.raises(ValueError, match="Number of terms must be non-negative"):
        generate_fibonacci_sequence(-1)

def test_fibonacci_invalid_input_type():
    """Test that non-integer input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_fibonacci_sequence(3.14)
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_fibonacci_sequence("5")
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_fibonacci_sequence(None)