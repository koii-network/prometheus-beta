import pytest
from src.lcm import calculate_lcm

def test_lcm_basic_cases():
    """Test basic LCM calculations"""
    assert calculate_lcm(4, 6) == 12
    assert calculate_lcm(21, 6) == 42
    assert calculate_lcm(5, 7) == 35
    assert calculate_lcm(2, 3) == 6

def test_lcm_same_number():
    """Test LCM when both numbers are the same"""
    assert calculate_lcm(5, 5) == 5
    assert calculate_lcm(10, 10) == 10

def test_lcm_one_number_multiple():
    """Test LCM when one number is a multiple of the other"""
    assert calculate_lcm(3, 9) == 9
    assert calculate_lcm(8, 16) == 16

def test_lcm_coprime_numbers():
    """Test LCM for coprime numbers"""
    assert calculate_lcm(7, 11) == 77
    assert calculate_lcm(13, 17) == 221

def test_lcm_invalid_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Both inputs must be integers"):
        calculate_lcm(4.5, 6)
    
    with pytest.raises(ValueError, match="Both inputs must be positive integers"):
        calculate_lcm(0, 5)
    
    with pytest.raises(ValueError, match="Both inputs must be positive integers"):
        calculate_lcm(-3, 6)
    
    with pytest.raises(ValueError, match="Both inputs must be positive integers"):
        calculate_lcm(-1, -1)