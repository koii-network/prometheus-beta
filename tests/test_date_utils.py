import pytest
from datetime import datetime, date, timedelta
from src.date_utils import add_days_to_date

def test_add_days_to_datetime():
    """Test adding days to a datetime object."""
    start_date = datetime(2023, 1, 1)
    result = add_days_to_date(start_date, 5)
    assert result == datetime(2023, 1, 6).date()

def test_add_days_to_date():
    """Test adding days to a date object."""
    start_date = date(2023, 1, 1)
    result = add_days_to_date(start_date, 5)
    assert result == date(2023, 1, 6)

def test_add_days_to_iso_string():
    """Test adding days to an ISO formatted date string."""
    start_date = "2023-01-01"
    result = add_days_to_date(start_date, 5)
    assert result == date(2023, 1, 6)

def test_add_zero_days():
    """Test adding zero days."""
    start_date = datetime(2023, 1, 1)
    result = add_days_to_date(start_date, 0)
    assert result == datetime(2023, 1, 1).date()

def test_add_negative_days():
    """Test adding negative days."""
    start_date = datetime(2023, 1, 10)
    result = add_days_to_date(start_date, -5)
    assert result == datetime(2023, 1, 5).date()

def test_invalid_date_type():
    """Test raising TypeError for invalid date type."""
    with pytest.raises(TypeError):
        add_days_to_date(123, 5)

def test_invalid_date_string():
    """Test raising TypeError for invalid date string."""
    with pytest.raises(TypeError):
        add_days_to_date("invalid-date", 5)

def test_invalid_days_type():
    """Test raising ValueError for non-integer days."""
    with pytest.raises(ValueError):
        add_days_to_date(datetime(2023, 1, 1), "5")

def test_leap_year():
    """Test adding days across a leap year."""
    start_date = "2020-02-28"
    result = add_days_to_date(start_date, 1)
    assert result == date(2020, 2, 29)

def test_end_of_year():
    """Test adding days that cross year boundary."""
    start_date = datetime(2022, 12, 28)
    result = add_days_to_date(start_date, 5)
    assert result == datetime(2023, 1, 2).date()