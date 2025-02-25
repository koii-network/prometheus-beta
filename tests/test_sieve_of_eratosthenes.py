import pytest
from src.sieve_of_eratosthenes import sieve_of_eratosthenes

def test_basic_prime_finding():
    """Test finding primes up to a small number."""
    assert sieve_of_eratosthenes(10) == [2, 3, 5, 7]

def test_large_prime_finding():
    """Test finding primes in a larger range."""
    result = sieve_of_eratosthenes(30)
    assert result == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def test_minimal_prime():
    """Test finding primes starting from the first prime."""
    assert sieve_of_eratosthenes(2) == [2]

def test_invalid_input_less_than_two():
    """Test that ValueError is raised for inputs less than 2."""
    with pytest.raises(ValueError, match="Input must be at least 2"):
        sieve_of_eratosthenes(1)

def test_invalid_input_negative():
    """Test that ValueError is raised for negative inputs."""
    with pytest.raises(ValueError, match="Input must be at least 2"):
        sieve_of_eratosthenes(-5)

def test_invalid_input_type():
    """Test that TypeError is raised for non-integer inputs."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        sieve_of_eratosthenes(10.5)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        sieve_of_eratosthenes("20")

def test_empty_list_for_edge_cases():
    """Verify correct behavior for edge cases."""
    assert sieve_of_eratosthenes(2) == [2]