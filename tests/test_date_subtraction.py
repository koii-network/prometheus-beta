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

def test_subtract_days_crossing_month():
    # Test subtraction crossing month boundary
    result = subtract_days_from_date('2023-03-10', 15)
    assert result == datetime(2023, 2, 23)

def test_invalid_days_input():
    # Test invalid days input
    with pytest.raises(ValueError, match="days_to_subtract must be an integer"):
        subtract_days_from_date(datetime(2023, 5, 15), '10')
    
    with pytest.raises(ValueError, match="days_to_subtract must be a non-negative integer"):
        subtract_days_from_date(datetime(2023, 5, 15), -5)

def test_invalid_date_input():
    # Test invalid date input
    with pytest.raises(ValueError, match="input_date string must be in format 'YYYY-MM-DD'"):
        subtract_days_from_date('2023/05/15', 10)
    
    with pytest.raises(ValueError, match="input_date must be a datetime or a string in 'YYYY-MM-DD' format"):
        subtract_days_from_date(123, 10)