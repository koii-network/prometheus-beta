import pytest
from src.prime_filter import filter_primes

def test_filter_primes_basic():
    """Test basic prime number filtering."""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected = [2, 3, 5, 7]
    assert filter_primes(input_list) == expected

def test_filter_primes_empty_list():
    """Test filtering an empty list."""
    assert filter_primes([]) == []

def test_filter_primes_no_primes():
    """Test a list with no prime numbers."""
    input_list = [1, 4, 6, 8, 9, 10]
    assert filter_primes(input_list) == []

def test_filter_primes_all_primes():
    """Test a list where all numbers are prime."""
    input_list = [2, 3, 5, 7, 11, 13]
    assert filter_primes(input_list) == input_list

def test_filter_primes_large_numbers():
    """Test filtering with larger prime and non-prime numbers."""
    input_list = [17, 22, 29, 36, 41, 50]
    expected = [17, 29, 41]
    assert filter_primes(input_list) == expected

def test_filter_primes_negative_numbers():
    """Test that negative numbers are handled correctly."""
    input_list = [-2, -3, -5, 0, 1, 2, 3, 5, 7]
    expected = [2, 3, 5, 7]
    assert filter_primes(input_list) == expected