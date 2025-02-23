import pytest
from datetime import datetime, timedelta
from src.date_subtractor import subtract_days_from_date

def test_subtract_days_from_datetime():
    """Test subtracting days from a datetime object."""
    date = datetime(2023, 5, 15)
    result = subtract_days_from_date(date, 10)
    assert result == datetime(2023, 5, 5)

def test_subtract_days_from_date_string():
    """Test subtracting days from a date string."""
    date_str = "2023-05-15"
    result = subtract_days_from_date(date_str, 10)
    assert result == datetime(2023, 5, 5)

def test_subtract_zero_days():
    """Test subtracting zero days returns the same date."""
    date = datetime(2023, 5, 15)
    result = subtract_days_from_date(date, 0)
    assert result == date

def test_subtract_many_days():
    """Test subtracting a large number of days."""
    date = datetime(2023, 5, 15)
    result = subtract_days_from_date(date, 100)
    assert result == datetime(2023, 2, 4)

def test_invalid_date_type():
    """Test that an invalid date type raises a TypeError."""
    with pytest.raises(TypeError, match="Date must be a datetime object or a string in ISO format"):
        subtract_days_from_date(123, 10)

def test_invalid_date_string():
    """Test that an invalid date string raises a TypeError."""
    with pytest.raises(TypeError, match="Date must be a datetime object or a string in ISO format"):
        subtract_days_from_date("invalid-date", 10)

def test_negative_days():
    """Test that negative days raise a ValueError."""
    with pytest.raises(ValueError, match="Days to subtract must be a non-negative integer"):
        subtract_days_from_date(datetime(2023, 5, 15), -5)

def test_non_integer_days():
    """Test that non-integer days raise a TypeError."""
    with pytest.raises(TypeError, match="Days to subtract must be an integer"):
        subtract_days_from_date(datetime(2023, 5, 15), "10")