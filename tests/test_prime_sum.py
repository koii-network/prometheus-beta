import pytest
from src.prime_sum import sum_of_primes

def test_sum_of_primes_basic():
    """Test basic functionality for small numbers."""
    assert sum_of_primes(10) == 17  # 2 + 3 + 5 + 7 = 17
    assert sum_of_primes(20) == 77  # 2 + 3 + 5 + 7 + 11 + 13 + 17 + 19 = 77

def test_sum_of_primes_small_numbers():
    """Test edge cases with small numbers."""
    assert sum_of_primes(2) == 2
    assert sum_of_primes(3) == 5
    assert sum_of_primes(7) == 17

def test_sum_of_primes_larger_number():
    """Test a larger number to ensure correct calculation."""
    assert sum_of_primes(30) == 129  # 2 + 3 + 5 + 7 + 11 + 13 + 17 + 19 + 23 + 29 = 129

def test_sum_of_primes_invalid_inputs():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be 2 or greater"):
        sum_of_primes(1)
    
    with pytest.raises(ValueError, match="Input must be 2 or greater"):
        sum_of_primes(0)
    
    with pytest.raises(ValueError, match="Input must be 2 or greater"):
        sum_of_primes(-5)

def test_sum_of_primes_type_error():
    """Test type checking for non-integer inputs."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_of_primes(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_of_primes("10")
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_of_primes(None)