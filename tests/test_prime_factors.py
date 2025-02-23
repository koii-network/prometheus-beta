import pytest
from src.prime_factors import prime_factorization

def test_prime_factorization_basic_case():
    """Test a basic composite number"""
    assert prime_factorization(120) == [2, 2, 2, 3, 5]

def test_prime_factorization_prime_number():
    """Test a prime number"""
    assert prime_factorization(17) == [17]

def test_prime_factorization_small_numbers():
    """Test small numbers with different factor patterns"""
    assert prime_factorization(1) == []
    assert prime_factorization(2) == [2]
    assert prime_factorization(4) == [2, 2]
    assert prime_factorization(12) == [2, 2, 3]

def test_prime_factorization_large_prime():
    """Test a large prime number"""
    assert prime_factorization(104729) == [104729]

def test_prime_factorization_large_composite():
    """Test a large composite number"""
    result = prime_factorization(123456)
    assert result == [2, 2, 2, 2, 2, 2, 1929]
    
def test_prime_factorization_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        prime_factorization(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        prime_factorization(-10)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        prime_factorization(3.14)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        prime_factorization("not a number")