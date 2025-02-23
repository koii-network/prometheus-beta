import pytest
from src.largest_prime_factor import find_largest_prime_factor

def test_find_largest_prime_factor_small_numbers():
    assert find_largest_prime_factor(2) == 2
    assert find_largest_prime_factor(3) == 3
    assert find_largest_prime_factor(4) == 2
    assert find_largest_prime_factor(13) == 13
    assert find_largest_prime_factor(15) == 5

def test_find_largest_prime_factor_larger_numbers():
    assert find_largest_prime_factor(100) == 5
    assert find_largest_prime_factor(13195) == 29
    assert find_largest_prime_factor(600851475143) == 6857

def test_find_largest_prime_factor_prime_numbers():
    primes = [17, 19, 23, 29, 31, 37]
    for prime in primes:
        assert find_largest_prime_factor(prime) == prime

def test_find_largest_prime_factor_invalid_inputs():
    with pytest.raises(ValueError):
        find_largest_prime_factor(1)
    
    with pytest.raises(ValueError):
        find_largest_prime_factor(0)
    
    with pytest.raises(ValueError):
        find_largest_prime_factor(-5)
    
    with pytest.raises(ValueError):
        find_largest_prime_factor(1.5)