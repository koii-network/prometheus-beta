import pytest
from datetime import date
from src.day_name import get_day_name

def test_get_day_name_date_object():
    """Test with a date object input."""
    test_date = date(2023, 7, 4)  # A Tuesday
    assert get_day_name(test_date) == 'Tuesday'

def test_get_day_name_string_input():
    """Test with a valid date string input."""
    assert get_day_name('2023-07-04') == 'Tuesday'

def test_get_day_name_different_dates():
    """Test multiple different dates."""
    test_cases = [
        (date(2023, 1, 1), 'Sunday'),    # New Year's Day 2023
        (date(2023, 12, 25), 'Monday'),  # Christmas 2023
        (date(2024, 2, 29), 'Thursday'), # Leap day 2024
    ]
    
    for test_date, expected_day in test_cases:
        assert get_day_name(test_date) == expected_day

def test_invalid_string_format():
    """Test invalid string date format raises ValueError."""
    with pytest.raises(ValueError, match="Invalid date format"):
        get_day_name('07-04-2023')  # Wrong format

def test_invalid_input_type():
    """Test invalid input type raises ValueError."""
    with pytest.raises(ValueError, match="Input must be a date object"):
        get_day_name(20230704)  # Integer input

def test_none_input():
    """Test None input raises ValueError."""
    with pytest.raises(ValueError, match="Input must be a date object"):
        get_day_name(None)