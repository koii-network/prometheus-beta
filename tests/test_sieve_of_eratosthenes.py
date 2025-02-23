import pytest
from src.sieve_of_eratosthenes import sieve_of_eratosthenes

def test_basic_prime_finding():
    """Test finding primes for a small number."""
    assert sieve_of_eratosthenes(10) == [2, 3, 5, 7]

def test_larger_prime_range():
    """Test finding primes in a larger range."""
    assert sieve_of_eratosthenes(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def test_single_prime():
    """Test finding primes when only 2 is prime."""
    assert sieve_of_eratosthenes(2) == [2]

def test_invalid_input_less_than_two():
    """Test that ValueError is raised for inputs less than 2."""
    with pytest.raises(ValueError, match="Input must be greater than or equal to 2"):
        sieve_of_eratosthenes(1)

def test_invalid_input_type():
    """Test that TypeError is raised for non-integer inputs."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        sieve_of_eratosthenes("not an int")

def test_zero_input():
    """Test that ValueError is raised for zero input."""
    with pytest.raises(ValueError, match="Input must be greater than or equal to 2"):
        sieve_of_eratosthenes(0)

def test_negative_input():
    """Test that ValueError is raised for negative inputs."""
    with pytest.raises(ValueError, match="Input must be greater than or equal to 2"):
        sieve_of_eratosthenes(-5)