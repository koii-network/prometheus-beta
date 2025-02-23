import pytest
from src.date_calculator import calculate_days_between_dates

def test_calculate_days_between_dates_same_date():
    """Test calculating days between the same date"""
    assert calculate_days_between_dates('2023-01-01', '2023-01-01') == 0

def test_calculate_days_between_dates_different_dates():
    """Test calculating days between different dates"""
    assert calculate_days_between_dates('2023-01-01', '2023-01-10') == 9

def test_calculate_days_between_dates_reverse_order():
    """Test that order of dates doesn't matter"""
    assert calculate_days_between_dates('2023-01-10', '2023-01-01') == 9

def test_calculate_days_between_dates_different_years():
    """Test calculating days between dates in different years"""
    assert calculate_days_between_dates('2022-12-31', '2023-01-01') == 1

def test_calculate_days_between_dates_invalid_format():
    """Test that invalid date format raises ValueError"""
    with pytest.raises(ValueError, match="Invalid date format"):
        calculate_days_between_dates('2023/01/01', '2023-01-10')

def test_calculate_days_between_dates_invalid_date():
    """Test that invalid dates raise ValueError"""
    with pytest.raises(ValueError):
        calculate_days_between_dates('2023-02-30', '2023-01-10')

def test_calculate_days_between_dates_month_boundary():
    """Test calculating days across month boundaries"""
    assert calculate_days_between_dates('2023-01-31', '2023-03-01') == 29