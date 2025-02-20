import pytest
from src.prime_factors import get_prime_factors

def test_prime_factors_standard_cases():
    assert get_prime_factors(120) == [2, 2, 2, 3, 5]
    assert get_prime_factors(84) == [2, 2, 3, 7]
    assert get_prime_factors(13) == [13]
    assert get_prime_factors(1) == []

def test_prime_factors_single_digit_primes():
    assert get_prime_factors(2) == [2]
    assert get_prime_factors(3) == [3]
    assert get_prime_factors(5) == [5]
    assert get_prime_factors(7) == [7]

def test_prime_factors_large_numbers():
    assert get_prime_factors(9999991) == [9999991]  # A large prime number
    assert get_prime_factors(7 * 11 * 13) == [7, 11, 13]

def test_invalid_input():
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        get_prime_factors(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        get_prime_factors(-5)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        get_prime_factors(3.14)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        get_prime_factors("120")