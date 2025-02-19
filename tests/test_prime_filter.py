import pytest
from src.prime_filter import filter_primes

def test_filter_primes_basic():
    """Test basic functionality of prime number filtering."""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected_output = [2, 3, 5, 7]
    assert filter_primes(input_list) == expected_output

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
    """Test filtering large prime and non-prime numbers."""
    input_list = [17, 20, 29, 36, 41, 50, 53, 97]
    expected_output = [17, 29, 41, 53, 97]
    assert filter_primes(input_list) == expected_output

def test_filter_primes_negative_numbers():
    """Test filtering list with negative numbers."""
    input_list = [-2, -3, -5, -7, 0, 1, 2, 3, 5, 7]
    expected_output = [2, 3, 5, 7]
    assert filter_primes(input_list) == expected_output