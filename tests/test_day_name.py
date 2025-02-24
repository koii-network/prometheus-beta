import pytest
from datetime import date
from src.day_name import get_day_name

def test_get_day_name_date_object():
    """Test getting day name from a date object"""
    test_date = date(2023, 6, 21)  # Wednesday
    assert get_day_name(test_date) == 'Wednesday'

def test_get_day_name_string():
    """Test getting day name from a date string"""
    test_date_str = '2023-06-21'  # Wednesday
    assert get_day_name(test_date_str) == 'Wednesday'

def test_get_day_name_different_dates():
    """Test multiple different dates"""
    test_cases = [
        (date(2023, 1, 1), 'Sunday'),     # New Year's Day 2023
        (date(2023, 12, 25), 'Monday'),   # Christmas Day 2023
        (date(2024, 2, 29), 'Thursday')   # Leap day 2024
    ]
    
    for test_date, expected_day in test_cases:
        assert get_day_name(test_date) == expected_day
        assert get_day_name(test_date.strftime('%Y-%m-%d')) == expected_day

def test_invalid_date_string():
    """Test handling of invalid date string"""
    with pytest.raises(ValueError, match="Invalid date string"):
        get_day_name('2023/06/21')  # Wrong format
    
    with pytest.raises(ValueError, match="Invalid date string"):
        get_day_name('invalid-date')

def test_invalid_input_type():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        get_day_name(20230621)  # Integer
    
    with pytest.raises(TypeError):
        get_day_name(None)
    
    with pytest.raises(TypeError):
        get_day_name(['2023-06-21'])  # List