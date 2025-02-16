import pytest
from datetime import datetime, timedelta
from src.date_utils import add_days_to_date

def test_add_days_to_date_string_input():
    # Test adding days to a date provided as a string
    result = add_days_to_date('2023-05-15', 10)
    assert result == datetime(2023, 5, 25)

def test_add_days_to_date_datetime_input():
    # Test adding days to a date provided as a datetime object
    input_date = datetime(2023, 5, 15)
    result = add_days_to_date(input_date, 10)
    assert result == datetime(2023, 5, 25)

def test_add_negative_days():
    # Test subtracting days
    result = add_days_to_date('2023-05-15', -5)
    assert result == datetime(2023, 5, 10)

def test_invalid_date_format():
    # Test invalid date string format
    with pytest.raises(ValueError, match="Date must be in 'YYYY-MM-DD' format"):
        add_days_to_date('15-05-2023', 10)

def test_invalid_days_type():
    # Test invalid type for number of days
    with pytest.raises(ValueError, match="Number of days must be an integer"):
        add_days_to_date('2023-05-15', '10')

def test_leap_year():
    # Test adding days across a leap year boundary
    result = add_days_to_date('2024-02-28', 1)
    assert result == datetime(2024, 2, 29)

def test_non_leap_year():
    # Test adding days across a non-leap year boundary
    result = add_days_to_date('2023-02-28', 1)
    assert result == datetime(2023, 3, 1)