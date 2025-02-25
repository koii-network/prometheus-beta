import pytest
from src.prime_checker import is_prime

def test_prime_numbers():
    """Test known prime numbers within the valid range."""
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
                     997, 991, 983, 977, 971]
    for num in prime_numbers:
        assert is_prime(num) is True

def test_non_prime_numbers():
    """Test known non-prime numbers within the valid range."""
    non_prime_numbers = [4, 6, 8, 9, 10, 12, 14, 15, 16, 
                         20, 21, 22, 24, 25, 26, 
                         980, 982, 984, 986, 988, 990]
    for num in non_prime_numbers:
        assert is_prime(num) is False

def test_edge_cases():
    """Test edge cases at the boundaries of the valid range."""
    assert is_prime(2) is True
    assert is_prime(1000) is False

def test_invalid_inputs():
    """Test error handling for invalid inputs."""
    # Test below range
    with pytest.raises(ValueError, match="Input must be an integer between 2 and 1000"):
        is_prime(1)
    
    # Test above range
    with pytest.raises(ValueError, match="Input must be an integer between 2 and 1000"):
        is_prime(1001)
    
    # Test non-integer input
    with pytest.raises(ValueError, match="Input must be an integer"):
        is_prime(3.14)
    
    with pytest.raises(ValueError, match="Input must be an integer"):
        is_prime("17")
    
    with pytest.raises(ValueError, match="Input must be an integer"):
        is_prime(None)