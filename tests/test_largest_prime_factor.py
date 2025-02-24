import pytest
from src.largest_prime_factor import find_largest_prime_factor

def test_small_prime_number():
    """Test with a small prime number"""
    assert find_largest_prime_factor(17) == 17

def test_composite_number():
    """Test with a composite number"""
    assert find_largest_prime_factor(13195) == 29

def test_large_number():
    """Test with a large number"""
    assert find_largest_prime_factor(600851475143) == 6857

def test_prime_power():
    """Test with a number that is a power of a prime"""
    assert find_largest_prime_factor(8) == 2

def test_invalid_input_less_than_two():
    """Test that ValueError is raised for inputs <= 1"""
    with pytest.raises(ValueError):
        find_largest_prime_factor(1)
    
    with pytest.raises(ValueError):
        find_largest_prime_factor(0)
    
    with pytest.raises(ValueError):
        find_largest_prime_factor(-10)

def test_invalid_input_type():
    """Test that TypeError is raised for non-integer inputs"""
    with pytest.raises(TypeError):
        find_largest_prime_factor(3.14)
    
    with pytest.raises(TypeError):
        find_largest_prime_factor("123")
    
    with pytest.raises(TypeError):
        find_largest_prime_factor(None)