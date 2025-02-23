import pytest
from src.prime_filter import is_prime, filter_primes

def test_is_prime():
    """Test the is_prime function with various inputs."""
    # Known prime numbers
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(17) == True
    assert is_prime(29) == True
    
    # Known non-prime numbers
    assert is_prime(1) == False
    assert is_prime(0) == False
    assert is_prime(-7) == False
    assert is_prime(4) == False
    assert is_prime(15) == False
    assert is_prime(100) == False

def test_is_prime_type_error():
    """Test is_prime with invalid input types."""
    with pytest.raises(TypeError):
        is_prime("not a number")
    with pytest.raises(TypeError):
        is_prime(3.14)
    with pytest.raises(TypeError):
        is_prime(None)

def test_filter_primes():
    """Test filtering prime numbers from a list."""
    # Basic case
    assert filter_primes([2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 3, 5, 7]
    
    # Empty list
    assert filter_primes([]) == []
    
    # List with no primes
    assert filter_primes([1, 4, 6, 8, 9, 10]) == []
    
    # List with only primes
    assert filter_primes([2, 3, 5, 7, 11, 13]) == [2, 3, 5, 7, 11, 13]

def test_filter_primes_type_errors():
    """Test filter_primes with invalid inputs."""
    # Non-list input
    with pytest.raises(TypeError):
        filter_primes("not a list")
    
    # List with non-integer elements
    with pytest.raises(TypeError):
        filter_primes([1, 2, "three", 4])
    
    # List with float elements
    with pytest.raises(TypeError):
        filter_primes([1, 2, 3.14, 4])