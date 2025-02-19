import pytest
from src.prime_factorization import prime_factorization

def test_prime_factorization_basic():
    """Test basic prime factorization scenarios."""
    assert prime_factorization(12) == (2, 2, 3)
    assert prime_factorization(15) == (3, 5)
    assert prime_factorization(100) == (2, 2, 5, 5)
    assert prime_factorization(7) == (7,)

def test_prime_factorization_large_number():
    """Test prime factorization for larger numbers."""
    assert prime_factorization(84) == (2, 2, 3, 7)
    assert prime_factorization(360) == (2, 2, 2, 3, 3, 5)

def test_prime_factorization_prime_numbers():
    """Test prime factorization for prime numbers."""
    assert prime_factorization(2) == (2,)
    assert prime_factorization(17) == (17,)
    assert prime_factorization(97) == (97,)

def test_prime_factorization_error_handling():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be a positive integer greater than 1"):
        prime_factorization(1)
    
    with pytest.raises(ValueError, match="Input must be a positive integer greater than 1"):
        prime_factorization(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer greater than 1"):
        prime_factorization(-5)

def test_prime_factorization_type_checking():
    """Test type checking for input."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        prime_factorization(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        prime_factorization("10")
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        prime_factorization(None)