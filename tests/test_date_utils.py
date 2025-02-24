import pytest
from datetime import datetime, timedelta
from src.date_utils import add_days_to_date

def test_add_days_to_date_string_input():
    """Test adding days to a date string input"""
    result = add_days_to_date('2023-05-15', 10)
    assert result == datetime(2023, 5, 25)

def test_add_days_to_date_datetime_input():
    """Test adding days to a datetime input"""
    input_date = datetime(2023, 5, 15)
    result = add_days_to_date(input_date, 10)
    assert result == datetime(2023, 5, 25)

def test_subtract_days():
    """Test subtracting days"""
    result = add_days_to_date('2023-05-15', -5)
    assert result == datetime(2023, 5, 10)

def test_zero_days():
    """Test adding zero days"""
    input_date = datetime(2023, 5, 15)
    result = add_days_to_date(input_date, 0)
    assert result == input_date

def test_cross_month_boundary():
    """Test adding days across month boundary"""
    result = add_days_to_date('2023-01-30', 5)
    assert result == datetime(2023, 2, 4)

def test_cross_year_boundary():
    """Test adding days across year boundary"""
    result = add_days_to_date('2023-12-28', 5)
    assert result == datetime(2024, 1, 2)

def test_invalid_date_format():
    """Test invalid date string format"""
    with pytest.raises(ValueError, match="Invalid date format"):
        add_days_to_date('15-05-2023', 10)

def test_invalid_days_type():
    """Test invalid days type"""
    with pytest.raises(TypeError, match="Days must be an integer"):
        add_days_to_date('2023-05-15', '10')

def test_invalid_date_type():
    """Test invalid date type"""
    with pytest.raises(TypeError, match="Date must be a string"):
        add_days_to_date(123456, 10)