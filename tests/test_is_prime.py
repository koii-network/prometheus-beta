import pytest
from src.is_prime import is_prime

def test_prime_numbers():
    """Test known prime numbers"""
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
                     97, 101, 103, 107, 109, 997]
    for num in prime_numbers:
        assert is_prime(num) is True, f"{num} should be prime"

def test_non_prime_numbers():
    """Test known non-prime numbers"""
    non_prime_numbers = [1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 
                         18, 20, 21, 22, 24, 25, 100, 999]
    for num in non_prime_numbers:
        assert is_prime(num) is False, f"{num} should not be prime"

def test_input_validation():
    """Test input validation"""
    # Test invalid inputs
    with pytest.raises(ValueError, match="Input must be between 2 and 1000"):
        is_prime(1)
    with pytest.raises(ValueError, match="Input must be between 2 and 1000"):
        is_prime(1001)
    
    with pytest.raises(ValueError, match="Input must be an integer"):
        is_prime(3.14)
    with pytest.raises(ValueError, match="Input must be an integer"):
        is_prime("7")