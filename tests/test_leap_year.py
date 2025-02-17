import pytest
from src.leap_year import is_leap_year

def test_typical_leap_years():
    # Years divisible by 4 but not 100 are leap years
    assert is_leap_year(2020) == True
    assert is_leap_year(2024) == True
    assert is_leap_year(2028) == True

def test_non_leap_years():
    # Years not divisible by 4 are not leap years
    assert is_leap_year(2021) == False
    assert is_leap_year(2023) == False
    assert is_leap_year(2025) == False

def test_century_years():
    # Century years (divisible by 100) are not leap years, except those divisible by 400
    assert is_leap_year(1900) == False  # Not divisible by 400
    assert is_leap_year(2000) == True   # Divisible by 400
    assert is_leap_year(2100) == False  # Not divisible by 400

def test_early_leap_years():
    # Check some historical leap years
    assert is_leap_year(1600) == True
    assert is_leap_year(1804) == True

def test_edge_cases():
    # Minimum year
    assert is_leap_year(4) == True

def test_invalid_inputs():
    # Test type and value errors
    with pytest.raises(TypeError):
        is_leap_year("2020")
    
    with pytest.raises(TypeError):
        is_leap_year(2020.5)
    
    with pytest.raises(ValueError):
        is_leap_year(0)
    
    with pytest.raises(ValueError):
        is_leap_year(-2020)