import pytest
from src.prime_finder import find_primes_below_n

def test_find_primes_below_n_basic():
    """Test basic prime number finding."""
    assert find_primes_below_n(10) == [2, 3, 5, 7]

def test_find_primes_below_n_small_input():
    """Test input less than 2."""
    assert find_primes_below_n(2) == []
    assert find_primes_below_n(1) == []
    assert find_primes_below_n(0) == []

def test_find_primes_below_n_larger_input():
    """Test finding primes for a larger input."""
    primes_below_20 = [2, 3, 5, 7, 11, 13, 17, 19]
    assert find_primes_below_n(20) == primes_below_20

def test_find_primes_below_n_invalid_input():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError):
        find_primes_below_n("not a number")
    
    with pytest.raises(TypeError):
        find_primes_below_n(3.14)

def test_find_primes_below_n_edge_cases():
    """Test various edge cases."""
    # Ensure 1 is not considered prime
    assert 1 not in find_primes_below_n(10)
    
    # Check some known properties of prime numbers
    primes = find_primes_below_n(100)
    assert len(primes) > 0
    assert all(p > 1 for p in primes)
    assert all(all(p % divisor != 0 for divisor in range(2, int(p**0.5) + 1)) for p in primes)