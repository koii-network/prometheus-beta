import pytest
from src.perfect_number import is_perfect_number

def test_known_perfect_numbers():
    """Test known perfect numbers."""
    perfect_numbers = [6, 28, 496, 8128]
    for num in perfect_numbers:
        assert is_perfect_number(num) is True, f"{num} should be a perfect number"

def test_non_perfect_numbers():
    """Test numbers that are not perfect numbers."""
    non_perfect_numbers = [4, 10, 15, 21, 25]
    for num in non_perfect_numbers:
        assert is_perfect_number(num) is False, f"{num} should not be a perfect number"

def test_edge_cases():
    """Test edge cases and boundary conditions."""
    # Test 1, which is not considered a perfect number
    assert is_perfect_number(1) is False
    
    # Test very large number that is not a perfect number
    assert is_perfect_number(10000) is False

def test_invalid_inputs():
    """Test error handling for invalid inputs."""
    # Test non-integer inputs
    with pytest.raises(ValueError, match="Input must be an integer"):
        is_perfect_number(6.5)
    
    with pytest.raises(ValueError, match="Input must be an integer"):
        is_perfect_number("6")
    
    # Test non-positive inputs
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        is_perfect_number(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        is_perfect_number(-6)