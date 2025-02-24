import pytest
from datetime import datetime, timedelta
from src.date_utils import add_days_to_date

def test_add_days_to_datetime():
    """Test adding days to a datetime object."""
    base_date = datetime(2023, 1, 1)
    result = add_days_to_date(base_date, 5)
    assert result == datetime(2023, 1, 6)

def test_add_days_to_string_date():
    """Test adding days to a date string."""
    result = add_days_to_date('2023-01-01', 5)
    assert result == datetime(2023, 1, 6)

def test_subtract_days():
    """Test subtracting days."""
    base_date = datetime(2023, 1, 10)
    result = add_days_to_date(base_date, -5)
    assert result == datetime(2023, 1, 5)

def test_invalid_date_string():
    """Test handling of invalid date string."""
    with pytest.raises(ValueError, match="Date must be in 'YYYY-MM-DD' format"):
        add_days_to_date('2023/01/01', 5)

def test_invalid_days_type():
    """Test handling of non-integer days."""
    with pytest.raises(TypeError, match="Days must be an integer"):
        add_days_to_date(datetime(2023, 1, 1), '5')

def test_invalid_date_type():
    """Test handling of invalid date type."""
    with pytest.raises(TypeError, match="Date must be a datetime object or a string"):
        add_days_to_date(123, 5)

def test_leap_year():
    """Test adding days across a leap year boundary."""
    result = add_days_to_date('2020-02-28', 1)
    assert result == datetime(2020, 2, 29)

def test_large_day_addition():
    """Test adding a large number of days."""
    base_date = datetime(2023, 1, 1)
    result = add_days_to_date(base_date, 365)
    assert result == datetime(2024, 1, 1)