import pytest
from src.sieve_of_eratosthenes import sieve_of_eratosthenes

def test_sieve_of_eratosthenes_basic():
    """Test basic functionality of the Sieve of Eratosthenes."""
    assert sieve_of_eratosthenes(10) == [2, 3, 5, 7]
    assert sieve_of_eratosthenes(20) == [2, 3, 5, 7, 11, 13, 17, 19]

def test_sieve_of_eratosthenes_edge_cases():
    """Test edge cases for the Sieve of Eratosthenes."""
    assert sieve_of_eratosthenes(2) == [2]
    
def test_sieve_of_eratosthenes_invalid_input():
    """Test invalid input scenarios."""
    with pytest.raises(ValueError, match="Input must be at least 2"):
        sieve_of_eratosthenes(1)
    
    with pytest.raises(ValueError, match="Input must be at least 2"):
        sieve_of_eratosthenes(0)
    
    with pytest.raises(ValueError, match="Input must be at least 2"):
        sieve_of_eratosthenes(-5)

def test_sieve_of_eratosthenes_type_check():
    """Test type checking for input."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        sieve_of_eratosthenes("10")
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        sieve_of_eratosthenes(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        sieve_of_eratosthenes(None)