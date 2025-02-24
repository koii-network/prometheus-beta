import pytest
from datetime import datetime, timedelta
from src.date_utils import subtract_days_from_date

def test_subtract_days_from_datetime():
    """Test subtracting days from a datetime object."""
    date = datetime(2023, 5, 15)
    result = subtract_days_from_date(date, 10)
    assert result == datetime(2023, 5, 5)

def test_subtract_days_from_date_string():
    """Test subtracting days from an ISO format date string."""
    date_str = "2023-05-15"
    result = subtract_days_from_date(date_str, 10)
    assert result == datetime(2023, 5, 5)

def test_subtract_zero_days():
    """Test subtracting zero days."""
    date = datetime(2023, 5, 15)
    result = subtract_days_from_date(date, 0)
    assert result == date

def test_subtract_days_crossing_month():
    """Test subtracting days that cross a month boundary."""
    date = datetime(2023, 3, 10)
    result = subtract_days_from_date(date, 15)
    assert result == datetime(2023, 2, 23)

def test_invalid_days_negative():
    """Test raising an error for negative days."""
    date = datetime(2023, 5, 15)
    with pytest.raises(ValueError, match="days_to_subtract must be a non-negative integer"):
        subtract_days_from_date(date, -5)

def test_invalid_days_type():
    """Test raising an error for invalid days type."""
    date = datetime(2023, 5, 15)
    with pytest.raises(TypeError, match="days_to_subtract must be an integer"):
        subtract_days_from_date(date, "10")

def test_invalid_date_string():
    """Test raising an error for invalid date string."""
    with pytest.raises(ValueError, match="Invalid date format"):
        subtract_days_from_date("2023/05/15", 10)

def test_invalid_date_type():
    """Test raising an error for invalid date type."""
    with pytest.raises(TypeError, match="date must be a datetime object or an ISO format string"):
        subtract_days_from_date(12345, 10)