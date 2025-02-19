import pytest
from src.fibonacci_subsequence import fibonacci_subsequence

def test_fibonacci_subsequence_basic():
    """Test basic functionality of Fibonacci subsequence generation."""
    assert fibonacci_subsequence(1) == [0]
    assert fibonacci_subsequence(2) == [0, 1]
    assert fibonacci_subsequence(5) == [0, 1, 1, 2, 3]
    assert fibonacci_subsequence(7) == [0, 1, 1, 2, 3, 5, 8]

def test_fibonacci_subsequence_error_handling():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Subsequence length must be at least 1"):
        fibonacci_subsequence(0)
    
    with pytest.raises(ValueError, match="Subsequence length must be at least 1"):
        fibonacci_subsequence(-1)

def test_fibonacci_subsequence_larger_sequence():
    """Test generation of a larger Fibonacci subsequence."""
    result = fibonacci_subsequence(10)
    assert len(result) == 10
    
    # Verify the Fibonacci property
    for i in range(2, len(result)):
        assert result[i] == result[i-1] + result[i-2]