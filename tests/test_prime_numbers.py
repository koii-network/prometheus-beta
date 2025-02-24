import pytest
from src.prime_numbers import find_primes_up_to_n

def test_primes_up_to_100():
    """Test prime numbers up to 100."""
    expected_primes = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 
        53, 59, 61, 67, 71, 73, 79, 83, 89, 97
    ]
    assert find_primes_up_to_n(100) == expected_primes

def test_small_primes():
    """Test prime numbers for small inputs."""
    assert find_primes_up_to_n(10) == [2, 3, 5, 7]
    assert find_primes_up_to_n(2) == [2]

def test_edge_cases():
    """Test edge cases."""
    assert find_primes_up_to_n(1) == []
    assert find_primes_up_to_n(0) == []
    assert find_primes_up_to_n(-1) == []

def test_invalid_input():
    """Test invalid input types."""
    with pytest.raises(ValueError, match="Input must be an integer"):
        find_primes_up_to_n(3.14)
    
    with pytest.raises(ValueError, match="Input must be an integer"):
        find_primes_up_to_n("not a number")