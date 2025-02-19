import pytest
from src.fibonacci_subsequence import fibonacci_subsequence

def test_fibonacci_subsequence_zero_length():
    """Test generating a Fibonacci subsequence of length 0."""
    assert fibonacci_subsequence(0) == []

def test_fibonacci_subsequence_one_element():
    """Test generating a Fibonacci subsequence of length 1."""
    assert fibonacci_subsequence(1) == [0]

def test_fibonacci_subsequence_two_elements():
    """Test generating a Fibonacci subsequence of length 2."""
    assert fibonacci_subsequence(2) == [0, 1]

def test_fibonacci_subsequence_longer_sequence():
    """Test generating a Fibonacci subsequence of length 6."""
    assert fibonacci_subsequence(6) == [0, 1, 1, 2, 3, 5]

def test_fibonacci_subsequence_negative_input():
    """Test that a negative input raises a ValueError."""
    with pytest.raises(ValueError, match="Length of subsequence must be non-negative"):
        fibonacci_subsequence(-1)

def test_fibonacci_subsequence_large_sequence():
    """Test generating a larger Fibonacci subsequence."""
    result = fibonacci_subsequence(10)
    assert len(result) == 10
    # Verify Fibonacci property
    for i in range(2, len(result)):
        assert result[i] == result[i-1] + result[i-2]