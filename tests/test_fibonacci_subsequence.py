import pytest
from src.fibonacci_subsequence import generate_fibonacci_subsequence

def test_fibonacci_subsequence_basic():
    """Test basic functionality of Fibonacci subsequence generation."""
    assert generate_fibonacci_subsequence(5) == [0, 1, 1, 2, 3]
    assert generate_fibonacci_subsequence(7) == [0, 1, 1, 2, 3, 5, 8]

def test_fibonacci_subsequence_edge_cases():
    """Test edge cases for Fibonacci subsequence generation."""
    # Zero length
    assert generate_fibonacci_subsequence(0) == []
    
    # Single element
    assert generate_fibonacci_subsequence(1) == [0]
    
    # Two elements
    assert generate_fibonacci_subsequence(2) == [0, 1]

def test_fibonacci_subsequence_invalid_inputs():
    """Test error handling for invalid inputs."""
    # Negative input
    with pytest.raises(ValueError, match="Length of subsequence must be non-negative"):
        generate_fibonacci_subsequence(-1)
    
    # Non-integer input
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_fibonacci_subsequence(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_fibonacci_subsequence("5")

def test_fibonacci_subsequence_large_input():
    """Test generation of a larger Fibonacci subsequence."""
    result = generate_fibonacci_subsequence(10)
    assert len(result) == 10
    assert result == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]