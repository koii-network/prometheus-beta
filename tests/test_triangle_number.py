import pytest
from src.triangle_number import triangle_number

def test_known_triangle_numbers():
    """Test known Triangle Numbers."""
    triangle_numbers = [6, 28, 496, 8128]
    for num in triangle_numbers:
        assert triangle_number(num) is True, f"{num} should be a Triangle Number"

def test_non_triangle_numbers():
    """Test numbers that are not Triangle Numbers."""
    non_triangle_numbers = [4, 12, 100, 500]
    for num in non_triangle_numbers:
        assert triangle_number(num) is False, f"{num} should not be a Triangle Number"

def test_edge_cases():
    """Test edge cases for the triangle_number function."""
    # Test the smallest triangle number
    assert triangle_number(1) is False
    
    # Test a large triangle number
    assert triangle_number(8128) is True

def test_input_validation():
    """Test input validation for the triangle_number function."""
    # Test negative number
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        triangle_number(-5)
    
    # Test zero
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        triangle_number(0)
    
    # Test non-integer input
    with pytest.raises(TypeError, match="Input must be an integer"):
        triangle_number(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        triangle_number("6")