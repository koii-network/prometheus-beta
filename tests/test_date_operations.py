import pytest
from datetime import datetime, timedelta
from src.date_operations import add_days_to_date

def test_add_days_positive_string_input():
    result = add_days_to_date('2023-01-01', 5)
    assert result == datetime(2023, 1, 6)

def test_add_days_negative_string_input():
    result = add_days_to_date('2023-01-15', -10)
    assert result == datetime(2023, 1, 5)

def test_add_days_datetime_input():
    date = datetime(2023, 6, 15)
    result = add_days_to_date(date, 7)
    assert result == datetime(2023, 6, 22)

def test_zero_days():
    result = add_days_to_date('2023-03-03', 0)
    assert result == datetime(2023, 3, 3)

def test_invalid_date_format():
    with pytest.raises(ValueError, match="Invalid date format"):
        add_days_to_date('2023/01/01', 5)

def test_invalid_input_type():
    with pytest.raises(TypeError, match="Date must be a string"):
        add_days_to_date(12345, 5)

def test_invalid_days_type():
    with pytest.raises(TypeError, match="Days must be an integer"):
        add_days_to_date('2023-01-01', '5')

def test_leap_year():
    result = add_days_to_date('2020-02-28', 1)
    assert result == datetime(2020, 2, 29)

def test_large_number_of_days():
    result = add_days_to_date('2023-01-01', 365)
    assert result == datetime(2024, 1, 1)