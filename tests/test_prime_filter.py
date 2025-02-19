import pytest
from src.prime_filter import filter_primes

def test_filter_primes_positive_numbers():
    """Test filtering prime numbers from a list of positive numbers"""
    assert filter_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 3, 5, 7]

def test_filter_primes_mixed_numbers():
    """Test filtering prime numbers from a list with mixed numbers"""
    assert filter_primes([-7, -5, -3, -2, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [-7, -5, -3, -2, 2, 3, 5, 7]

def test_filter_primes_no_primes():
    """Test filtering when no prime numbers are present"""
    assert filter_primes([1, 4, 6, 8, 9, 10, 12]) == []

def test_filter_primes_only_primes():
    """Test filtering when all numbers are prime"""
    assert filter_primes([2, 3, 5, 7, 11, 13]) == [2, 3, 5, 7, 11, 13]

def test_filter_primes_empty_list():
    """Test filtering an empty list"""
    assert filter_primes([]) == []

def test_filter_primes_large_numbers():
    """Test filtering with some larger prime and non-prime numbers"""
    assert filter_primes([997, 1000, 1009, 1024]) == [997, 1009]