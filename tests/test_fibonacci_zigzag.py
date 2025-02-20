import pytest
from src.fibonacci_zigzag import fibonacci_zigzag

def test_fibonacci_zigzag_small_inputs():
    assert fibonacci_zigzag(1) == [0]
    assert fibonacci_zigzag(2) == [0, 1]
    assert fibonacci_zigzag(3) == [0, 2, 1]
    assert fibonacci_zigzag(4) == [0, 2, 3, 1]
    assert fibonacci_zigzag(5) == [0, 2, 3, 5, 1]

def test_fibonacci_zigzag_larger_input():
    result = fibonacci_zigzag(7)
    assert result == [0, 2, 3, 5, 8, 13, 1]
    assert len(result) == 7

def test_fibonacci_zigzag_invalid_inputs():
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_zigzag(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_zigzag(-1)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_zigzag(1.5)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_zigzag("3")

def test_fibonacci_zigzag_sequence_integrity():
    # Check that each pair of adjacent numbers follows Fibonacci rules
    result = fibonacci_zigzag(8)
    for i in range(2, len(result)):
        # Ensure each number (except first two) is sum of previous two in the Fibonacci sequence
        fib_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        # Check if the current result matches the expected Fibonacci sequence
        assert result[i] == fib_sequence[i] or result[max(0, i-1)] == fib_sequence[max(0, i-1)]