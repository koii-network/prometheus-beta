import pytest
from src.prime_numbers import find_primes

def test_default_primes():
    """Test finding primes from 1 to 100 by default"""
    expected_primes = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
        31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 
        73, 79, 83, 89, 97
    ]
    assert find_primes() == expected_primes

def test_primes_in_custom_range():
    """Test finding primes in a custom range"""
    assert find_primes(10, 20) == [11, 13, 17, 19]

def test_primes_lower_bound():
    """Test finding primes starting from a specific number"""
    assert find_primes(90, 100) == [97]

def test_invalid_start_raises_error():
    """Test that invalid start value raises ValueError"""
    with pytest.raises(ValueError, match="Start must be a positive integer"):
        find_primes(0, 100)

def test_invalid_end_raises_error():
    """Test that invalid end value raises ValueError"""
    with pytest.raises(ValueError, match="End must be greater than or equal to start"):
        find_primes(50, 20)

def test_single_prime_range():
    """Test finding primes in a range with a single prime"""
    assert find_primes(97, 97) == [97]

def test_no_primes_in_range():
    """Test finding primes in a range with no primes"""
    assert find_primes(24, 25) == []