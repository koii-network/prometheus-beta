import pytest
from datetime import datetime, timedelta
from src.date_utils import add_days_to_date

def test_add_days_to_date_string_input():
    """Test adding days to a date provided as a string."""
    result = add_days_to_date('2023-05-15', 10)
    assert result == datetime(2023, 5, 25)

def test_add_days_to_date_datetime_input():
    """Test adding days to a date provided as a datetime object."""
    input_date = datetime(2023, 05, 15)
    result = add_days_to_date(input_date, 10)
    assert result == datetime(2023, 5, 25)

def test_add_zero_days():
    """Test adding zero days leaves the date unchanged."""
    result = add_days_to_date('2023-05-15', 0)
    assert result == datetime(2023, 5, 15)

def test_add_negative_days():
    """Test adding negative days subtracts days from the date."""
    result = add_days_to_date('2023-05-15', -5)
    assert result == datetime(2023, 5, 10)

def test_invalid_days_input():
    """Test that a non-integer days input raises a ValueError."""
    with pytest.raises(ValueError, match="days_to_add must be an integer"):
        add_days_to_date('2023-05-15', '10')

def test_invalid_date_format():
    """Test that an invalid date format raises a ValueError."""
    with pytest.raises(ValueError, match="input_date must be in 'YYYY-MM-DD' format"):
        add_days_to_date('15-05-2023', 10)

def test_invalid_date_type():
    """Test that an invalid date type raises a ValueError."""
    with pytest.raises(ValueError, match="input_date must be a datetime object or a string in 'YYYY-MM-DD' format"):
        add_days_to_date(12345, 10)