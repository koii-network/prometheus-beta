import pytest
from src.prime_finder import find_primes_in_range

def test_basic_prime_range():
    """Test finding primes in a standard range"""
    assert find_primes_in_range(10, 20) == [11, 13, 17, 19]

def test_single_prime_range():
    """Test range with a single prime number"""
    assert find_primes_in_range(17, 17) == [17]

def test_no_primes_range():
    """Test range with no prime numbers"""
    assert find_primes_in_range(24, 26) == []

def test_lower_bound_larger_than_upper_bound():
    """Test that ValueError is raised when lower bound > upper bound"""
    with pytest.raises(ValueError, match="Lower bound must be less than or equal to upper bound"):
        find_primes_in_range(20, 10)

def test_non_integer_input():
    """Test that ValueError is raised for non-integer inputs"""
    with pytest.raises(ValueError, match="Inputs must be integers"):
        find_primes_in_range(10.5, 20)
    with pytest.raises(ValueError, match="Inputs must be integers"):
        find_primes_in_range(10, "20")

def test_small_range():
    """Test range below 2"""
    assert find_primes_in_range(0, 1) == []

def test_large_range():
    """Test a larger range of primes"""
    expected_primes = [83, 89, 97]
    assert find_primes_in_range(80, 100) == expected_primes

def test_range_starting_below_two():
    """Test range that starts below 2"""
    assert find_primes_in_range(-10, 10) == [2, 3, 5, 7]