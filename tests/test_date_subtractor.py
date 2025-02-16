import pytest
from datetime import datetime, timedelta
from src.date_subtractor import subtract_days_from_date

def test_subtract_days_from_datetime():
    """Test subtracting days from a datetime object."""
    date = datetime(2023, 5, 15)
    result = subtract_days_from_date(date, 10)
    assert result == datetime(2023, 5, 5)

def test_subtract_days_from_string():
    """Test subtracting days from a date string."""
    date_str = '2023-05-15'
    result = subtract_days_from_date(date_str, 10)
    assert result == datetime(2023, 5, 5)

def test_subtract_zero_days():
    """Test subtracting zero days returns the same date."""
    date = datetime(2023, 5, 15)
    result = subtract_days_from_date(date, 0)
    assert result == date

def test_invalid_date_format():
    """Test that an invalid date format raises a ValueError."""
    with pytest.raises(ValueError, match="Invalid date format"):
        subtract_days_from_date('15-05-2023', 10)

def test_negative_days_subtraction():
    """Test that negative days raise a ValueError."""
    with pytest.raises(ValueError, match="Days to subtract cannot be negative"):
        subtract_days_from_date(datetime(2023, 5, 15), -5)

def test_invalid_input_type():
    """Test that invalid input types raise a TypeError."""
    with pytest.raises(TypeError):
        subtract_days_from_date(12345, 10)
    
    with pytest.raises(TypeError):
        subtract_days_from_date(datetime(2023, 5, 15), '10')