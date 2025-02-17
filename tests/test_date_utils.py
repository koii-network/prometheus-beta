import pytest
from datetime import datetime, timedelta
from src.date_utils import add_days_to_date

def test_add_days_to_datetime():
    """Test adding days to a datetime object"""
    start_date = datetime(2023, 1, 1)
    result = add_days_to_date(start_date, 5)
    assert result == datetime(2023, 1, 6)

def test_add_days_to_date_string():
    """Test adding days to a date string"""
    result = add_days_to_date('2023-01-01', 5)
    assert result == datetime(2023, 1, 6)

def test_subtract_days():
    """Test subtracting days"""
    start_date = datetime(2023, 1, 10)
    result = add_days_to_date(start_date, -3)
    assert result == datetime(2023, 1, 7)

def test_invalid_date_format():
    """Test invalid date string format"""
    with pytest.raises(ValueError, match="Date must be in 'YYYY-MM-DD' format"):
        add_days_to_date('01-01-2023', 5)

def test_invalid_days_type():
    """Test invalid days type"""
    with pytest.raises(ValueError, match="Days must be an integer"):
        add_days_to_date(datetime(2023, 1, 1), '5')

def test_invalid_date_type():
    """Test invalid date type"""
    with pytest.raises(ValueError, match="Date must be a datetime object or a string"):
        add_days_to_date(123, 5)

def test_large_day_addition():
    """Test adding a large number of days"""
    start_date = datetime(2023, 1, 1)
    result = add_days_to_date(start_date, 365)
    assert result == datetime(2024, 1, 1)

def test_leap_year():
    """Test date addition across a leap year"""
    start_date = datetime(2020, 2, 28)
    result = add_days_to_date(start_date, 1)
    assert result == datetime(2020, 2, 29)