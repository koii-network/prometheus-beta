import pytest
from src.sieve_of_eratosthenes import sieve_of_eratosthenes

def test_basic_prime_generation():
    """Test basic prime number generation"""
    assert sieve_of_eratosthenes(10) == [2, 3, 5, 7]

def test_larger_number():
    """Test prime generation for a larger number"""
    assert sieve_of_eratosthenes(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def test_minimum_value():
    """Test that the minimum valid input works correctly"""
    assert sieve_of_eratosthenes(2) == [2]

def test_invalid_input_low():
    """Test that input less than 2 raises a ValueError"""
    with pytest.raises(ValueError, match="Input must be at least 2"):
        sieve_of_eratosthenes(1)

def test_invalid_input_type():
    """Test that non-integer input raises a TypeError"""
    with pytest.raises(TypeError, match="Input must be an integer"):
        sieve_of_eratosthenes("10")
    with pytest.raises(TypeError, match="Input must be an integer"):
        sieve_of_eratosthenes(10.5)

def test_large_input():
    """Test that the function works with a large input"""
    primes = sieve_of_eratosthenes(100)
    assert len(primes) > 0
    assert all(is_prime(p) for p in primes)
    assert primes[0] == 2
    assert primes[-1] <= 100

def is_prime(n):
    """Helper function to verify primality"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True