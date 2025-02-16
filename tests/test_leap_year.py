import pytest
from src.leap_year import is_leap_year

def test_standard_leap_years():
    """Test typical leap years"""
    assert is_leap_year(2000) == True
    assert is_leap_year(2004) == True
    assert is_leap_year(2020) == True
    assert is_leap_year(2024) == True

def test_non_leap_years():
    """Test typical non-leap years"""
    assert is_leap_year(2100) == False
    assert is_leap_year(2001) == False
    assert is_leap_year(2023) == False
    assert is_leap_year(1900) == False

def test_century_exceptions():
    """Test century years special cases"""
    assert is_leap_year(2000) == True   # Divisible by 400
    assert is_leap_year(1600) == True   # Divisible by 400
    assert is_leap_year(1900) == False  # Divisible by 100 but not 400
    assert is_leap_year(2100) == False  # Divisible by 100 but not 400

def test_edge_invalid_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        is_leap_year("2023")
    
    with pytest.raises(TypeError):
        is_leap_year(2023.5)
    
    with pytest.raises(ValueError):
        is_leap_year(0)
    
    with pytest.raises(ValueError):
        is_leap_year(-2023)