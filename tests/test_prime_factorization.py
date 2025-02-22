import pytest
from src.prime_factorization import prime_factorization

def test_prime_factors_of_prime_number():
    """Test factorization of a prime number"""
    assert prime_factorization(17) == (17,)

def test_prime_factors_of_composite_number():
    """Test factorization of a composite number"""
    assert prime_factorization(12) == (2, 2, 3)
    assert prime_factorization(100) == (2, 2, 5, 5)
    assert prime_factorization(84) == (2, 2, 3, 7)

def test_large_prime_number():
    """Test factorization of a large prime number"""
    assert prime_factorization(997) == (997,)

def test_small_input_error():
    """Test error handling for inputs less than 2"""
    with pytest.raises(ValueError, match="Input must be a positive integer greater than 1"):
        prime_factorization(1)
    with pytest.raises(ValueError, match="Input must be a positive integer greater than 1"):
        prime_factorization(0)
    with pytest.raises(ValueError, match="Input must be a positive integer greater than 1"):
        prime_factorization(-5)

def test_type_error():
    """Test error handling for non-integer inputs"""
    with pytest.raises(TypeError, match="Input must be an integer"):
        prime_factorization(3.14)
    with pytest.raises(TypeError, match="Input must be an integer"):
        prime_factorization("12")
    with pytest.raises(TypeError, match="Input must be an integer"):
        prime_factorization(None)