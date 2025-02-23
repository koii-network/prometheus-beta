import pytest
from src.prime_finder import find_primes

def test_find_primes_basic_range():
    """Test finding primes in a basic range"""
    assert find_primes(1, 10) == [2, 3, 5, 7]

def test_find_primes_single_prime():
    """Test range with only one prime"""
    assert find_primes(7, 7) == [7]

def test_find_primes_no_primes():
    """Test range with no primes"""
    assert find_primes(4, 4) == []

def test_find_primes_large_range():
    """Test finding primes in a larger range"""
    assert find_primes(10, 30) == [11, 13, 17, 19, 23, 29]

def test_find_primes_lower_bound_zero():
    """Test range starting from zero"""
    assert find_primes(0, 10) == [2, 3, 5, 7]

def test_find_primes_negative_lower_bound():
    """Test that negative lower bound raises ValueError"""
    with pytest.raises(ValueError, match="Input range must be non-negative"):
        find_primes(-5, 10)

def test_find_primes_negative_upper_bound():
    """Test that negative upper bound raises ValueError"""
    with pytest.raises(ValueError, match="Input range must be non-negative"):
        find_primes(5, -10)

def test_find_primes_invalid_range():
    """Test that invalid range (a > b) raises ValueError"""
    with pytest.raises(ValueError, match="Lower bound must be less than or equal to upper bound"):
        find_primes(10, 5)

def test_find_primes_edge_case_two():
    """Test edge case with 2 as a prime number"""
    assert find_primes(2, 2) == [2]