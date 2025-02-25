import pytest
from src.prime_detector import is_prime

def test_prime_numbers():
    """Test known prime numbers."""
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
                     31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 
                     73, 79, 83, 89, 97]
    for num in prime_numbers:
        assert is_prime(num) is True, f"{num} should be prime"

def test_non_prime_numbers():
    """Test known non-prime numbers."""
    non_prime_numbers = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 
                         20, 21, 22, 24, 25, 26, 27, 28, 30]
    for num in non_prime_numbers:
        assert is_prime(num) is False, f"{num} should not be prime"

def test_boundary_values():
    """Test boundary values of the input range."""
    assert is_prime(2) is True, "2 is the smallest prime number"
    assert is_prime(1000) is False, "1000 is not a prime number"

def test_invalid_inputs():
    """Test invalid input handling."""
    # Test inputs outside the valid range
    with pytest.raises(ValueError, match="Input must be between 2 and 1000"):
        is_prime(1)
    with pytest.raises(ValueError, match="Input must be between 2 and 1000"):
        is_prime(1001)
    
    # Test non-integer inputs
    with pytest.raises(ValueError, match="Input must be an integer"):
        is_prime(3.14)
    with pytest.raises(ValueError, match="Input must be an integer"):
        is_prime("not a number")