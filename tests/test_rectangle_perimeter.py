import pytest
from src.rectangle_perimeter import calculate_rectangle_perimeter

def test_rectangle_perimeter_positive_numbers():
    """Test perimeter calculation with positive numbers"""
    assert calculate_rectangle_perimeter(5, 3) == 16
    assert calculate_rectangle_perimeter(10, 7) == 34
    assert calculate_rectangle_perimeter(2.5, 4.5) == 14.0

def test_rectangle_perimeter_zero():
    """Test perimeter calculation with zero dimensions"""
    assert calculate_rectangle_perimeter(0, 5) == 10
    assert calculate_rectangle_perimeter(5, 0) == 10
    assert calculate_rectangle_perimeter(0, 0) == 0

def test_rectangle_perimeter_negative_input():
    """Test that negative inputs raise a ValueError"""
    with pytest.raises(ValueError, match="Length and width must be non-negative numbers"):
        calculate_rectangle_perimeter(-1, 5)
    
    with pytest.raises(ValueError, match="Length and width must be non-negative numbers"):
        calculate_rectangle_perimeter(5, -3)
    
    with pytest.raises(ValueError, match="Length and width must be non-negative numbers"):
        calculate_rectangle_perimeter(-2, -4)