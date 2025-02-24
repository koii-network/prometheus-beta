import pytest
from src.fibonacci import fibonacci_sequence

def test_fibonacci_sequence_basic():
    """Test basic Fibonacci sequence generation."""
    assert fibonacci_sequence(0) == []
    assert fibonacci_sequence(1) == [0]
    assert fibonacci_sequence(2) == [0, 1]
    assert fibonacci_sequence(5) == [0, 1, 1, 2, 3]
    assert fibonacci_sequence(7) == [0, 1, 1, 2, 3, 5, 8]

def test_fibonacci_sequence_larger_n():
    """Test Fibonacci sequence for larger n."""
    sequence = fibonacci_sequence(10)
    assert len(sequence) == 10
    assert sequence == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def test_fibonacci_sequence_negative_input():
    """Test that negative input raises a ValueError."""
    with pytest.raises(ValueError, match="n must be a non-negative integer"):
        fibonacci_sequence(-1)

def test_fibonacci_sequence_type_input():
    """Test that non-integer input raises a TypeError."""
    with pytest.raises(TypeError):
        fibonacci_sequence(3.14)
    with pytest.raises(TypeError):
        fibonacci_sequence("5")

def test_fibonacci_sequence_large_input():
    """Test Fibonacci sequence for a larger input to verify performance."""
    sequence = fibonacci_sequence(20)
    assert len(sequence) == 20
    # Verify the last few numbers in the sequence
    assert sequence[-3:] == [1597, 2584, 4181]