import pytest
from src.prime_filter import is_prime, filter_primes

def test_is_prime():
    # Test positive prime numbers
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(17) == True
    assert is_prime(29) == True
    
    # Test non-prime positive numbers
    assert is_prime(1) == False
    assert is_prime(4) == False
    assert is_prime(15) == False
    assert is_prime(25) == False
    
    # Test zero and negative numbers
    assert is_prime(0) == False
    assert is_prime(1) == False
    assert is_prime(-2) == False
    assert is_prime(-17) == False

def test_filter_primes():
    # Test with a mix of prime and non-prime numbers
    assert filter_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 3, 5, 7]
    
    # Test with negative numbers
    assert filter_primes([-3, -2, -1, 0, 1, 2, 3, 4, 5]) == [2, 3, 5]
    
    # Test with an empty list
    assert filter_primes([]) == []
    
    # Test with only non-prime numbers
    assert filter_primes([1, 4, 6, 8, 9, 10]) == []
    
    # Test with only prime numbers
    assert filter_primes([2, 3, 5, 7, 11, 13]) == [2, 3, 5, 7, 11, 13]

def test_large_primes():
    # Test with larger prime numbers
    assert is_prime(97) == True
    assert is_prime(541) == True
    
    # Test with larger non-prime numbers
    assert is_prime(100) == False
    assert is_prime(567) == False