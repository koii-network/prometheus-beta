import pytest
from src.sieve_of_eratosthenes import sieve_of_eratosthenes

def test_sieve_basic_cases():
    """Test basic functionality of Sieve of Eratosthenes"""
    assert sieve_of_eratosthenes(10) == [2, 3, 5, 7]
    assert sieve_of_eratosthenes(20) == [2, 3, 5, 7, 11, 13, 17, 19]

def test_edge_cases():
    """Test edge cases"""
    # Small prime range
    assert sieve_of_eratosthenes(2) == [2]
    
    # Larger prime range
    large_primes = sieve_of_eratosthenes(100)
    assert 97 in large_primes
    assert len(large_primes) == 25  # Number of primes less than or equal to 100

def test_error_handling():
    """Test error handling for invalid inputs"""
    # Test less than 2
    with pytest.raises(ValueError, match="Input must be 2 or greater"):
        sieve_of_eratosthenes(1)
    
    # Test negative numbers
    with pytest.raises(ValueError, match="Input must be 2 or greater"):
        sieve_of_eratosthenes(-5)
    
    # Test non-integer input
    with pytest.raises(TypeError, match="Input must be an integer"):
        sieve_of_eratosthenes(10.5)
        
    with pytest.raises(TypeError, match="Input must be an integer"):
        sieve_of_eratosthenes("20")