import pytest
from src.prime_numbers import get_primes

def test_primes_up_to_100():
    """Test that all primes up to 100 are correctly identified."""
    expected_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    assert get_primes(100) == expected_primes

def test_small_primes():
    """Test lower bound and small prime number cases."""
    assert get_primes(10) == [2, 3, 5, 7]
    assert get_primes(1) == []

def test_boundary_conditions():
    """Test edge cases like 0 and 1."""
    assert get_primes(0) == []
    assert get_primes(1) == []

def test_invalid_input():
    """Test that a ValueError is raised for negative inputs."""
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        get_primes(-5)