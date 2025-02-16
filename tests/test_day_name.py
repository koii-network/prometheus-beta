import pytest
from datetime import datetime
from src.day_name import get_day_name

def test_get_day_name_string_input():
    """Test get_day_name with string input"""
    assert get_day_name('2023-06-14') == 'Wednesday'
    assert get_day_name('2023-06-15') == 'Thursday'
    assert get_day_name('2023-06-16') == 'Friday'

def test_get_day_name_datetime_input():
    """Test get_day_name with datetime input"""
    date = datetime(2023, 6, 14)
    assert get_day_name(date) == 'Wednesday'

def test_get_day_name_invalid_format():
    """Test get_day_name with invalid date format"""
    with pytest.raises(ValueError, match="Invalid date format"):
        get_day_name('14-06-2023')

def test_get_day_name_invalid_type():
    """Test get_day_name with invalid input type"""
    with pytest.raises(TypeError, match="Input must be"):
        get_day_name(20230614)
        get_day_name(None)