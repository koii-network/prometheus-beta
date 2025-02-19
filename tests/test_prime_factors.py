import pytest
from src.prime_factors import get_prime_factors

def test_prime_factors_basic():
    assert get_prime_factors(12) == [2, 2, 3]
    assert get_prime_factors(15) == [3, 5]
    assert get_prime_factors(100) == [2, 2, 5, 5]

def test_prime_factors_prime_number():
    assert get_prime_factors(7) == [7]
    assert get_prime_factors(23) == [23]

def test_prime_factors_large_number():
    assert get_prime_factors(84) == [2, 2, 3, 7]

def test_prime_factors_edge_cases():
    with pytest.raises(ValueError):
        get_prime_factors(1)
    
    with pytest.raises(ValueError):
        get_prime_factors(0)
    
    with pytest.raises(ValueError):
        get_prime_factors(-5)

def test_prime_factors_type_checking():
    with pytest.raises(TypeError):
        get_prime_factors(3.14)
    
    with pytest.raises(TypeError):
        get_prime_factors("12")
    
    with pytest.raises(TypeError):
        get_prime_factors([12])