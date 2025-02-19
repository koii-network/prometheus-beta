import pytest
from src.prime_factors import get_prime_factors

def test_prime_factors_basic():
    """Test basic prime factorizations."""
    assert get_prime_factors(12) == [2, 2, 3]
    assert get_prime_factors(15) == [3, 5]
    assert get_prime_factors(100) == [2, 2, 5, 5]

def test_prime_factors_prime_number():
    """Test factorization of prime numbers."""
    assert get_prime_factors(2) == [2]
    assert get_prime_factors(7) == [7]
    assert get_prime_factors(17) == [17]

def test_prime_factors_large_number():
    """Test factorization of a larger number."""
    assert get_prime_factors(84) == [2, 2, 3, 7]

def test_prime_factors_error_handling():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError):
        get_prime_factors(0)
    
    with pytest.raises(ValueError):
        get_prime_factors(-5)
    
    with pytest.raises(ValueError):
        get_prime_factors(3.14)
    
    with pytest.raises(ValueError):
        get_prime_factors("not a number")