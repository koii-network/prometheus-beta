import pytest
from src.prime_numbers import generate_primes

def test_generate_primes_default():
    """Test default prime number generation (up to 100)"""
    primes = generate_primes()
    expected_primes = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
        31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 
        73, 79, 83, 89, 97
    ]
    assert primes == expected_primes

def test_generate_primes_small_range():
    """Test generating primes in a small range"""
    assert generate_primes(10) == [2, 3, 5, 7]

def test_generate_primes_lower_bound():
    """Test edge cases with lower bound"""
    assert generate_primes(1) == []
    assert generate_primes(0) == []
    assert generate_primes(-5) == []

def test_generate_primes_large_range():
    """Test generating primes in a larger range"""
    primes = generate_primes(200)
    assert len(primes) > 25  # more than the primes up to 100
    assert all(is_prime(p) for p in primes)

def is_prime(n):
    """Helper function to verify primality"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True