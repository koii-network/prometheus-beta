import pytest
from src.fibonacci_subsequence import generate_fibonacci_subsequence

def test_generate_fibonacci_subsequence_zero():
    """Test subsequence generation for n = 0"""
    assert generate_fibonacci_subsequence(0) == [0]

def test_generate_fibonacci_subsequence_specific_cases():
    """Test some known cases of subsequence generation"""
    # Test cases with different even-indexed sums
    assert generate_fibonacci_subsequence(2) == [0, 1, 1, 2]
    assert generate_fibonacci_subsequence(5) == [0, 1, 1, 2, 3, 5]

def test_generate_fibonacci_subsequence_larger_sum():
    """Test subsequence generation with larger sums"""
    subsequence = generate_fibonacci_subsequence(10)
    # Verify even-indexed sum
    assert sum(subsequence[::2]) == 10
    # Verify it's a Fibonacci-like sequence
    for i in range(2, len(subsequence)):
        assert subsequence[i] == subsequence[i-1] + subsequence[i-2]

def test_generate_fibonacci_subsequence_invalid_sum():
    """Test that an exception is raised for impossible sums"""
    with pytest.raises(ValueError):
        generate_fibonacci_subsequence(10000)  # Extremely large sum

def test_subsequence_properties():
    """Verify general properties of the generated subsequence"""
    for n in range(1, 20):
        subsequence = generate_fibonacci_subsequence(n)
        # Check that even-indexed sum matches
        assert sum(subsequence[::2]) == n
        # Check Fibonacci property
        for i in range(2, len(subsequence)):
            assert subsequence[i] == subsequence[i-1] + subsequence[i-2]