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
    """Test subtracting zero days."""
    date = datetime(2023, 5, 15)
    result = subtract_days_from_date(date, 0)
    assert result == date

def test_subtract_days_across_month():
    """Test subtracting days across month boundary."""
    date = datetime(2023, 3, 10)
    result = subtract_days_from_date(date, 15)
    assert result == datetime(2023, 2, 23)

def test_invalid_days_input():
    """Test that TypeError is raised for non-integer days."""
    with pytest.raises(TypeError):
        subtract_days_from_date(datetime.now(), "10")
    with pytest.raises(TypeError):
        subtract_days_from_date(datetime.now(), 3.5)

def test_invalid_date_input():
    """Test that TypeError is raised for invalid date input."""
    with pytest.raises(TypeError):
        subtract_days_from_date(123, 10)

def test_invalid_date_string():
    """Test that ValueError is raised for incorrectly formatted date string."""
    with pytest.raises(ValueError):
        subtract_days_from_date("2023/05/15", 10)
    with pytest.raises(ValueError):
        subtract_days_from_date("invalid-date", 10)