import pytest
from src.fibonacci_subsequence import generate_fibonacci_subsequence

def test_generate_fibonacci_subsequence_zero():
    """Test generating subsequence for n=0"""
    result = generate_fibonacci_subsequence(0)
    assert result == [0]
    assert sum(result[::2]) == 0

def test_generate_fibonacci_subsequence_simple_cases():
    """Test some simple cases"""
    test_cases = [
        1,  # should return [0, 1, 1]
        2,  # should return [1, 1, 2]
        4,  # should find a valid subsequence
        10  # should find a valid subsequence
    ]
    
    for n in test_cases:
        result = generate_fibonacci_subsequence(n)
        # Verify key properties
        assert len(result) >= 2
        assert sum(result[::2]) == n
        
        # Verify Fibonacci property
        for i in range(2, len(result)):
            assert result[i] == result[i-1] + result[i-2]

def test_generate_fibonacci_subsequence_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        generate_fibonacci_subsequence(-1)

def test_generate_fibonacci_subsequence_large_n():
    """Test generating subsequence for a larger number"""
    n = 100
    result = generate_fibonacci_subsequence(n)
    assert sum(result[::2]) == n
    
    # Verify Fibonacci property
    for i in range(2, len(result)):
        assert result[i] == result[i-1] + result[i-2]

def test_no_subsequence_exists():
    """Verify that an appropriate error is raised if no subsequence can be found"""
    with pytest.raises(ValueError, match="No Fibonacci subsequence found"):
        generate_fibonacci_subsequence(1000000)  # An extremely large number