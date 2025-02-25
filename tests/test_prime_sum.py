import pytest
from src.prime_sum import sum_primes_under_n

def test_sum_primes_under_n_basic():
    """Test basic functionality of sum_primes_under_n."""
    assert sum_primes_under_n(10) == 17  # 2 + 3 + 5 + 7

def test_sum_primes_under_n_small_numbers():
    """Test edge cases with small numbers."""
    assert sum_primes_under_n(2) == 0  # No primes less than 2
    assert sum_primes_under_n(1) == 0  # No primes less than 1

def test_sum_primes_under_n_larger_number():
    """Test sum of primes for a larger number."""
    assert sum_primes_under_n(20) == 77  # 2 + 3 + 5 + 7 + 11 + 13 + 17 + 19

def test_sum_primes_under_n_invalid_input():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError):
        sum_primes_under_n("not a number")
    
    with pytest.raises(TypeError):
        sum_primes_under_n(3.14)

def test_sum_primes_under_n_zero_and_negative():
    """Test behavior with zero and negative numbers."""
    assert sum_primes_under_n(0) == 0
    assert sum_primes_under_n(-5) == 0