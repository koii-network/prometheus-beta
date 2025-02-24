import pytest
from src.leap_year import is_leap_year

def test_standard_leap_years():
    """Test standard leap years divisible by 4"""
    assert is_leap_year(2020) == True
    assert is_leap_year(2024) == True
    assert is_leap_year(2000) == True

def test_non_leap_years():
    """Test non-leap years"""
    assert is_leap_year(2100) == False
    assert is_leap_year(2001) == False
    assert is_leap_year(2022) == False

def test_century_years():
    """Test century years that are leap years"""
    assert is_leap_year(2000) == True
    assert is_leap_year(2400) == True

def test_century_years_not_leap():
    """Test century years that are not leap years"""
    assert is_leap_year(1900) == False
    assert is_leap_year(2100) == False

def test_invalid_input_types():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        is_leap_year("2020")
    with pytest.raises(TypeError):
        is_leap_year(2020.5)
    with pytest.raises(TypeError):
        is_leap_year(None)

def test_invalid_year_values():
    """Test handling of invalid year values"""
    with pytest.raises(ValueError):
        is_leap_year(0)
    with pytest.raises(ValueError):
        is_leap_year(-2020)