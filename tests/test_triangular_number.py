import pytest
from src.triangular_number import calculate_triangular_number

def test_positive_triangular_numbers():
    """Test triangular numbers for positive inputs."""
    test_cases = [
        (0, 0),   # Edge case: first triangular number
        (1, 1),   # First positive triangular number 
        (2, 3),   # 1 + 2
        (3, 6),   # 1 + 2 + 3
        (4, 10),  # 1 + 2 + 3 + 4
        (5, 15),  # 1 + 2 + 3 + 4 + 5
        (10, 55)  # A larger triangular number
    ]
    
    for n, expected in test_cases:
        assert calculate_triangular_number(n) == expected

def test_invalid_inputs():
    """Test error handling for invalid inputs."""
    # Test negative numbers
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        calculate_triangular_number(-1)
    
    # Test non-integer inputs
    with pytest.raises(ValueError, match="Input must be an integer"):
        calculate_triangular_number(3.14)
    
    with pytest.raises(ValueError, match="Input must be an integer"):
        calculate_triangular_number("5")

def test_large_input():
    """Test a larger input to ensure no integer overflow."""
    # A reasonably large number that should not cause overflow
    large_n = 10000
    large_result = calculate_triangular_number(large_n)
    # Manually verify using the formula
    expected = large_n * (large_n + 1) // 2
    assert large_result == expected