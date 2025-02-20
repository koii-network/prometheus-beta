import pytest
from src.fibonacci_subsequence import generate_fibonacci_subsequence

def test_generate_fibonacci_subsequence_basic_cases():
    # Test zero case
    assert generate_fibonacci_subsequence(0) == [0]
    
    # Test small positive cases
    assert generate_fibonacci_subsequence(1) == [1, 1]
    
def test_generate_fibonacci_subsequence_various_sums():
    # Test various sum cases
    cases = [
        2,   # Simple case
        4,   # Another simple case
        10,  # More complex case
        20   # Even more complex case
    ]
    
    for n in cases:
        subsequence = generate_fibonacci_subsequence(n)
        
        # Verify key properties
        assert len(subsequence) > 1
        assert sum(subsequence[::2]) == n, f"Failed for n = {n}"
        
        # Ensure it follows Fibonacci generation rules
        for i in range(2, len(subsequence)):
            assert subsequence[i] == subsequence[i-1] + subsequence[i-2]

def test_generate_fibonacci_subsequence_error_cases():
    # Test cases where no subsequence should exist (very large numbers)
    with pytest.raises(ValueError):
        generate_fibonacci_subsequence(10000)

def test_fibonacci_subsequence_properties():
    # Comprehensive test of generated subsequence
    n = 15
    subsequence = generate_fibonacci_subsequence(n)
    
    # Check sum of even-indexed numbers
    assert sum(subsequence[::2]) == n
    
    # Ensure Fibonacci property
    for i in range(2, len(subsequence)):
        assert subsequence[i] == subsequence[i-1] + subsequence[i-2]