import pytest
from src.prime_factorization import prime_factorization

def test_prime_factorization_normal_cases():
    """Test prime factorization for various normal inputs."""
    assert prime_factorization(12) == (2, 2, 3)
    assert prime_factorization(17) == (17,)
    assert prime_factorization(100) == (2, 2, 5, 5)
    assert prime_factorization(2) == (2,)
    assert prime_factorization(3) == (3,)

def test_prime_factorization_large_number():
    """Test prime factorization for a larger number."""
    assert prime_factorization(84) == (2, 2, 3, 7)

def test_prime_factorization_prime_number():
    """Test prime factorization for various prime numbers."""
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for prime in primes:
        assert prime_factorization(prime) == (prime,)

def test_prime_factorization_error_handling():
    """Test error handling for invalid inputs."""
    # Test invalid types
    with pytest.raises(TypeError):
        prime_factorization("12")
    with pytest.raises(TypeError):
        prime_factorization(12.5)
    with pytest.raises(TypeError):
        prime_factorization(None)
    
    # Test values less than 2
    with pytest.raises(ValueError):
        prime_factorization(1)
    with pytest.raises(ValueError):
        prime_factorization(0)
    with pytest.raises(ValueError):
        prime_factorization(-5)