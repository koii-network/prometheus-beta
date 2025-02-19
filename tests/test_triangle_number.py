import pytest
from src.triangle_number import triangle_number

def test_triangle_numbers():
    """Test known Triangle Numbers"""
    # These are known Triangle Numbers
    triangle_nums = [1, 6, 28, 496, 8128]
    for num in triangle_nums:
        assert triangle_number(num) == True, f"{num} should be a Triangle Number"

def test_non_triangle_numbers():
    """Test non-Triangle Numbers"""
    non_triangle_nums = [2, 4, 7, 12, 15, 100]
    for num in non_triangle_nums:
        assert triangle_number(num) == False, f"{num} should not be a Triangle Number"

def test_input_validation():
    """Test input validation"""
    # Test zero
    with pytest.raises(ValueError):
        triangle_number(0)
    
    # Test negative number
    with pytest.raises(ValueError):
        triangle_number(-5)
    
    # Test non-integer
    with pytest.raises(ValueError):
        triangle_number(3.14)
    with pytest.raises(ValueError):
        triangle_number("not a number")