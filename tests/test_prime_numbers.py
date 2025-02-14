import pytest
from src.prime_numbers import get_primes_to_100

def test_get_primes_to_100():
    # Expected list of prime numbers from 1 to 100
    expected_primes = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
        31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 
        73, 79, 83, 89, 97
    ]
    
    # Get the primes from the function
    result_primes = get_primes_to_100()
    
    # Check that the result matches the expected primes
    assert result_primes == expected_primes, "List of primes does not match expected values"

def test_primes_properties():
    primes = get_primes_to_100()
    
    # Verify that each number in the list is prime
    for prime in primes:
        # A prime number should only be divisible by 1 and itself
        assert all(prime % i != 0 for i in range(2, int(prime**0.5) + 1)), \
            f"{prime} is not a prime number"

def test_primes_range():
    primes = get_primes_to_100()
    
    # Verify all primes are within the range 1-100
    assert all(2 <= prime <= 100 for prime in primes), \
        "Primes outside the range 1-100 found"

def test_prime_count():
    primes = get_primes_to_100()
    
    # Verify the correct number of primes
    assert len(primes) == 25, "Incorrect number of prime numbers found"