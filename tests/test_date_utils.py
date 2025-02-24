import pytest
from datetime import date
from src.date_utils import get_day_name

def test_get_day_name_date_object():
    """Test get_day_name with a date object"""
    test_date = date(2023, 6, 21)  # Known to be a Wednesday
    assert get_day_name(test_date) == 'Wednesday'

def test_get_day_name_string():
    """Test get_day_name with a valid date string"""
    assert get_day_name('2023-06-21') == 'Wednesday'

def test_get_day_name_invalid_string():
    """Test get_day_name with an invalid date string"""
    with pytest.raises(ValueError, match="Invalid date string"):
        get_day_name('2023/06/21')

def test_get_day_name_invalid_type():
    """Test get_day_name with an invalid input type"""
    with pytest.raises(TypeError, match="Input must be a date object"):
        get_day_name(12345)

def test_get_day_name_different_dates():
    """Test get_day_name with various dates"""
    test_cases = [
        (date(2023, 1, 1), 'Sunday'),
        (date(2023, 12, 25), 'Monday'),
        (date(2024, 2, 29), 'Thursday')  # Leap year
    ]
    
    for test_date, expected_day in test_cases:
        assert get_day_name(test_date) == expected_day