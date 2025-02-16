import pytest
from src.prime_numbers import find_primes

def test_default_primes():
    """Test default range of primes from 1 to 100"""
    primes = find_primes()
    expected_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    assert primes == expected_primes

def test_custom_range_primes():
    """Test finding primes in a custom range"""
    primes = find_primes(10, 30)
    expected_primes = [11, 13, 17, 19, 23, 29]
    assert primes == expected_primes

def test_invalid_range_start():
    """Test that function raises error for start less than 1"""
    with pytest.raises(ValueError, match="Start of range must be at least 1"):
        find_primes(0, 100)

def test_invalid_range_end():
    """Test that function raises error when end is less than start"""
    with pytest.raises(ValueError, match="End of range must be greater than or equal to start"):
        find_primes(50, 30)

def test_small_range():
    """Test finding primes in a very small range"""
    primes = find_primes(1, 2)
    assert primes == [2]

def test_no_primes_in_range():
    """Test a range with no prime numbers"""
    primes = find_primes(24, 26)
    assert primes == []