import pytest
from src.find_primes import find_primes_below_n

def test_find_primes_below_n_basic():
    """Test basic prime number finding"""
    assert find_primes_below_n(10) == [2, 3, 5, 7]
    assert find_primes_below_n(20) == [2, 3, 5, 7, 11, 13, 17, 19]

def test_find_primes_below_n_edge_cases():
    """Test edge cases"""
    assert find_primes_below_n(2) == []  # No primes below 2
    assert find_primes_below_n(1) == []  # No primes below 1
    assert find_primes_below_n(0) == []  # No primes below 0
    assert find_primes_below_n(-5) == []  # No primes for negative numbers

def test_find_primes_below_n_large_number():
    """Test with a larger number"""
    primes = find_primes_below_n(100)
    expected_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    assert primes == expected_primes

def test_find_primes_below_n_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        find_primes_below_n("not a number")
    
    with pytest.raises(TypeError):
        find_primes_below_n(3.14)