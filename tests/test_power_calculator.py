import pytest
from src.power_calculator import recursive_power

def test_positive_exponents():
    """Test power calculation with various positive exponents."""
    assert recursive_power(2, 0) == 1
    assert recursive_power(2, 1) == 2
    assert recursive_power(2, 2) == 4
    assert recursive_power(2, 3) == 8
    assert recursive_power(3, 3) == 27

def test_float_base():
    """Test power calculation with float bases."""
    assert recursive_power(2.5, 2) == 6.25
    assert recursive_power(1.5, 3) == 3.375

def test_edge_cases():
    """Test edge cases for power calculation."""
    assert recursive_power(5, 0) == 1
    assert recursive_power(1, 10) == 1

def test_type_errors():
    """Test error handling for incorrect input types."""
    with pytest.raises(TypeError, match="Base must be a number"):
        recursive_power("2", 2)
    
    with pytest.raises(TypeError, match="Exponent must be an integer"):
        recursive_power(2, 2.5)

def test_negative_exponent_error():
    """Test that negative exponents raise a ValueError."""
    with pytest.raises(ValueError, match="Exponent must be non-negative"):
        recursive_power(2, -1)