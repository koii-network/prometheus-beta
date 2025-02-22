import pytest
from src.fibonacci_subsequence import generate_fibonacci_subsequence

def test_generate_fibonacci_subsequence_basic():
    # Test a few known cases
    assert generate_fibonacci_subsequence(0) == [0]
    assert generate_fibonacci_subsequence(2) == [0, 1, 1]
    assert generate_fibonacci_subsequence(5) == [0, 1, 1, 2, 3]

def test_generate_fibonacci_subsequence_larger_values():
    # Test some larger values
    result = generate_fibonacci_subsequence(10)
    assert sum(result[::2]) == 10
    
    result = generate_fibonacci_subsequence(20)
    assert sum(result[::2]) == 20

def test_generate_fibonacci_subsequence_edge_cases():
    # Test error cases
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        generate_fibonacci_subsequence(-1)
    
    with pytest.raises(ValueError, match="No Fibonacci subsequence found"):
        generate_fibonacci_subsequence(1000000)  # An extremely large value

def test_subsequence_properties():
    # Verify Fibonacci sequence properties
    for target in range(0, 50, 5):
        result = generate_fibonacci_subsequence(target)
        
        # Check Fibonacci property
        for i in range(2, len(result)):
            assert result[i] == result[i-1] + result[i-2]
        
        # Check even-indexed sum
        assert sum(result[::2]) == target