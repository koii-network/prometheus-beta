import pytest
from src.prime_sum import sum_primes_under_n

def test_small_n():
    # Sum of primes less than 10 = 2 + 3 + 5 + 7 = 17
    assert sum_primes_under_n(10) == 17

def test_large_n():
    # Sum of primes less than 20 = 2 + 3 + 5 + 7 + 11 + 13 + 17 + 19 = 77
    assert sum_primes_under_n(20) == 77

def test_n_less_than_two():
    # Test that n must be greater than 1
    with pytest.raises(ValueError, match="Input must be a positive integer greater than 1"):
        sum_primes_under_n(1)

def test_n_zero():
    # Test that n must be greater than 1
    with pytest.raises(ValueError, match="Input must be a positive integer greater than 1"):
        sum_primes_under_n(0)

def test_n_negative():
    # Test that n must be greater than 1
    with pytest.raises(ValueError, match="Input must be a positive integer greater than 1"):
        sum_primes_under_n(-5)

def test_n_float():
    # Test that n must be an integer
    with pytest.raises(ValueError, match="Input must be a positive integer greater than 1"):
        sum_primes_under_n(10.5)

def test_n_string():
    # Test that n must be an integer
    with pytest.raises(ValueError, match="Input must be a positive integer greater than 1"):
        sum_primes_under_n("10")

def test_primes_under_2():
    # No primes less than 2
    assert sum_primes_under_n(2) == 0