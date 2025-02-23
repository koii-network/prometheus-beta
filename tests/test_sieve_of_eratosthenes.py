import pytest
from src.sieve_of_eratosthenes import sieve_of_eratosthenes

def test_sieve_of_eratosthenes_basic():
    """Test basic functionality with a small number."""
    assert sieve_of_eratosthenes(10) == [2, 3, 5, 7]

def test_sieve_of_eratosthenes_large():
    """Test with a larger number."""
    result = sieve_of_eratosthenes(30)
    assert result == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def test_sieve_of_eratosthenes_edge_cases():
    """Test edge cases."""
    # 2 is the smallest prime number
    assert sieve_of_eratosthenes(2) == [2]

def test_sieve_of_eratosthenes_invalid_input():
    """Test error handling for invalid inputs."""
    # Test non-integer input
    with pytest.raises(TypeError):
        sieve_of_eratosthenes(10.5)

def test_sieve_of_eratosthenes_empty_result():
    """Test cases where no primes exist in the range."""
    # Should return empty list for inputs < 2
    assert sieve_of_eratosthenes(1) == []
    assert sieve_of_eratosthenes(0) == []
    assert sieve_of_eratosthenes(-1) == []