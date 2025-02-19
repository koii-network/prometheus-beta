import pytest
from src.find_primes import find_primes_in_range

def test_find_primes_in_range_basic():
    """Test finding primes in a basic range"""
    assert find_primes_in_range(1, 10) == [2, 3, 5, 7]

def test_find_primes_in_range_large():
    """Test finding primes in a larger range"""
    assert find_primes_in_range(10, 30) == [11, 13, 17, 19, 23, 29]

def test_find_primes_in_range_single_prime():
    """Test finding a single prime number"""
    assert find_primes_in_range(17, 17) == [17]

def test_find_primes_in_range_no_primes():
    """Test range with no primes"""
    assert find_primes_in_range(4, 6) == []

def test_find_primes_in_range_lower_bound_validation():
    """Test validation of lower bound"""
    with pytest.raises(ValueError, match="Input numbers must be non-negative"):
        find_primes_in_range(-1, 10)

def test_find_primes_in_range_upper_bound_validation():
    """Test validation of upper bound"""
    with pytest.raises(ValueError, match="Input numbers must be non-negative"):
        find_primes_in_range(10, -1)

def test_find_primes_in_range_invalid_bounds():
    """Test when lower bound is greater than upper bound"""
    with pytest.raises(ValueError, match="Lower bound must be less than or equal to upper bound"):
        find_primes_in_range(10, 5)

def test_find_primes_in_range_edge_cases():
    """Test edge cases"""
    assert find_primes_in_range(0, 1) == []  # No primes
    assert find_primes_in_range(2, 2) == [2]  # Smallest prime