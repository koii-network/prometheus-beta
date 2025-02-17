import pytest
from datetime import datetime, timedelta
from src.date_utils import add_days_to_date

def test_add_days_to_date_string_input():
    # Test adding days to a date string
    result = add_days_to_date('2023-01-01', 5)
    assert result == datetime(2023, 1, 6)

def test_add_days_to_date_datetime_input():
    # Test adding days to a datetime object
    input_date = datetime(2023, 1, 1)
    result = add_days_to_date(input_date, 5)
    assert result == datetime(2023, 1, 6)

def test_add_negative_days():
    # Test subtracting days
    result = add_days_to_date('2023-01-10', -3)
    assert result == datetime(2023, 1, 7)

def test_add_zero_days():
    # Test adding zero days
    result = add_days_to_date('2023-01-01', 0)
    assert result == datetime(2023, 1, 1)

def test_invalid_date_format():
    # Test invalid date string format
    with pytest.raises(ValueError, match="Date must be in 'YYYY-MM-DD' format"):
        add_days_to_date('01-01-2023', 5)

def test_invalid_days_type():
    # Test invalid days type
    with pytest.raises(TypeError, match="Days must be an integer"):
        add_days_to_date('2023-01-01', '5')

def test_invalid_date_type():
    # Test invalid date type
    with pytest.raises(TypeError, match="Date must be a string in 'YYYY-MM-DD' format or a datetime object"):
        add_days_to_date(123, 5)