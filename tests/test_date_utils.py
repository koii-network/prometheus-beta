import pytest
from datetime import datetime, timedelta
from src.date_utils import calculate_days_between_dates

def test_calculate_days_between_dates_same_date():
    """Test when both dates are the same"""
    assert calculate_days_between_dates('2023-01-01', '2023-01-01') == 0

def test_calculate_days_between_dates_datetime_objects():
    """Test with datetime objects"""
    date1 = datetime(2023, 1, 1)
    date2 = datetime(2023, 1, 10)
    assert calculate_days_between_dates(date1, date2) == 9

def test_calculate_days_between_dates_string_dates():
    """Test with date strings"""
    assert calculate_days_between_dates('2023-01-01', '2023-01-10') == 9

def test_calculate_days_between_dates_reverse_order():
    """Test that order of dates doesn't matter"""
    assert calculate_days_between_dates('2023-01-10', '2023-01-01') == 9

def test_calculate_days_between_dates_different_formats():
    """Test different input date formats"""
    assert calculate_days_between_dates('2023-01-01', datetime(2023, 1, 10)) == 9

def test_invalid_date_string():
    """Test handling of invalid date strings"""
    with pytest.raises(ValueError):
        calculate_days_between_dates('invalid-date', '2023-01-01')

def test_invalid_input_type():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        calculate_days_between_dates(123, '2023-01-01')

def test_large_date_difference():
    """Test a large difference between dates"""
    assert calculate_days_between_dates('2020-01-01', '2023-01-01') == 1096  # 3 years