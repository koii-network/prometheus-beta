import pytest
from datetime import datetime, timedelta
from src.date_subtractor import subtract_days

def test_subtract_days_datetime():
    """Test subtracting days from a datetime object"""
    date = datetime(2023, 5, 15)
    result = subtract_days(date, 10)
    assert result == datetime(2023, 5, 5)

def test_subtract_days_string():
    """Test subtracting days from an ISO format date string"""
    date = "2023-05-15"
    result = subtract_days(date, 10)
    assert result == datetime(2023, 5, 5)

def test_subtract_zero_days():
    """Test subtracting zero days returns the same date"""
    date = datetime(2023, 5, 15)
    result = subtract_days(date, 0)
    assert result == date

def test_subtract_days_across_month():
    """Test subtracting days across month boundary"""
    date = datetime(2023, 3, 10)
    result = subtract_days(date, 15)
    assert result == datetime(2023, 2, 23)

def test_subtract_days_across_year():
    """Test subtracting days across year boundary"""
    date = datetime(2023, 1, 15)
    result = subtract_days(date, 20)
    assert result == datetime(2022, 12, 26)

def test_invalid_days_type():
    """Test raising TypeError for invalid days type"""
    date = datetime(2023, 5, 15)
    with pytest.raises(TypeError, match="Days must be an integer"):
        subtract_days(date, "10")

def test_negative_days():
    """Test raising ValueError for negative days"""
    date = datetime(2023, 5, 15)
    with pytest.raises(ValueError, match="Number of days to subtract must be non-negative"):
        subtract_days(date, -5)

def test_invalid_date_type():
    """Test raising TypeError for invalid date type"""
    with pytest.raises(TypeError, match="Date must be a datetime object or ISO format string"):
        subtract_days([], 5)

def test_invalid_date_string():
    """Test raising ValueError for invalid date string format"""
    with pytest.raises(ValueError, match="Invalid date format"):
        subtract_days("2023/05/15", 5)