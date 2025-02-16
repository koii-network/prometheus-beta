import pytest
from src.leap_year import is_leap_year

def test_typical_leap_years():
    """Test typical leap years divisible by 4"""
    assert is_leap_year(2020) == True
    assert is_leap_year(2024) == True
    assert is_leap_year(2000) == True

def test_non_leap_years():
    """Test years that are not leap years"""
    assert is_leap_year(2021) == False
    assert is_leap_year(2022) == False
    assert is_leap_year(2023) == False

def test_century_years():
    """Test century years that are not leap years"""
    assert is_leap_year(1900) == False
    assert is_leap_year(2100) == False

def test_special_century_years():
    """Test century years divisible by 400"""
    assert is_leap_year(2000) == True
    assert is_leap_year(2400) == True

def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        is_leap_year("2020")
    
    with pytest.raises(TypeError):
        is_leap_year(3.14)
    
    with pytest.raises(ValueError):
        is_leap_year(0)
    
    with pytest.raises(ValueError):
        is_leap_year(-2020)