import pytest
from src.largest_prime_factor import find_largest_prime_factor

def test_prime_number():
    # Test when the input is a prime number
    assert find_largest_prime_factor(17) == 17

def test_composite_number():
    # Test a composite number with various prime factors
    assert find_largest_prime_factor(13195) == 29

def test_large_number():
    # Test a large number
    assert find_largest_prime_factor(600851475143) == 6857

def test_even_number():
    # Test an even number
    assert find_largest_prime_factor(100) == 5

def test_perfect_square():
    # Test a perfect square
    assert find_largest_prime_factor(81) == 3

def test_invalid_input():
    # Test invalid inputs
    with pytest.raises(ValueError):
        find_largest_prime_factor(1)
    
    with pytest.raises(ValueError):
        find_largest_prime_factor(0)
    
    with pytest.raises(ValueError):
        find_largest_prime_factor(-10)