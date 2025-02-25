import pytest
from src.prime_numbers import get_primes_up_to_n

def test_primes_up_to_n():
    # Test base cases
    assert get_primes_up_to_n(1) == []
    assert get_primes_up_to_n(2) == [2]
    
    # Test first few prime numbers
    assert get_primes_up_to_n(10) == [2, 3, 5, 7]
    
    # Test full range of primes up to 100
    expected_primes_up_to_100 = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
        31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 
        73, 79, 83, 89, 97
    ]
    assert get_primes_up_to_n(100) == expected_primes_up_to_100
    
    # Test edge cases
    assert get_primes_up_to_n(0) == []
    assert get_primes_up_to_n(-5) == []

def test_prime_number_count():
    # Verify the correct count of prime numbers
    assert len(get_primes_up_to_n(100)) == 25

def test_large_input():
    # Test large input to ensure efficiency
    primes_large = get_primes_up_to_n(1000)
    assert primes_large[0] == 2
    assert primes_large[-1] == 997
    assert len(primes_large) == 168  # There are 168 primes <= 1000