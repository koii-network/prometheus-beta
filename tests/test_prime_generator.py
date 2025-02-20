import pytest
from src.prime_generator import generate_primes

def test_primes_up_to_100():
    """Test prime number generation up to 100."""
    expected_primes = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 
        43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
    ]
    assert generate_primes(100) == expected_primes

def test_edge_cases():
    """Test edge cases for prime number generation."""
    assert generate_primes(1) == []
    assert generate_primes(2) == [2]
    assert generate_primes(0) == []
    assert generate_primes(-5) == []

def test_prime_properties():
    """Additional tests to verify prime number properties."""
    primes = generate_primes(30)
    
    # Verify no even numbers except 2
    assert all(prime == 2 or prime % 2 != 0 for prime in primes)
    
    # Verify primality of generated numbers
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    assert all(is_prime(prime) for prime in primes)