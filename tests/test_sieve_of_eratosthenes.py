import pytest
from src.sieve_of_eratosthenes import sieve_of_eratosthenes

def test_sieve_of_eratosthenes_basic():
    """Test basic prime number generation"""
    assert sieve_of_eratosthenes(10) == [2, 3, 5, 7]
    assert sieve_of_eratosthenes(20) == [2, 3, 5, 7, 11, 13, 17, 19]

def test_sieve_of_eratosthenes_edge_cases():
    """Test edge cases"""
    assert sieve_of_eratosthenes(2) == [2]
    
def test_sieve_of_eratosthenes_invalid_input():
    """Test invalid input handling"""
    with pytest.raises(ValueError, match="Input must be greater than or equal to 2"):
        sieve_of_eratosthenes(1)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        sieve_of_eratosthenes(3.14)
        sieve_of_eratosthenes("10")
        sieve_of_eratosthenes(None)

def test_sieve_of_eratosthenes_large_input():
    """Test with a larger input"""
    primes = sieve_of_eratosthenes(100)
    assert len(primes) == 25  # Number of primes less than or equal to 100
    # Verify some known primes in this range
    assert all(p in primes for p in [2, 3, 5, 7, 11, 13, 17, 19, 97])