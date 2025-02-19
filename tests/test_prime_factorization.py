import pytest
from src.prime_factorization import prime_factorization

def test_prime_factorization_basic():
    assert prime_factorization(12) == (2, 2, 3)
    assert prime_factorization(15) == (3, 5)
    assert prime_factorization(100) == (2, 2, 5, 5)

def test_prime_number_factorization():
    assert prime_factorization(7) == (7)
    assert prime_factorization(11) == (11)
    assert prime_factorization(17) == (17)

def test_large_number_factorization():
    assert prime_factorization(84) == (2, 2, 3, 7)
    assert prime_factorization(360) == (2, 2, 2, 3, 3, 5)

def test_power_of_two():
    assert prime_factorization(2) == (2)
    assert prime_factorization(16) == (2, 2, 2, 2)

def test_invalid_inputs():
    with pytest.raises(ValueError):
        prime_factorization(1)
    
    with pytest.raises(ValueError):
        prime_factorization(0)
    
    with pytest.raises(ValueError):
        prime_factorization(-10)
    
    with pytest.raises(TypeError):
        prime_factorization(3.14)
    
    with pytest.raises(TypeError):
        prime_factorization("not a number")