import pytest
from src.lcm import calculate_lcm

def test_lcm_basic():
    """Test basic LCM calculations"""
    assert calculate_lcm(4, 6) == 12
    assert calculate_lcm(21, 6) == 42
    assert calculate_lcm(17, 5) == 85

def test_lcm_zero():
    """Test LCM with zero"""
    assert calculate_lcm(0, 5) == 0
    assert calculate_lcm(5, 0) == 0
    assert calculate_lcm(0, 0) == 0

def test_lcm_same_number():
    """Test LCM of the same number"""
    assert calculate_lcm(7, 7) == 7
    assert calculate_lcm(13, 13) == 13

def test_lcm_one():
    """Test LCM with 1"""
    assert calculate_lcm(1, 5) == 5
    assert calculate_lcm(5, 1) == 5

def test_large_numbers():
    """Test LCM with larger numbers"""
    assert calculate_lcm(100, 75) == 300
    assert calculate_lcm(48, 180) == 720

def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    # Test non-integer inputs
    with pytest.raises(TypeError):
        calculate_lcm(4.5, 6)
    with pytest.raises(TypeError):
        calculate_lcm(4, '6')
    with pytest.raises(TypeError):
        calculate_lcm('4', 6)
    
    # Test negative inputs
    with pytest.raises(ValueError):
        calculate_lcm(-4, 6)
    with pytest.raises(ValueError):
        calculate_lcm(4, -6)
    with pytest.raises(ValueError):
        calculate_lcm(-4, -6)