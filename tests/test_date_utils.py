import pytest
from datetime import datetime, timedelta
from src.date_utils import calculate_days_between_dates

def test_calculate_days_between_dates_basic():
    """Test calculating days between two different dates"""
    assert calculate_days_between_dates('2023-01-01', '2023-01-10') == 9

def test_calculate_days_between_dates_same_date():
    """Test calculating days between the same date"""
    assert calculate_days_between_dates('2023-01-01', '2023-01-01') == 0

def test_calculate_days_between_dates_reverse_order():
    """Test that order of dates doesn't matter"""
    assert calculate_days_between_dates('2023-01-10', '2023-01-01') == 9

def test_calculate_days_between_dates_different_years():
    """Test calculating days between dates in different years"""
    assert calculate_days_between_dates('2022-12-31', '2023-01-01') == 1

def test_invalid_date_format():
    """Test that incorrect date format raises a ValueError"""
    with pytest.raises(ValueError, match="Dates must be in 'YYYY-MM-DD' format"):
        calculate_days_between_dates('2023/01/01', '2023-01-10')

def test_invalid_date():
    """Test that invalid dates raise a ValueError"""
    with pytest.raises(ValueError):
        calculate_days_between_dates('2023-02-30', '2023-01-10')