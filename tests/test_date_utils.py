import pytest
from datetime import datetime, timedelta
from src.date_utils import subtract_days_from_date

def test_subtract_days_from_datetime_object():
    original_date = datetime(2023, 5, 15)
    result = subtract_days_from_date(original_date, 10)
    assert result == datetime(2023, 5, 5)

def test_subtract_days_from_date_string():
    result = subtract_days_from_date("2023-05-15", 10)
    assert result == datetime(2023, 5, 5)

def test_subtract_zero_days():
    original_date = datetime(2023, 5, 15)
    result = subtract_days_from_date(original_date, 0)
    assert result == original_date

def test_subtract_multiple_days_crossing_month():
    result = subtract_days_from_date("2023-03-10", 15)
    assert result == datetime(2023, 2, 23)

def test_invalid_days_type():
    with pytest.raises(TypeError, match="Days must be an integer"):
        subtract_days_from_date(datetime.now(), "10")

def test_invalid_date_type():
    with pytest.raises(TypeError, match="Date must be a datetime object or a string in 'YYYY-MM-DD' format"):
        subtract_days_from_date(123, 10)

def test_invalid_date_string_format():
    with pytest.raises(ValueError, match="Date string must be in format 'YYYY-MM-DD'"):
        subtract_days_from_date("15-05-2023", 10)