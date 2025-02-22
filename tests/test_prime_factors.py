import pytest
from src.prime_factors import get_prime_factors

def test_prime_factors_basic():
    assert get_prime_factors(12) == [2, 2, 3]
    assert get_prime_factors(15) == [3, 5]
    assert get_prime_factors(100) == [2, 2, 5, 5]

def test_prime_factors_prime_numbers():
    assert get_prime_factors(2) == [2]
    assert get_prime_factors(7) == [7]
    assert get_prime_factors(17) == [17]

def test_prime_factors_large_number():
    assert get_prime_factors(84) == [2, 2, 3, 7]

def test_prime_factors_one():
    assert get_prime_factors(1) == []

def test_prime_factors_invalid_input():
    with pytest.raises(ValueError):
        get_prime_factors(0)
    
    with pytest.raises(ValueError):
        get_prime_factors(-5)
    
    with pytest.raises(ValueError):
        get_prime_factors(3.14)

def test_prime_factors_sorted():
    result = get_prime_factors(84)
    assert result == sorted(result), "Factors should be in ascending order"