import pytest
from datetime import datetime, timedelta
from src.date_calculator import calculate_days_between_dates

def test_calculate_days_between_dates_same_day():
    """Test dates on the same day return 0 days."""
    today = datetime.now().date()
    assert calculate_days_between_dates(today, today) == 0

def test_calculate_days_between_dates_string_inputs():
    """Test calculation with string date inputs."""
    assert calculate_days_between_dates('2023-01-01', '2023-01-10') == 9

def test_calculate_days_between_dates_datetime_inputs():
    """Test calculation with datetime inputs."""
    date1 = datetime(2023, 1, 1)
    date2 = datetime(2023, 1, 10)
    assert calculate_days_between_dates(date1, date2) == 9

def test_calculate_days_between_dates_reverse_order():
    """Test that order of dates doesn't matter."""
    date1 = '2023-01-01'
    date2 = '2023-01-10'
    assert calculate_days_between_dates(date1, date2) == calculate_days_between_dates(date2, date1)

def test_calculate_days_between_dates_invalid_date():
    """Test raising ValueError for invalid date formats."""
    with pytest.raises(ValueError):
        calculate_days_between_dates('invalid-date', '2023-01-10')

def test_calculate_days_between_dates_different_years():
    """Test calculation between dates in different years."""
    assert calculate_days_between_dates('2022-12-31', '2023-01-02') == 2

def test_calculate_days_between_dates_iso_format():
    """Test ISO format dates with timezone."""
    date1 = '2023-01-01T00:00:00Z'
    date2 = '2023-01-10T00:00:00Z'
    assert calculate_days_between_dates(date1, date2) == 9