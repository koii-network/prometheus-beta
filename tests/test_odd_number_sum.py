import pytest
from src.odd_number_sum import sum_odd_numbers

def test_sum_odd_numbers_basic():
    """Test basic functionality with small positive integers."""
    assert sum_odd_numbers(5) == 9  # 1 + 3 + 5
    assert sum_odd_numbers(10) == 25  # 1 + 3 + 5 + 7 + 9

def test_sum_odd_numbers_zero():
    """Test behavior with zero input."""
    assert sum_odd_numbers(0) == 0

def test_sum_odd_numbers_one():
    """Test behavior with input of 1."""
    assert sum_odd_numbers(1) == 1

def test_sum_odd_numbers_large():
    """Test behavior with a larger input."""
    assert sum_odd_numbers(100) == 2500

def test_sum_odd_numbers_invalid_input():
    """Test error handling for invalid inputs."""
    # Test negative input
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        sum_odd_numbers(-5)
    
    # Test non-integer input
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_odd_numbers(5.5)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_odd_numbers("10")
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_odd_numbers([1, 2, 3])