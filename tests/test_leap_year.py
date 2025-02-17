import pytest
from src.leap_year import is_leap_year

def test_typical_leap_years():
    """Test typical leap years"""
    assert is_leap_year(2000) == True
    assert is_leap_year(2020) == True
    assert is_leap_year(2024) == True

def test_non_leap_years():
    """Test typical non-leap years"""
    assert is_leap_year(2100) == False
    assert is_leap_year(2019) == False
    assert is_leap_year(2021) == False

def test_century_years():
    """Test century years with special leap year rules"""
    assert is_leap_year(1900) == False  # Not divisible by 400
    assert is_leap_year(2000) == True   # Divisible by 400
    assert is_leap_year(2400) == True   # Divisible by 400

def test_edge_cases():
    """Test edge case years"""
    assert is_leap_year(0) == True  # 0 is considered a leap year
    assert is_leap_year(4) == True

def test_error_handling():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        is_leap_year("2020")
    
    with pytest.raises(TypeError):
        is_leap_year(2020.5)
    
    with pytest.raises(ValueError):
        is_leap_year(-2020)