import pytest
from src.rectangle_perimeter import calculate_rectangle_perimeter

def test_positive_rectangle_perimeter():
    """Test perimeter calculation for standard positive rectangle."""
    assert calculate_rectangle_perimeter(5, 3) == 16

def test_zero_dimensions():
    """Test perimeter calculation with zero dimensions."""
    assert calculate_rectangle_perimeter(0, 0) == 0

def test_float_dimensions():
    """Test perimeter calculation with float dimensions."""
    assert calculate_rectangle_perimeter(2.5, 3.5) == 12.0

def test_equal_sides_square():
    """Test perimeter calculation for a square (equal sides)."""
    assert calculate_rectangle_perimeter(4, 4) == 16

def test_negative_length_raises_error():
    """Test that negative length raises a ValueError."""
    with pytest.raises(ValueError, match="Length and width must be non-negative"):
        calculate_rectangle_perimeter(-1, 5)

def test_negative_width_raises_error():
    """Test that negative width raises a ValueError."""
    with pytest.raises(ValueError, match="Length and width must be non-negative"):
        calculate_rectangle_perimeter(5, -1)

def test_non_numeric_input_raises_error():
    """Test that non-numeric inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Length and width must be numeric values"):
        calculate_rectangle_perimeter("5", 3)
    
    with pytest.raises(TypeError, match="Length and width must be numeric values"):
        calculate_rectangle_perimeter(5, "3")
    
    with pytest.raises(TypeError, match="Length and width must be numeric values"):
        calculate_rectangle_perimeter(None, 3)