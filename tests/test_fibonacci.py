import pytest
from src.fibonacci import fibonacci_sequence

def test_fibonacci_sequence_zero():
    """Test generating 0 Fibonacci sequence elements."""
    assert fibonacci_sequence(0) == []

def test_fibonacci_sequence_one():
    """Test generating 1 Fibonacci sequence element."""
    assert fibonacci_sequence(1) == [0]

def test_fibonacci_sequence_two():
    """Test generating 2 Fibonacci sequence elements."""
    assert fibonacci_sequence(2) == [0, 1]

def test_fibonacci_sequence_multiple():
    """Test generating multiple Fibonacci sequence elements."""
    assert fibonacci_sequence(6) == [0, 1, 1, 2, 3, 5]

def test_fibonacci_sequence_ten():
    """Test a larger sequence of Fibonacci numbers."""
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert fibonacci_sequence(10) == expected

def test_fibonacci_sequence_negative():
    """Test that a negative input raises a ValueError."""
    with pytest.raises(ValueError, match="n must be a non-negative integer"):
        fibonacci_sequence(-1)

def test_fibonacci_sequence_large():
    """Test generating a relatively large Fibonacci sequence."""
    sequence = fibonacci_sequence(20)
    assert len(sequence) == 20
    
    # Verify that each number (after the first two) is the sum of the previous two
    for i in range(2, len(sequence)):
        assert sequence[i] == sequence[i-1] + sequence[i-2]