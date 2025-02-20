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
    """Test Fibonacci sequence generation for larger values of n."""
    seq_10 = fibonacci_sequence(10)
    assert len(seq_10) == 10
    assert seq_10 == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def test_fibonacci_sequence_negative_input():
    """Test that negative inputs raise a ValueError."""
    with pytest.raises(ValueError, match="n must be a non-negative integer"):
        fibonacci_sequence(-1)

def test_fibonacci_sequence_large_n():
    """Test Fibonacci sequence generation for a relatively large value of n."""
    seq_20 = fibonacci_sequence(20)
    assert len(seq_20) == 20
    
    # Verify sequence generation without explicitly checking every number
    for i in range(2, len(seq_20)):
        assert seq_20[i] == seq_20[i-1] + seq_20[i-2]