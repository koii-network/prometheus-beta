import pytest
from src.prime_sum import sum_of_primes

def test_sum_of_primes_basic():
    """Test basic functionality with small numbers."""
    assert sum_of_primes(10) == 17  # 2 + 3 + 5 + 7
    assert sum_of_primes(20) == 77  # 2 + 3 + 5 + 7 + 11 + 13 + 17 + 19

def test_sum_of_primes_edge_cases():
    """Test edge cases and boundary conditions."""
    assert sum_of_primes(2) == 2  # Smallest prime
    
    with pytest.raises(ValueError, match="Input must be 2 or greater"):
        sum_of_primes(1)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_of_primes(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_of_primes("10")

def test_sum_of_primes_larger_numbers():
    """Test with larger numbers to ensure correctness."""
    assert sum_of_primes(30) == 129  # Sum of primes up to 30
    assert sum_of_primes(50) == 328  # Sum of primes up to 50