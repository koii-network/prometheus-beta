import pytest
from datetime import datetime, timedelta
from src.date_subtraction import subtract_days_from_date

def test_subtract_days_from_datetime():
    # Test subtracting days from a datetime object
    date = datetime(2023, 5, 15)
    result = subtract_days_from_date(date, 10)
    assert result == datetime(2023, 5, 5)

def test_subtract_days_from_string():
    # Test subtracting days from a date string
    result = subtract_days_from_date('2023-05-15', 10)
    assert result == datetime(2023, 5, 5)

def test_subtract_zero_days():
    # Test subtracting 0 days
    date = datetime(2023, 5, 15)
    result = subtract_days_from_date(date, 0)
    assert result == date

def test_invalid_date_format():
    # Test invalid date string format
    with pytest.raises(ValueError, match="Input date must be in 'YYYY-MM-DD' format"):
        subtract_days_from_date('15-05-2023', 10)

def test_invalid_date_type():
    # Test invalid date type
    with pytest.raises(ValueError, match="Input date must be a datetime object or a string"):
        subtract_days_from_date(123, 10)

def test_negative_days_to_subtract():
    # Test negative days to subtract
    with pytest.raises(ValueError, match="Days to subtract must be a non-negative integer"):
        subtract_days_from_date(datetime(2023, 5, 15), -5)

def test_non_integer_days():
    # Test non-integer days to subtract
    with pytest.raises(ValueError, match="Days to subtract must be an integer"):
        subtract_days_from_date(datetime(2023, 5, 15), 5.5)