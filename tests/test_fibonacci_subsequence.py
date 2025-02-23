import pytest
from src.fibonacci_subsequence import generate_fibonacci_subsequence

def test_generate_fibonacci_subsequence_basic():
    # Basic test cases with various inputs
    assert generate_fibonacci_subsequence(0) == [0]
    assert generate_fibonacci_subsequence(1) == [1, 0]
    assert generate_fibonacci_subsequence(2) == [2, 0]
    
    # Validate sum of even-indexed numbers
    for n in range(10):
        result = generate_fibonacci_subsequence(n)
        assert sum(result[j] for j in range(len(result)) if j % 2 == 0) == n

def test_generate_fibonacci_subsequence_more_complex():
    # More complex test cases
    for n in range(15):
        result = generate_fibonacci_subsequence(n)
        even_sum = sum(result[j] for j in range(len(result)) if j % 2 == 0)
        assert even_sum == n

def test_generate_fibonacci_subsequence_error_cases():
    # Error case tests
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        generate_fibonacci_subsequence(-1)
    
    # Validate error for very large numbers
    with pytest.raises(ValueError):
        generate_fibonacci_subsequence(10**6)

def test_generate_fibonacci_subsequence_validation():
    # Validate the generated subsequence properties
    for n in range(15):
        result = generate_fibonacci_subsequence(n)
        
        # Check even-indexed sum
        assert sum(result[j] for j in range(len(result)) if j % 2 == 0) == n
        
        # Ensure length is at least 2
        assert len(result) >= 2

def test_generate_fibonacci_subsequence_edge_cases():
    # Edge case tests
    result = generate_fibonacci_subsequence(0)
    assert result == [0]
    
    result = generate_fibonacci_subsequence(1)
    assert result == [1, 0]