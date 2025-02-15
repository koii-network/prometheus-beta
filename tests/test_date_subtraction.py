import pytest
from datetime import datetime, timedelta
from src.date_subtraction import subtract_days_from_date

def test_subtract_days_from_datetime():
    """Test subtracting days from a datetime object."""
    original_date = datetime(2023, 5, 15)
    result = subtract_days_from_date(original_date, 10)
    assert result == datetime(2023, 5, 5)

def test_subtract_days_from_string_date():
    """Test subtracting days from a date string."""
    result = subtract_days_from_date('2023-05-15', 10)
    assert result == datetime(2023, 5, 5)

def test_zero_days_subtraction():
    """Test subtracting zero days."""
    original_date = datetime(2023, 5, 15)
    result = subtract_days_from_date(original_date, 0)
    assert result == original_date

def test_invalid_date_string():
    """Test invalid date string format."""
    with pytest.raises(ValueError, match="Invalid date format"):
        subtract_days_from_date('2023/05/15', 10)

def test_negative_days_subtraction():
    """Test raising error for negative days."""
    with pytest.raises(ValueError, match="days_to_subtract cannot be negative"):
        subtract_days_from_date(datetime(2023, 5, 15), -5)

def test_invalid_days_type():
    """Test raising error for invalid days type."""
    with pytest.raises(ValueError, match="days_to_subtract must be an integer"):
        subtract_days_from_date(datetime(2023, 5, 15), '10')