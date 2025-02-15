import pytest
from datetime import datetime, timedelta
from src.date_utils import subtract_days_from_date

def test_subtract_days_from_datetime():
    """Test subtracting days from a datetime object."""
    start_date = datetime(2023, 6, 15)
    result = subtract_days_from_date(start_date, 5)
    assert result == datetime(2023, 6, 10)

def test_subtract_days_from_string_date():
    """Test subtracting days from a date string."""
    result = subtract_days_from_date("2023-06-15", 5)
    assert result == datetime(2023, 6, 10)

def test_subtract_zero_days():
    """Test subtracting zero days."""
    start_date = datetime(2023, 6, 15)
    result = subtract_days_from_date(start_date, 0)
    assert result == start_date

def test_subtract_days_crossing_month():
    """Test subtracting days that cross a month boundary."""
    start_date = datetime(2023, 3, 10)
    result = subtract_days_from_date(start_date, 15)
    assert result == datetime(2023, 2, 23)

def test_invalid_date_format():
    """Test raising an error for an invalid date string format."""
    with pytest.raises(ValueError, match="Invalid date format"):
        subtract_days_from_date("15-06-2023", 5)

def test_negative_days_to_subtract():
    """Test raising an error when trying to subtract negative days."""
    with pytest.raises(ValueError, match="Days to subtract cannot be negative"):
        subtract_days_from_date(datetime(2023, 6, 15), -5)

def test_invalid_input_types():
    """Test raising errors for invalid input types."""
    with pytest.raises(TypeError, match="Input must be a datetime object or a date string"):
        subtract_days_from_date(123, 5)
    
    with pytest.raises(TypeError, match="Days to subtract must be an integer"):
        subtract_days_from_date(datetime(2023, 6, 15), "5")