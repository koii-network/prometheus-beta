import pytest
from src.prime_factorization import prime_factorize

def test_prime_factorization_basic():
    """Test basic prime factorization cases."""
    assert prime_factorize(12) == (2, 2, 3)
    assert prime_factorize(15) == (3, 5)
    assert prime_factorize(100) == (2, 2, 5, 5)

def test_prime_factorization_prime_numbers():
    """Test prime numbers are returned correctly."""
    assert prime_factorize(2) == (2,)
    assert prime_factorize(17) == (17,)
    assert prime_factorize(29) == (29,)

def test_prime_factorization_edge_cases():
    """Test edge case inputs."""
    assert prime_factorize(1) == ()

def test_prime_factorization_invalid_inputs():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be an integer"):
        prime_factorize(3.14)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        prime_factorize(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        prime_factorize(-10)

def test_prime_factorization_large_number():
    """Test factorization of a larger number."""
    assert prime_factorize(84) == (2, 2, 3, 7)
    assert prime_factorize(360) == (2, 2, 2, 3, 3, 5)