import pytest
from src.prime_factors import get_prime_factors

def test_prime_factors_standard_cases():
    """Test prime factorization for various standard numbers."""
    assert get_prime_factors(12) == [2, 2, 3]
    assert get_prime_factors(15) == [3, 5]
    assert get_prime_factors(100) == [2, 2, 5, 5]
    assert get_prime_factors(7) == [7]

def test_prime_factors_edge_cases():
    """Test edge cases for prime factorization."""
    assert get_prime_factors(1) == []  # Special case for 1
    assert get_prime_factors(2) == [2]  # Smallest prime
    assert get_prime_factors(16) == [2, 2, 2, 2]  # Power of prime

def test_prime_factors_large_number():
    """Test prime factorization for a larger number."""
    assert get_prime_factors(84) == [2, 2, 3, 7]

def test_prime_factors_input_validation():
    """Test input validation for the function."""
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        get_prime_factors(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        get_prime_factors(-5)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        get_prime_factors(3.14)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        get_prime_factors("not a number")