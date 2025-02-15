import pytest
from datetime import datetime
from src.day_name import get_day_name

def test_get_day_name_string_input():
    """Test getting day name from a string date input"""
    assert get_day_name('2023-06-21') == 'Wednesday'
    assert get_day_name('2023-06-22') == 'Thursday'

def test_get_day_name_datetime_input():
    """Test getting day name from a datetime input"""
    date_obj = datetime(2023, 6, 21)
    assert get_day_name(date_obj) == 'Wednesday'

def test_get_day_name_invalid_string_format():
    """Test error handling for invalid string date format"""
    with pytest.raises(ValueError, match="Invalid date format"):
        get_day_name('21-06-2023')  # Wrong format
    
    with pytest.raises(ValueError, match="Invalid date format"):
        get_day_name('2023/06/21')  # Wrong separator

def test_get_day_name_invalid_input_type():
    """Test error handling for invalid input types"""
    with pytest.raises(ValueError, match="Input must be"):
        get_day_name(20230621)  # Integer input
    
    with pytest.raises(ValueError, match="Input must be"):
        get_day_name(None)  # None input

def test_get_day_name_edge_cases():
    """Test edge cases with different dates"""
    assert get_day_name('2000-02-29') == 'Tuesday'  # Leap year
    assert get_day_name('2023-12-31') == 'Sunday'  # Year end
    assert get_day_name('2023-01-01') == 'Sunday'  # Year start