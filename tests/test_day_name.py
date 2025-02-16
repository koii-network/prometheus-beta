import pytest
from datetime import datetime
from src.day_name import get_day_name

def test_get_day_name_string_input():
    """Test getting day name from a date string"""
    assert get_day_name('2023-06-21') == 'Wednesday'
    assert get_day_name('2023-06-25') == 'Sunday'

def test_get_day_name_datetime_input():
    """Test getting day name from a datetime object"""
    date = datetime(2023, 6, 21)
    assert get_day_name(date) == 'Wednesday'

def test_get_day_name_invalid_string_format():
    """Test that an invalid string format raises a ValueError"""
    with pytest.raises(ValueError, match="Invalid date format"):
        get_day_name('21-06-2023')  # Wrong format
    with pytest.raises(ValueError, match="Invalid date format"):
        get_day_name('2023/06/21')  # Wrong separator

def test_get_day_name_invalid_input_type():
    """Test that invalid input types raise a TypeError"""
    with pytest.raises(TypeError, match="Input must be a date string or datetime object"):
        get_day_name(20230621)  # Integer input
    with pytest.raises(TypeError, match="Input must be a date string or datetime object"):
        get_day_name(None)  # None input
    with pytest.raises(TypeError, match="Input must be a date string or datetime object"):
        get_day_name([2023, 6, 21])  # List input