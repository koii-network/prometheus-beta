import pytest
from src.largest_prime_factor import find_largest_prime_factor

def test_basic_cases():
    """Test basic scenarios with known inputs."""
    assert find_largest_prime_factor(13195) == 29
    assert find_largest_prime_factor(600851475143) == 6857
    assert find_largest_prime_factor(17) == 17

def test_prime_number():
    """Test when input is a prime number."""
    assert find_largest_prime_factor(17) == 17
    assert find_largest_prime_factor(97) == 97

def test_even_number():
    """Test with even numbers."""
    assert find_largest_prime_factor(100) == 5
    assert find_largest_prime_factor(2) == 2

def test_large_number():
    """Test with larger numbers."""
    assert find_largest_prime_factor(1000000007) == 1000000007  # Prime number
    assert find_largest_prime_factor(123456789) == 3803

def test_invalid_inputs():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError):
        find_largest_prime_factor("not a number")
    
    with pytest.raises(TypeError):
        find_largest_prime_factor(3.14)
    
    with pytest.raises(ValueError):
        find_largest_prime_factor(1)
    
    with pytest.raises(ValueError):
        find_largest_prime_factor(0)
    
    with pytest.raises(ValueError):
        find_largest_prime_factor(-10)