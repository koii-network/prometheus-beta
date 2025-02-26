import pytest
from src.largest_prime_factor import find_largest_prime_factor

def test_simple_cases():
    """Test simple known cases of largest prime factor."""
    assert find_largest_prime_factor(13195) == 29
    assert find_largest_prime_factor(15) == 5
    assert find_largest_prime_factor(7) == 7

def test_large_number():
    """Test a large number case."""
    assert find_largest_prime_factor(600851475143) == 6857

def test_prime_number():
    """Test that a prime number returns itself."""
    assert find_largest_prime_factor(17) == 17
    assert find_largest_prime_factor(97) == 97

def test_even_number():
    """Test an even number with prime factors."""
    assert find_largest_prime_factor(24) == 3

def test_invalid_inputs():
    """Test error handling for invalid inputs."""
    # Less than or equal to 1
    with pytest.raises(ValueError, match="Input must be a positive integer greater than 1"):
        find_largest_prime_factor(1)
    
    with pytest.raises(ValueError, match="Input must be a positive integer greater than 1"):
        find_largest_prime_factor(0)
    
    # Negative number
    with pytest.raises(ValueError, match="Input must be a positive integer greater than 1"):
        find_largest_prime_factor(-10)
    
    # Non-integer input
    with pytest.raises(TypeError, match="Input must be an integer"):
        find_largest_prime_factor(10.5)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        find_largest_prime_factor("123")