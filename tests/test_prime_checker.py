import pytest
from src.prime_checker import is_prime

def test_prime_numbers():
    """Test known prime numbers"""
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
                     97, 101, 103, 107, 109, 997, 993]
    for num in prime_numbers:
        assert is_prime(num), f"{num} should be prime"

def test_non_prime_numbers():
    """Test known non-prime numbers"""
    non_prime_numbers = [4, 6, 8, 9, 10, 12, 14, 15, 16, 
                         20, 21, 22, 24, 25, 100, 999]
    for num in non_prime_numbers:
        assert not is_prime(num), f"{num} should not be prime"

def test_input_validation():
    """Test input validation"""
    # Test lower bound
    with pytest.raises(ValueError, match="Input must be between 2 and 1000"):
        is_prime(1)
    
    # Test upper bound
    with pytest.raises(ValueError, match="Input must be between 2 and 1000"):
        is_prime(1001)
    
    # Test non-integer input
    with pytest.raises(ValueError, match="Input must be an integer"):
        is_prime(3.14)
    with pytest.raises(ValueError, match="Input must be an integer"):
        is_prime("17")

def test_boundary_conditions():
    """Test boundary conditions"""
    assert is_prime(2), "2 should be prime"
    assert is_prime(997), "997 should be prime"
    assert is_prime(993), "993 should be prime"
    assert not is_prime(1000), "1000 should not be prime"