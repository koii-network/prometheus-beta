import pytest
from src.prime_finder import find_primes_below_n

def test_find_primes_below_n_basic():
    """Test basic prime number generation"""
    assert find_primes_below_n(10) == [2, 3, 5, 7]
    assert find_primes_below_n(20) == [2, 3, 5, 7, 11, 13, 17, 19]

def test_find_primes_below_n_edge_cases():
    """Test edge cases"""
    assert find_primes_below_n(2) == []
    assert find_primes_below_n(3) == [2]
    assert find_primes_below_n(1) == []

def test_find_primes_below_n_larger_numbers():
    """Test with larger numbers"""
    primes_below_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    assert find_primes_below_n(100) == primes_below_100

def test_find_primes_below_n_error_handling():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        find_primes_below_n("10")
    with pytest.raises(TypeError):
        find_primes_below_n(3.14)
    with pytest.raises(TypeError):
        find_primes_below_n(None)