import pytest
from datetime import datetime, timedelta
from src.date_subtractor import subtract_days_from_date

def test_subtract_days_from_datetime():
    """Test subtracting days from a datetime object"""
    base_date = datetime(2023, 5, 15)
    result = subtract_days_from_date(base_date, 10)
    assert result == datetime(2023, 5, 5)

def test_subtract_days_from_date_string():
    """Test subtracting days from a date string"""
    base_date = "2023-05-15"
    result = subtract_days_from_date(base_date, 5)
    assert result == datetime(2023, 5, 10)

def test_subtract_zero_days():
    """Test subtracting zero days"""
    base_date = datetime(2023, 5, 15)
    result = subtract_days_from_date(base_date, 0)
    assert result == base_date

def test_invalid_days_to_subtract():
    """Test negative days input"""
    base_date = datetime(2023, 5, 15)
    with pytest.raises(ValueError, match="days_to_subtract must be a non-negative integer"):
        subtract_days_from_date(base_date, -5)

def test_invalid_date_type():
    """Test invalid date input type"""
    with pytest.raises(TypeError, match="date must be a datetime object or an ISO formatted date string"):
        subtract_days_from_date(123, 5)

def test_invalid_days_input():
    """Test invalid days input type"""
    base_date = datetime(2023, 5, 15)
    with pytest.raises(TypeError, match="days_to_subtract must be an integer"):
        subtract_days_from_date(base_date, "5")

def test_invalid_date_string():
    """Test invalid date string format"""
    with pytest.raises(ValueError, match="Invalid date string format"):
        subtract_days_from_date("2023/05/15", 5)