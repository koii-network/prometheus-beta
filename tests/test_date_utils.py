import pytest
from datetime import datetime, timedelta
from src.date_utils import subtract_days_from_date

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
    """Test subtracting zero days."""
    date = datetime(2023, 5, 15)
    result = subtract_days_from_date(date, 0)
    assert result == date

def test_subtract_days_across_month():
    """Test subtracting days that cross month boundary."""
    date = datetime(2023, 3, 10)
    result = subtract_days_from_date(date, 15)
    assert result == datetime(2023, 2, 23)

def test_invalid_days_input_negative():
    """Test that negative number of days raises ValueError."""
    with pytest.raises(ValueError, match="days_to_subtract must be a non-negative integer"):
        subtract_days_from_date(datetime(2023, 5, 15), -5)

def test_invalid_days_input_non_integer():
    """Test that non-integer days input raises ValueError."""
    with pytest.raises(ValueError, match="days_to_subtract must be an integer"):
        subtract_days_from_date(datetime(2023, 5, 15), "10")

def test_invalid_date_string():
    """Test that an incorrectly formatted date string raises ValueError."""
    with pytest.raises(ValueError, match="Invalid date string"):
        subtract_days_from_date("2023/05/15", 10)

def test_invalid_date_type():
    """Test that an invalid date type raises ValueError."""
    with pytest.raises(ValueError, match="Input must be a datetime object or a date string"):
        subtract_days_from_date(123, 10)