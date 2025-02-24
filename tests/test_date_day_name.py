import pytest
from datetime import datetime
from src.date_day_name import get_day_name

def test_get_day_name_string_input():
    """Test getting day name from a date string"""
    assert get_day_name('2023-06-21') == 'Wednesday'
    assert get_day_name('2023-01-01') == 'Sunday'

def test_get_day_name_datetime_input():
    """Test getting day name from a datetime object"""
    date = datetime(2023, 6, 21)
    assert get_day_name(date) == 'Wednesday'

def test_get_day_name_invalid_string_format():
    """Test error handling for invalid string format"""
    with pytest.raises(ValueError, match="Invalid date format"):
        get_day_name('21-06-2023')

def test_get_day_name_invalid_input_type():
    """Test error handling for invalid input type"""
    with pytest.raises(TypeError, match="Input must be a string or datetime object"):
        get_day_name(12345)

def test_get_day_name_edge_cases():
    """Test various edge cases"""
    # Leap year date
    assert get_day_name('2020-02-29') == 'Saturday'
    
    # Early date
    assert get_day_name('1900-01-01') == 'Monday'
    
    # Future date
    assert get_day_name('2050-12-25') == 'Monday'