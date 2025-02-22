import pytest
from src.prime_sum import sum_of_primes

def test_sum_of_primes_basic():
    """Test basic prime sum calculation."""
    assert sum_of_primes(10) == 17  # 2 + 3 + 5 + 7 = 17
    assert sum_of_primes(20) == 77  # 2 + 3 + 5 + 7 + 11 + 13 + 17 + 19 = 77

def test_sum_of_primes_edge_cases():
    """Test edge cases."""
    assert sum_of_primes(2) == 2  # Lowest prime number
    assert sum_of_primes(3) == 5  # 2 + 3
    
def test_sum_of_primes_error_handling():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be at least 2"):
        sum_of_primes(1)
    
    with pytest.raises(ValueError, match="Input must be at least 2"):
        sum_of_primes(0)
    
    with pytest.raises(ValueError, match="Input must be at least 2"):
        sum_of_primes(-5)
    
def test_sum_of_primes_type_error():
    """Test type error handling."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_of_primes(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_of_primes("10")
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_of_primes(None)