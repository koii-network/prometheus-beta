import pytest
from src.leap_year import is_leap_year

def test_typical_leap_years():
    # Years divisible by 4 but not 100
    assert is_leap_year(2020) == True
    assert is_leap_year(2024) == True

def test_century_years():
    # Years divisible by 100 but also by 400 are leap years
    assert is_leap_year(2000) == True
    
    # Years divisible by 100 but not by 400 are not leap years
    assert is_leap_year(1900) == False

def test_non_leap_years():
    # Years not divisible by 4
    assert is_leap_year(2021) == False
    assert is_leap_year(2023) == False

def test_error_handling():
    # Test invalid input types
    with pytest.raises(TypeError):
        is_leap_year("2020")
    
    with pytest.raises(TypeError):
        is_leap_year(2020.5)
    
    # Test invalid year values
    with pytest.raises(ValueError):
        is_leap_year(0)
    
    with pytest.raises(ValueError):
        is_leap_year(-2020)

def test_early_and_future_years():
    # Test some early and future years
    assert is_leap_year(1600) == True   # Divisible by 400
    assert is_leap_year(2400) == True   # Future year divisible by 400
    assert is_leap_year(2100) == False  # Divisible by 100 but not 400