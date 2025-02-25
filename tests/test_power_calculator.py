import pytest
import sys
import os

# Add project root to path to import the module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.power_calculator import recursive_power

def test_basic_power_calculation():
    """Test basic power calculations"""
    assert recursive_power(2, 3) == 8
    assert recursive_power(5, 2) == 25
    assert recursive_power(10, 0) == 1
    assert recursive_power(3, 1) == 3

def test_zero_cases():
    """Test edge cases involving zero"""
    assert recursive_power(0, 0) == 1
    assert recursive_power(0, 5) == 0
    assert recursive_power(7, 0) == 1

def test_float_base():
    """Test power calculations with float bases"""
    assert recursive_power(2.5, 2) == 6.25
    assert recursive_power(1.5, 3) == 3.375

def test_negative_exponent_error():
    """Test that negative exponents raise a ValueError"""
    with pytest.raises(ValueError, match="Exponent cannot be negative"):
        recursive_power(2, -1)

def test_type_errors():
    """Test type checking"""
    with pytest.raises(TypeError, match="Base must be a number"):
        recursive_power("2", 3)
    
    with pytest.raises(TypeError, match="Exponent must be an integer"):
        recursive_power(2, 3.5)
    
    with pytest.raises(TypeError, match="Base must be a number"):
        recursive_power(None, 3)
    
    with pytest.raises(TypeError, match="Exponent must be an integer"):
        recursive_power(2, None)