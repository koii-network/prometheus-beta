import pytest
from src.find_primes import find_primes_in_range

def test_find_primes_in_standard_range():
    """Test finding primes in a standard range"""
    assert find_primes_in_range(10, 20) == [11, 13, 17, 19]

def test_find_primes_in_small_range():
    """Test finding primes in a small range"""
    assert find_primes_in_range(1, 10) == [2, 3, 5, 7]

def test_find_primes_with_same_number():
    """Test when lower and upper bounds are the same"""
    assert find_primes_in_range(17, 17) == [17]
    assert find_primes_in_range(4, 4) == []

def test_find_primes_with_zero_and_one():
    """Test range including zero and one"""
    assert find_primes_in_range(0, 2) == [2]

def test_find_primes_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Both a and b must be non-negative integers"):
        find_primes_in_range(-1, 10)
    
    with pytest.raises(ValueError, match="Lower bound a must be less than or equal to upper bound b"):
        find_primes_in_range(20, 10)

def test_find_primes_large_range():
    """Test finding primes in a larger range"""
    primes = find_primes_in_range(90, 110)
    assert primes == [97, 101, 103, 107, 109]