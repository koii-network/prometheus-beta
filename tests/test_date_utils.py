import pytest
from datetime import datetime, timedelta
from src.date_utils import add_days_to_date

def test_add_days_to_date_string_input():
    """Test adding days to a date string input"""
    result = add_days_to_date('2023-01-01', 5)
    assert result == datetime(2023, 1, 6)

def test_add_days_to_date_datetime_input():
    """Test adding days to a datetime input"""
    input_date = datetime(2023, 1, 1)
    result = add_days_to_date(input_date, 10)
    assert result == datetime(2023, 1, 11)

def test_add_zero_days():
    """Test adding zero days"""
    result = add_days_to_date('2023-01-01', 0)
    assert result == datetime(2023, 1, 1)

def test_add_negative_days():
    """Test subtracting days"""
    result = add_days_to_date('2023-01-15', -5)
    assert result == datetime(2023, 1, 10)

def test_invalid_date_string():
    """Test invalid date string format"""
    with pytest.raises(ValueError, match="Input date must be in 'YYYY-MM-DD' format"):
        add_days_to_date('01-01-2023', 5)

def test_invalid_input_type():
    """Test invalid input type"""
    with pytest.raises(ValueError, match="Input must be a datetime object or a date string"):
        add_days_to_date(123, 5)

def test_invalid_days_type():
    """Test invalid days type"""
    with pytest.raises(ValueError, match="Days to add must be an integer"):
        add_days_to_date('2023-01-01', '5')

def test_leap_year_handling():
    """Test handling of leap years"""
    result = add_days_to_date('2020-02-28', 1)
    assert result == datetime(2020, 2, 29)

def test_non_leap_year_handling():
    """Test handling of non-leap years"""
    result = add_days_to_date('2021-02-28', 1)
    assert result == datetime(2021, 3, 1)