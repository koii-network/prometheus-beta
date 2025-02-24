import pytest
from src.leap_year import is_leap_year

def test_typical_leap_years():
    """Test typical leap years"""
    assert is_leap_year(2020) == True
    assert is_leap_year(2024) == True

def test_non_leap_years():
    """Test typical non-leap years"""
    assert is_leap_year(2021) == False
    assert is_leap_year(2022) == False
    assert is_leap_year(2023) == False

def test_century_years():
    """Test century years which are not leap years"""
    assert is_leap_year(1900) == False
    assert is_leap_year(2100) == False

def test_exceptional_century_years():
    """Test century years divisible by 400 which are leap years"""
    assert is_leap_year(2000) == True
    assert is_leap_year(2400) == True

def test_edge_cases():
    """Test edge case years"""
    assert is_leap_year(4) == True  # Earliest leap year
    assert is_leap_year(400) == True  # Century leap year

def test_error_handling():
    """Test error handling for invalid inputs"""
    # Test non-integer inputs
    with pytest.raises(TypeError):
        is_leap_year("2020")
    with pytest.raises(TypeError):
        is_leap_year(2020.5)
    
    # Test non-positive inputs
    with pytest.raises(ValueError):
        is_leap_year(0)
    with pytest.raises(ValueError):
        is_leap_year(-2020)