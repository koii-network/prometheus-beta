import pytest
from src.sieve_of_eratosthenes import sieve_of_eratosthenes

def test_sieve_of_eratosthenes_basic():
    """Test basic functionality of Sieve of Eratosthenes"""
    assert sieve_of_eratosthenes(10) == [2, 3, 5, 7]
    assert sieve_of_eratosthenes(20) == [2, 3, 5, 7, 11, 13, 17, 19]

def test_sieve_of_eratosthenes_small_prime():
    """Test smallest prime inputs"""
    assert sieve_of_eratosthenes(2) == [2]

def test_sieve_of_eratosthenes_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Input must be greater than or equal to 2"):
        sieve_of_eratosthenes(1)
    
    with pytest.raises(ValueError, match="Input must be greater than or equal to 2"):
        sieve_of_eratosthenes(0)
    
    with pytest.raises(ValueError, match="Input must be greater than or equal to 2"):
        sieve_of_eratosthenes(-5)

def test_sieve_of_eratosthenes_large_input():
    """Test a larger input"""
    primes = sieve_of_eratosthenes(100)
    assert len(primes) == 25  # There are 25 primes <= 100
    assert primes[0] == 2
    assert primes[-1] == 97