import pytest
from datetime import datetime
from src.day_of_week import get_day_of_week

def test_get_day_of_week_string_input():
    # Known date with a specific day
    assert get_day_of_week('2023-06-21') == 'Wednesday'
    assert get_day_of_week('2023-12-25') == 'Monday'

def test_get_day_of_week_datetime_input():
    # Test with datetime object
    date = datetime(2023, 6, 21)
    assert get_day_of_week(date) == 'Wednesday'

def test_get_day_of_week_invalid_string_format():
    # Test invalid date string formats
    with pytest.raises(ValueError, match="Invalid date format"):
        get_day_of_week('21-06-2023')  # wrong format
        get_day_of_week('June 21, 2023')  # wrong format

def test_get_day_of_week_invalid_input():
    # Test invalid input types
    with pytest.raises(ValueError, match="Input must be a date string or datetime object"):
        get_day_of_week(12345)
        get_day_of_week(None)
        get_day_of_week([])