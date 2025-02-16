import pytest
from src.prime_numbers import get_primes_up_to

def test_primes_up_to_100():
    """Test prime numbers up to 100."""
    expected_primes = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
        31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 
        73, 79, 83, 89, 97
    ]
    assert get_primes_up_to(100) == expected_primes

def test_primes_edge_cases():
    """Test edge cases for prime number generation."""
    # Test lower boundary conditions
    assert get_primes_up_to(1) == []
    assert get_primes_up_to(2) == [2]
    
def test_small_ranges():
    """Test prime numbers in small ranges."""
    assert get_primes_up_to(10) == [2, 3, 5, 7]
    assert get_primes_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]

def test_type_error():
    """Test handling of invalid input type."""
    with pytest.raises(TypeError):
        get_primes_up_to("100")
        
def test_negative_input():
    """Test handling of negative input."""
    assert get_primes_up_to(-5) == []