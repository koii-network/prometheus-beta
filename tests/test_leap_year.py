import pytest
from src.leap_year import is_leap_year

def test_leap_year_divisible_by_4():
    assert is_leap_year(2020) == True
    assert is_leap_year(2024) == True

def test_non_leap_year_not_divisible_by_4():
    assert is_leap_year(2021) == False
    assert is_leap_year(2023) == False

def test_century_years():
    # Century years not divisible by 400 are not leap years
    assert is_leap_year(1900) == False
    assert is_leap_year(2100) == False

def test_leap_century_years():
    # Century years divisible by 400 are leap years
    assert is_leap_year(2000) == True
    assert is_leap_year(2400) == True

def test_invalid_inputs():
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