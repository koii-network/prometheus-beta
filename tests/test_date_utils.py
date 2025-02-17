import pytest
from datetime import datetime
from src.date_utils import add_days_to_date

def test_add_days_to_date_string_input():
    """Test adding days to a date provided as a string"""
    assert add_days_to_date('2023-01-01', 5) == '2023-01-06'

def test_add_days_to_date_datetime_input():
    """Test adding days to a date provided as a datetime object"""
    date = datetime(2023, 1, 1)
    assert add_days_to_date(date, 5) == '2023-01-06'

def test_add_zero_days():
    """Test adding zero days returns the same date"""
    assert add_days_to_date('2023-01-01', 0) == '2023-01-01'

def test_subtract_days():
    """Test subtracting days from a date"""
    assert add_days_to_date('2023-01-10', -5) == '2023-01-05'

def test_cross_month_boundary():
    """Test adding days that cross a month boundary"""
    assert add_days_to_date('2023-01-30', 5) == '2023-02-04'

def test_cross_year_boundary():
    """Test adding days that cross a year boundary"""
    assert add_days_to_date('2022-12-30', 5) == '2023-01-04'

def test_invalid_date_format():
    """Test that an invalid date format raises a ValueError"""
    with pytest.raises(ValueError, match="Invalid date format"):
        add_days_to_date('2023/01/01', 5)

def test_invalid_days_type():
    """Test that non-integer days raises a TypeError"""
    with pytest.raises(TypeError, match="Days must be an integer"):
        add_days_to_date('2023-01-01', '5')
        add_days_to_date('2023-01-01', 5.5)