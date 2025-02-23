import pytest
from src.fibonacci_subsequence import generate_fibonacci_subsequence

def test_generate_fibonacci_subsequence_basic():
    # Basic test cases with various inputs
    assert generate_fibonacci_subsequence(0) == [0]
    assert generate_fibonacci_subsequence(1) == [1, 0]
    assert generate_fibonacci_subsequence(2) == [2, 0]
    assert generate_fibonacci_subsequence(5) == [5, 0, 2, 3]

def test_generate_fibonacci_subsequence_more_complex():
    # More complex test cases
    result = generate_fibonacci_subsequence(10)
    assert sum(result[j] for j in range(len(result)) if j % 2 == 0) == 10

def test_generate_fibonacci_subsequence_error_cases():
    # Error case tests
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        generate_fibonacci_subsequence(-1)
    
    # Test very large numbers or numbers that cannot be generated
    with pytest.raises(ValueError):
        generate_fibonacci_subsequence(10**6)

def test_generate_fibonacci_subsequence_validation():
    # Validate the generated subsequence properties
    for n in range(15):
        result = generate_fibonacci_subsequence(n)
        
        # Check even-indexed sum
        assert sum(result[j] for j in range(len(result)) if j % 2 == 0) == n
        
        # Validate Fibonacci-like sequence
        for i in range(2, len(result)):
            assert result[i] == result[i-1] + result[i-2]

def test_generate_fibonacci_subsequence_edge_cases():
    # Edge case tests
    result = generate_fibonacci_subsequence(0)
    assert result == [0]
    
    result = generate_fibonacci_subsequence(1)
    assert result == [1, 0]