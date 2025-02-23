import pytest
from src.prime_sum import sum_primes_under_n

def test_sum_primes_under_n_basic():
    """Test basic functionality with small numbers."""
    assert sum_primes_under_n(10) == 17  # 2 + 3 + 5 + 7

def test_sum_primes_under_n_small_numbers():
    """Test edge cases with small numbers."""
    assert sum_primes_under_n(2) == 0
    assert sum_primes_under_n(1) == 0

def test_sum_primes_under_n_larger_number():
    """Test with a larger number."""
    assert sum_primes_under_n(20) == 77  # 2 + 3 + 5 + 7 + 11 + 13 + 17 + 19

def test_sum_primes_under_n_invalid_input():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be an integer"):
        sum_primes_under_n(3.14)
    
    with pytest.raises(ValueError, match="Input must be an integer"):
        sum_primes_under_n("10")

def test_sum_primes_under_n_zero_and_negative():
    """Test behavior with zero and negative numbers."""
    assert sum_primes_under_n(0) == 0
    assert sum_primes_under_n(-5) == 0