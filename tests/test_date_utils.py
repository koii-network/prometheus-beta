import pytest
from datetime import datetime, date
from src.date_utils import calculate_days_between_dates

def test_calculate_days_between_dates_string_input():
    # Test string input dates
    assert calculate_days_between_dates('2023-01-01', '2023-01-10') == 9
    assert calculate_days_between_dates('2023-01-10', '2023-01-01') == 9

def test_calculate_days_between_dates_datetime_input():
    # Test datetime input
    date1 = datetime(2023, 1, 1).date()
    date2 = datetime(2023, 1, 10).date()
    assert calculate_days_between_dates(date1, date2) == 9

def test_calculate_days_between_dates_same_date():
    # Test same date returns 0
    assert calculate_days_between_dates('2023-01-01', '2023-01-01') == 0

def test_calculate_days_between_dates_different_years():
    # Test dates across different years
    assert calculate_days_between_dates('2022-12-31', '2023-01-01') == 1

def test_calculate_days_between_dates_invalid_format():
    # Test invalid date format raises ValueError
    with pytest.raises(ValueError, match="must be in 'YYYY-MM-DD' format"):
        calculate_days_between_dates('01-01-2023', '2023-01-10')
    
    with pytest.raises(ValueError, match="must be in 'YYYY-MM-DD' format"):
        calculate_days_between_dates('2023-01-10', 'invalid-date')