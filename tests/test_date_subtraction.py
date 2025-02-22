import pytest
from datetime import datetime, timedelta
from src.date_subtraction import subtract_days_from_date

def test_subtract_days_from_datetime():
    # Test subtracting days from a datetime object
    date = datetime(2023, 5, 15)
    result = subtract_days_from_date(date, 10)
    assert result == datetime(2023, 5, 5)

def test_subtract_days_from_string_date():
    # Test subtracting days from a date string
    date_str = '2023-05-15'
    result = subtract_days_from_date(date_str, 10)
    assert result == datetime(2023, 5, 5)

def test_subtract_zero_days():
    # Test subtracting zero days
    date = datetime(2023, 5, 15)
    result = subtract_days_from_date(date, 0)
    assert result == date

def test_subtract_multiple_days():
    # Test subtracting multiple days
    date = datetime(2023, 5, 15)
    result = subtract_days_from_date(date, 50)
    assert result == datetime(2023, 3, 26)

def test_invalid_date_type():
    # Test invalid date type
    with pytest.raises(TypeError):
        subtract_days_from_date(123, 10)

def test_invalid_days_type():
    # Test invalid days type
    with pytest.raises(TypeError):
        subtract_days_from_date(datetime(2023, 5, 15), '10')

def test_invalid_date_string_format():
    # Test invalid date string format
    with pytest.raises(ValueError):
        subtract_days_from_date('2023/05/15', 10)

def test_cross_month_subtraction():
    # Test subtraction that crosses month boundary
    date = datetime(2023, 3, 15)
    result = subtract_days_from_date(date, 20)
    assert result == datetime(2023, 2, 23)