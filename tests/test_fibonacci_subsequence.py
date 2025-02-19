import pytest
from src.fibonacci_subsequence import fibonacci_subsequence

def test_fibonacci_subsequence_length_1():
    """Test Fibonacci subsequence of length 1."""
    assert fibonacci_subsequence(1) == [0]

def test_fibonacci_subsequence_length_2():
    """Test Fibonacci subsequence of length 2."""
    assert fibonacci_subsequence(2) == [0, 1]

def test_fibonacci_subsequence_length_5():
    """Test Fibonacci subsequence of length 5."""
    assert fibonacci_subsequence(5) == [0, 1, 1, 2, 3]

def test_fibonacci_subsequence_length_7():
    """Test Fibonacci subsequence of length 7."""
    assert fibonacci_subsequence(7) == [0, 1, 1, 2, 3, 5, 8]

def test_fibonacci_subsequence_invalid_input():
    """Test that an error is raised for non-positive inputs."""
    with pytest.raises(ValueError, match="Subsequence length must be a positive integer"):
        fibonacci_subsequence(0)
    
    with pytest.raises(ValueError, match="Subsequence length must be a positive integer"):
        fibonacci_subsequence(-1)