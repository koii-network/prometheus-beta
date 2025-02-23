import pytest
from src.prime_factors import get_prime_factors

def test_prime_factors_basic():
    """Test basic prime factorization."""
    assert get_prime_factors(12) == [2, 2, 3]
    assert get_prime_factors(15) == [3, 5]
    assert get_prime_factors(100) == [2, 2, 5, 5]

def test_prime_factors_prime_number():
    """Test prime numbers are returned correctly."""
    assert get_prime_factors(17) == [17]
    assert get_prime_factors(2) == [2]

def test_prime_factors_one():
    """Test that 1 returns an empty list."""
    assert get_prime_factors(1) == []

def test_prime_factors_large_number():
    """Test a larger number with multiple prime factors."""
    assert get_prime_factors(84) == [2, 2, 3, 7]

def test_prime_factors_invalid_input():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be an integer"):
        get_prime_factors("not an integer")
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        get_prime_factors(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        get_prime_factors(-5)

def test_prime_factors_order():
    """Ensure factors are always returned in ascending order."""
    assert get_prime_factors(72) == [2, 2, 2, 3, 3]