import pytest
from src.prime_checker import is_prime

def test_prime_numbers():
    """Test known prime numbers"""
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
                     97, 101, 503, 997]
    for num in prime_numbers:
        assert is_prime(num) is True, f"{num} should be prime"

def test_non_prime_numbers():
    """Test known non-prime numbers"""
    non_prime_numbers = [4, 6, 8, 9, 10, 12, 14, 15, 16, 
                         20, 21, 22, 24, 25, 26, 27, 28, 
                         100, 500, 999]
    for num in non_prime_numbers:
        assert is_prime(num) is False, f"{num} should not be prime"

def test_edge_cases():
    """Test boundary conditions"""
    # Test lower bound
    assert is_prime(2) is True, "2 should be prime"
    # Test upper bound
    assert is_prime(1000) is False, "1000 should not be prime"

def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    # Test non-integer inputs
    with pytest.raises(ValueError, match="Input must be an integer"):
        is_prime(3.14)
        is_prime("7")
        is_prime(None)
    
    # Test out of range inputs
    with pytest.raises(ValueError, match="Number must be between 2 and 1000"):
        is_prime(1)
        is_prime(1001)
        is_prime(-5)