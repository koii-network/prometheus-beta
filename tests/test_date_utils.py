import pytest
from datetime import datetime
from src.date_utils import add_days_to_date

def test_add_days_to_string_date():
    """Test adding days to a date provided as a string"""
    assert add_days_to_date('2023-05-15', 10) == '2023-05-25'

def test_add_days_to_datetime():
    """Test adding days to a datetime object"""
    date = datetime(2023, 5, 15)
    assert add_days_to_date(date, 10) == '2023-05-25'

def test_add_zero_days():
    """Test adding 0 days"""
    assert add_days_to_date('2023-05-15', 0) == '2023-05-15'

def test_add_negative_days():
    """Test adding negative days"""
    assert add_days_to_date('2023-05-15', -5) == '2023-05-10'

def test_cross_month_boundary():
    """Test adding days that cross a month boundary"""
    assert add_days_to_date('2023-01-30', 5) == '2023-02-04'

def test_cross_year_boundary():
    """Test adding days that cross a year boundary"""
    assert add_days_to_date('2022-12-30', 5) == '2023-01-04'

def test_invalid_date_format():
    """Test raising error for invalid date format"""
    with pytest.raises(ValueError, match="Invalid date format"):
        add_days_to_date('15-05-2023', 10)

def test_invalid_days_type():
    """Test raising error for non-integer days"""
    with pytest.raises(ValueError, match="days_to_add must be an integer"):
        add_days_to_date('2023-05-15', '10')