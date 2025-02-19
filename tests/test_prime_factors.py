import pytest
from src.prime_factors import get_prime_factors

def test_prime_factors_basic_cases():
    assert get_prime_factors(2) == [2]
    assert get_prime_factors(4) == [2, 2]
    assert get_prime_factors(12) == [2, 2, 3]
    assert get_prime_factors(15) == [3, 5]

def test_prime_factors_prime_numbers():
    assert get_prime_factors(7) == [7]
    assert get_prime_factors(11) == [11]
    assert get_prime_factors(17) == [17]
    assert get_prime_factors(23) == [23]

def test_prime_factors_large_numbers():
    assert get_prime_factors(100) == [2, 2, 5, 5]
    assert get_prime_factors(84) == [2, 2, 3, 7]
    assert get_prime_factors(1024) == [2] * 10

def test_prime_factors_error_handling():
    with pytest.raises(ValueError):
        get_prime_factors(0)
    
    with pytest.raises(ValueError):
        get_prime_factors(-5)
    
    with pytest.raises(ValueError):
        get_prime_factors(1.5)