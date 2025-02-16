import pytest
from datetime import datetime, timedelta
from src.date_utils import subtract_days_from_date

def test_subtract_days_from_datetime():
    """Test subtracting days from a datetime object."""
    base_date = datetime(2023, 5, 15)
    result = subtract_days_from_date(base_date, 10)
    assert result == datetime(2023, 5, 5)

def test_subtract_days_from_date_string():
    """Test subtracting days from an ISO format date string."""
    base_date = "2023-05-15"
    result = subtract_days_from_date(base_date, 10)
    assert result == datetime(2023, 5, 5)

def test_subtract_zero_days():
    """Test subtracting zero days returns the same date."""
    base_date = datetime(2023, 5, 15)
    result = subtract_days_from_date(base_date, 0)
    assert result == base_date

def test_subtract_days_across_month_boundary():
    """Test subtracting days across a month boundary."""
    base_date = datetime(2023, 3, 10)
    result = subtract_days_from_date(base_date, 15)
    assert result == datetime(2023, 2, 23)

def test_invalid_days_input_type():
    """Test raising TypeError for invalid days input type."""
    base_date = datetime(2023, 5, 15)
    with pytest.raises(TypeError, match="days_to_subtract must be an integer"):
        subtract_days_from_date(base_date, "10")

def test_negative_days_input():
    """Test raising ValueError for negative days input."""
    base_date = datetime(2023, 5, 15)
    with pytest.raises(ValueError, match="days_to_subtract must be a non-negative integer"):
        subtract_days_from_date(base_date, -5)

def test_invalid_date_input():
    """Test raising TypeError for invalid date input."""
    with pytest.raises(TypeError, match="date must be a datetime object or an ISO format date string"):
        subtract_days_from_date(123, 10)

def test_invalid_date_string():
    """Test raising TypeError for invalid date string."""
    with pytest.raises(TypeError, match="date must be a datetime object or an ISO format date string"):
        subtract_days_from_date("2023/05/15", 10)