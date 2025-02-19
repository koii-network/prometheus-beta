import pytest
from src.prime_factorization import prime_factorization

def test_prime_factorization_basic():
    assert prime_factorization(12) == (2, 2, 3)
    assert prime_factorization(15) == (3, 5)
    assert prime_factorization(100) == (2, 2, 5, 5)

def test_prime_factorization_prime_number():
    assert prime_factorization(17) == (17,)
    assert prime_factorization(2) == (2,)
    assert prime_factorization(3) == (3,)

def test_prime_factorization_large_number():
    assert prime_factorization(84) == (2, 2, 3, 7)
    assert prime_factorization(360) == (2, 2, 2, 3, 3, 5)

def test_prime_factorization_invalid_input():
    with pytest.raises(TypeError):
        prime_factorization(3.14)
    
    with pytest.raises(TypeError):
        prime_factorization("12")
    
    with pytest.raises(ValueError):
        prime_factorization(1)
    
    with pytest.raises(ValueError):
        prime_factorization(0)
    
    with pytest.raises(ValueError):
        prime_factorization(-10)