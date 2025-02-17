import pytest
from src.power_of_two import is_power_of_two

def test_powers_of_two():
    """Test known powers of two"""
    assert is_power_of_two(1) == True
    assert is_power_of_two(2) == True
    assert is_power_of_two(4) == True
    assert is_power_of_two(8) == True
    assert is_power_of_two(16) == True
    assert is_power_of_two(1024) == True
    assert is_power_of_two(65536) == True

def test_non_powers_of_two():
    """Test numbers that are not powers of two"""
    assert is_power_of_two(0) == False
    assert is_power_of_two(3) == False
    assert is_power_of_two(5) == False
    assert is_power_of_two(7) == False
    assert is_power_of_two(15) == False
    assert is_power_of_two(100) == False

def test_error_handling():
    """Test error handling for invalid inputs"""
    # Test negative numbers
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        is_power_of_two(-1)
    
    # Test non-integer inputs
    with pytest.raises(TypeError, match="Input must be an integer"):
        is_power_of_two(2.5)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        is_power_of_two("2")
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        is_power_of_two(None)