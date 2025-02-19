import pytest
from src.prime_filter import filter_primes

def test_filter_primes_basic():
    """Test basic prime filtering"""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected = [2, 3, 5, 7]
    assert filter_primes(input_list) == expected

def test_filter_primes_empty_list():
    """Test filtering an empty list"""
    assert filter_primes([]) == []

def test_filter_primes_no_primes():
    """Test list with no prime numbers"""
    input_list = [1, 4, 6, 8, 9, 10]
    assert filter_primes(input_list) == []

def test_filter_primes_all_primes():
    """Test list with all prime numbers"""
    input_list = [2, 3, 5, 7, 11, 13]
    assert filter_primes(input_list) == input_list

def test_filter_primes_negative_numbers():
    """Test filtering list with negative numbers"""
    input_list = [-3, -2, -1, 0, 1, 2, 3, 4, 5]
    expected = [2, 3, 5]
    assert filter_primes(input_list) == expected

def test_filter_primes_large_numbers():
    """Test filtering large prime and non-prime numbers"""
    input_list = [97, 100, 541, 1000, 104729]
    expected = [97, 541, 104729]
    assert filter_primes(input_list) == expected