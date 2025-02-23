import pytest
from src.lcm import find_lcm

def test_lcm_basic_numbers():
    """Test LCM for basic positive integers"""
    assert find_lcm(4, 6) == 12
    assert find_lcm(21, 6) == 42
    assert find_lcm(17, 5) == 85

def test_lcm_same_number():
    """Test LCM when both numbers are the same"""
    assert find_lcm(7, 7) == 7

def test_lcm_one_multiple_of_other():
    """Test LCM when one number is a multiple of the other"""
    assert find_lcm(3, 9) == 9
    assert find_lcm(9, 3) == 9

def test_lcm_coprime_numbers():
    """Test LCM for coprime numbers"""
    assert find_lcm(5, 7) == 35

def test_invalid_input_types():
    """Test that non-integer inputs raise ValueError"""
    with pytest.raises(ValueError, match="Inputs must be integers"):
        find_lcm(3.5, 4)
    with pytest.raises(ValueError, match="Inputs must be integers"):
        find_lcm("4", 5)

def test_invalid_non_positive_numbers():
    """Test that non-positive inputs raise ValueError"""
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        find_lcm(0, 5)
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        find_lcm(-3, 4)
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        find_lcm(3, -4)
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        find_lcm(0, 0)