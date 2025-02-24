import pytest
from datetime import datetime, timedelta
from src.date_calculator import calculate_days_between_dates

def test_calculate_days_between_dates_basic():
    """Test calculating days between two dates"""
    assert calculate_days_between_dates('2023-01-01', '2023-01-10') == 9
    assert calculate_days_between_dates('2023-01-10', '2023-01-01') == 9

def test_calculate_days_between_dates_same_date():
    """Test when both dates are the same"""
    assert calculate_days_between_dates('2023-01-01', '2023-01-01') == 0

def test_calculate_days_between_dates_different_years():
    """Test calculating days between dates in different years"""
    assert calculate_days_between_dates('2022-12-31', '2023-01-01') == 1

def test_calculate_days_between_dates_leap_year():
    """Test calculating days between dates crossing a leap year"""
    assert calculate_days_between_dates('2020-02-28', '2020-03-01') == 2

def test_calculate_days_between_dates_invalid_format():
    """Test handling of invalid date formats"""
    with pytest.raises(ValueError, match=r"Invalid date format"):
        calculate_days_between_dates('2023/01/01', '2023-01-10')
    
    with pytest.raises(ValueError, match=r"Invalid date format"):
        calculate_days_between_dates('2023-1-1', '2023-01-10')

def test_calculate_days_between_dates_invalid_date():
    """Test handling of invalid dates"""
    with pytest.raises(ValueError, match=r"Invalid date format"):
        calculate_days_between_dates('2023-13-01', '2023-01-10')
    
    with pytest.raises(ValueError, match=r"Invalid date format"):
        calculate_days_between_dates('2023-02-30', '2023-01-10')