import pytest
from src.rectangle_perimeter import calculate_rectangle_perimeter

def test_rectangle_perimeter_standard():
    """Test perimeter calculation for standard rectangle."""
    assert calculate_rectangle_perimeter(5, 3) == 16

def test_rectangle_perimeter_zero():
    """Test perimeter calculation with zero dimensions."""
    assert calculate_rectangle_perimeter(0, 0) == 0

def test_rectangle_perimeter_square():
    """Test perimeter calculation for a square."""
    assert calculate_rectangle_perimeter(4, 4) == 16

def test_rectangle_perimeter_float():
    """Test perimeter calculation with float values."""
    assert calculate_rectangle_perimeter(2.5, 3.5) == 12.0

def test_rectangle_perimeter_negative_input():
    """Test that negative inputs raise a ValueError."""
    with pytest.raises(ValueError, match="Length and width must be non-negative numbers."):
        calculate_rectangle_perimeter(-1, 5)
    
    with pytest.raises(ValueError, match="Length and width must be non-negative numbers."):
        calculate_rectangle_perimeter(5, -3)