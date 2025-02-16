import pytest
from src.prime_numbers import find_primes_to_100

def test_find_primes_to_100():
    # Get the list of primes
    primes = find_primes_to_100()
    
    # Expected list of primes from 1 to 100
    expected_primes = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
        31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 
        73, 79, 83, 89, 97
    ]
    
    # Check that the function returns the correct list of primes
    assert primes == expected_primes, f"Expected {expected_primes}, but got {primes}"
    
def test_primes_properties():
    primes = find_primes_to_100()
    
    # Verify each number is prime
    for prime in primes:
        # A prime number should have exactly two factors: 1 and itself
        factors = [i for i in range(1, prime + 1) if prime % i == 0]
        assert len(factors) == 2, f"{prime} should have exactly 2 factors"
        assert factors == [1, prime], f"{prime} is not a prime number"
    
def test_primes_range():
    primes = find_primes_to_100()
    
    # Verify all primes are within the range 1-100
    assert all(2 <= prime <= 100 for prime in primes), "All primes should be between 2 and 100"
    
def test_primes_count():
    primes = find_primes_to_100()
    
    # The number of primes from 1 to 100 should be 25
    assert len(primes) == 25, f"Expected 25 primes, but got {len(primes)}"