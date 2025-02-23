import pytest
from datetime import datetime, date
from src.date_difference import calculate_days_between_dates

def test_calculate_days_between_dates_strings():
    # Test with date strings
    assert calculate_days_between_dates('2023-01-01', '2023-01-10') == 9
    assert calculate_days_between_dates('2023-01-10', '2023-01-01') == 9

def test_calculate_days_between_dates_datetime():
    # Test with datetime/date objects
    date1 = datetime(2023, 1, 1)
    date2 = datetime(2023, 1, 10)
    assert calculate_days_between_dates(date1, date2) == 9

def test_calculate_days_between_dates_mixed_types():
    # Test with mixed input types
    date1 = '2023-01-01'
    date2 = datetime(2023, 1, 10)
    assert calculate_days_between_dates(date1, date2) == 9

def test_calculate_days_between_dates_same_date():
    # Test when dates are the same
    assert calculate_days_between_dates('2023-01-01', '2023-01-01') == 0

def test_calculate_days_between_dates_different_years():
    # Test dates across different years
    assert calculate_days_between_dates('2022-12-31', '2023-01-01') == 1

def test_invalid_date_format():
    # Test invalid date formats
    with pytest.raises(ValueError):
        calculate_days_between_dates('2023/01/01', '2023-01-10')
    
    with pytest.raises(ValueError):
        calculate_days_between_dates('2023-01-01', '2023/01/10')