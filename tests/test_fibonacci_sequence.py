import pytest
from src.fibonacci_sequence import fibonacci_sequence

def test_fibonacci_sequence_basic():
    """Test basic Fibonacci sequence generation."""
    assert fibonacci_sequence(0) == []
    assert fibonacci_sequence(1) == [0]
    assert fibonacci_sequence(2) == [0, 1]
    assert fibonacci_sequence(5) == [0, 1, 1, 2, 3]
    assert fibonacci_sequence(7) == [0, 1, 1, 2, 3, 5, 8]

def test_fibonacci_sequence_edge_cases():
    """Test edge cases for Fibonacci sequence generation."""
    # Empty sequence
    assert fibonacci_sequence(0) == []
    
    # First few numbers of the sequence
    assert fibonacci_sequence(3) == [0, 1, 1]

def test_fibonacci_sequence_large_n():
    """Test Fibonacci sequence generation with larger n."""
    # Verify length of sequence
    assert len(fibonacci_sequence(10)) == 10
    
    # Verify some specific values in a larger sequence
    sequence = fibonacci_sequence(10)
    assert sequence[9] == 34

def test_fibonacci_sequence_negative_input():
    """Test that negative input raises a ValueError."""
    with pytest.raises(ValueError, match="n must be a non-negative integer"):
        fibonacci_sequence(-1)
    
    with pytest.raises(ValueError, match="n must be a non-negative integer"):
        fibonacci_sequence(-100)