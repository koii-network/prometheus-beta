import pytest
from datetime import datetime, timedelta
from src.date_utils import add_days_to_date

def test_add_days_to_date_string_input():
    result = add_days_to_date("2023-07-15", 5)
    assert result == datetime(2023, 7, 20)

def test_add_days_to_date_datetime_input():
    input_date = datetime(2023, 7, 15)
    result = add_days_to_date(input_date, 5)
    assert result == datetime(2023, 7, 20)

def test_add_negative_days():
    result = add_days_to_date("2023-07-15", -3)
    assert result == datetime(2023, 7, 12)

def test_add_zero_days():
    result = add_days_to_date("2023-07-15", 0)
    assert result == datetime(2023, 7, 15)

def test_add_large_number_of_days():
    result = add_days_to_date("2023-07-15", 365)
    assert result == datetime(2024, 7, 15)

def test_invalid_date_string():
    with pytest.raises(ValueError, match="Invalid date format"):
        add_days_to_date("15-07-2023", 5)

def test_invalid_input_type():
    with pytest.raises(ValueError, match="Input must be a datetime object or a date string"):
        add_days_to_date(12345, 5)

def test_invalid_days_type():
    with pytest.raises(ValueError, match="Number of days must be an integer"):
        add_days_to_date("2023-07-15", "5")