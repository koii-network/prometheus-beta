import pytest
from src.date_difference import calculate_days_between_dates

def test_days_between_dates_same_date():
    assert calculate_days_between_dates('2023-01-01', '2023-01-01') == 0

def test_days_between_dates_different_years():
    assert calculate_days_between_dates('2022-01-01', '2023-01-01') == 365

def test_days_between_dates_leap_year():
    assert calculate_days_between_dates('2020-02-01', '2020-03-01') == 29

def test_days_between_dates_reverse_order():
    assert calculate_days_between_dates('2023-01-15', '2023-01-01') == 14

def test_invalid_date_format():
    with pytest.raises(ValueError, match="Invalid date format"):
        calculate_days_between_dates('2023/01/01', '2023-01-15')

def test_invalid_date():
    with pytest.raises(ValueError, match="Invalid date format"):
        calculate_days_between_dates('2023-13-01', '2023-01-15')