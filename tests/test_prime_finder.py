import pytest
from src.prime_finder import find_primes

def test_prime_numbers_between_2_and_100():
    """Test that all prime numbers between 2 and 100 are found correctly."""
    expected_primes = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 
        53, 59, 61, 67, 71, 73, 79, 83, 89, 97
    ]
    assert find_primes() == expected_primes

def test_prime_numbers_with_different_limit():
    """Test prime number finding with a different limit."""
    assert find_primes(20) == [2, 3, 5, 7, 11, 13, 17, 19]

def test_primes_with_lower_limit():
    """Test prime number finding with limits less than 2."""
    assert find_primes(1) == []
    assert find_primes(0) == []
    assert find_primes(-5) == []

def test_prime_numbers_are_unique():
    """Ensure no duplicate prime numbers are returned."""
    primes = find_primes()
    assert len(primes) == len(set(primes))

def test_prime_numbers_are_sorted():
    """Ensure prime numbers are returned in ascending order."""
    primes = find_primes()
    assert primes == sorted(primes)