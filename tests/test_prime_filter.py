import pytest
from src.prime_filter import is_prime, filter_primes

# Tests for is_prime function
def test_is_prime_known_primes():
    """Test known prime numbers"""
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(7) == True
    assert is_prime(11) == True
    assert is_prime(13) == True
    assert is_prime(17) == True
    assert is_prime(19) == True

def test_is_prime_known_non_primes():
    """Test known non-prime numbers"""
    assert is_prime(1) == False
    assert is_prime(4) == False
    assert is_prime(6) == False
    assert is_prime(8) == False
    assert is_prime(9) == False
    assert is_prime(10) == False
    assert is_prime(12) == False
    assert is_prime(15) == False

def test_is_prime_negative_numbers():
    """Test that negative numbers and zero are not prime"""
    assert is_prime(0) == False
    assert is_prime(-1) == False
    assert is_prime(-7) == False

def test_is_prime_invalid_input():
    """Test that invalid inputs raise appropriate exceptions"""
    with pytest.raises(TypeError):
        is_prime("2")
    with pytest.raises(TypeError):
        is_prime(3.14)
    with pytest.raises(TypeError):
        is_prime(None)

# Tests for filter_primes function
def test_filter_primes_basic():
    """Test basic filtering of prime numbers"""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected = [2, 3, 5, 7]
    assert filter_primes(input_list) == expected

def test_filter_primes_empty_list():
    """Test filtering an empty list"""
    assert filter_primes([]) == []

def test_filter_primes_no_primes():
    """Test filtering a list with no prime numbers"""
    assert filter_primes([1, 4, 6, 8, 9, 10]) == []

def test_filter_primes_all_primes():
    """Test filtering a list of all prime numbers"""
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    assert filter_primes(primes) == primes

def test_filter_primes_invalid_input():
    """Test that invalid inputs to filter_primes raise appropriate exceptions"""
    with pytest.raises(TypeError):
        filter_primes("not a list")
    
    with pytest.raises(TypeError):
        filter_primes([1, 2, "3", 4])
    
    with pytest.raises(TypeError):
        filter_primes([1, 2, 3.14, 4])