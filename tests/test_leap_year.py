import pytest
from src.leap_year import is_leap_year

def test_typical_leap_years():
    """Test typical leap years"""
    assert is_leap_year(2000) == True
    assert is_leap_year(2004) == True
    assert is_leap_year(2020) == True
    assert is_leap_year(2024) == True

def test_non_leap_years():
    """Test non-leap years"""
    assert is_leap_year(1900) == False
    assert is_leap_year(2100) == False
    assert is_leap_year(2001) == False
    assert is_leap_year(2003) == False

def test_century_exceptions():
    """Test century years with special leap year rules"""
    assert is_leap_year(2000) == True  # Divisible by 400
    assert is_leap_year(1900) == False  # Divisible by 100 but not 400
    assert is_leap_year(2100) == False  # Divisible by 100 but not 400

def test_invalid_inputs():
    """Test invalid input handling"""
    with pytest.raises(ValueError, match="Year must be an integer"):
        is_leap_year("2020")
    
    with pytest.raises(ValueError, match="Year must be a positive integer"):
        is_leap_year(0)
    
    with pytest.raises(ValueError, match="Year must be a positive integer"):
        is_leap_year(-2020)