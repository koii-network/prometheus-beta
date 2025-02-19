import pytest
from src.prime_sum import sum_primes_under_n

def test_sum_primes_under_small_n():
    """Test sum of primes for a small number"""
    assert sum_primes_under_n(10) == 17  # 2 + 3 + 5 + 7

def test_sum_primes_under_larger_n():
    """Test sum of primes for a larger number"""
    assert sum_primes_under_n(20) == 77  # 2 + 3 + 5 + 7 + 11 + 13 + 17 + 19

def test_sum_primes_under_low_prime():
    """Test sum of primes for the smallest prime"""
    assert sum_primes_under_n(3) == 2

def test_sum_primes_under_invalid_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError):
        sum_primes_under_n(1)
    
    with pytest.raises(ValueError):
        sum_primes_under_n(0)
    
    with pytest.raises(ValueError):
        sum_primes_under_n(-5)
    
    with pytest.raises(ValueError):
        sum_primes_under_n(2.5)
    
    with pytest.raises(ValueError):
        sum_primes_under_n("not a number")