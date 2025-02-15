import pytest
from src.date_diff_calculator import calculate_days_between_dates

def test_calculate_days_between_dates_same_date():
    assert calculate_days_between_dates('2023-01-01', '2023-01-01') == 0

def test_calculate_days_between_dates_different_months():
    assert calculate_days_between_dates('2023-01-01', '2023-02-15') == 45

def test_calculate_days_between_dates_different_years():
    assert calculate_days_between_dates('2022-12-31', '2023-01-01') == 1

def test_calculate_days_between_dates_leap_year():
    assert calculate_days_between_dates('2020-02-28', '2020-03-01') == 2

def test_calculate_days_between_dates_reversed_order():
    assert calculate_days_between_dates('2023-03-15', '2023-01-01') == 73

def test_calculate_days_between_dates_invalid_format():
    with pytest.raises(ValueError, match="Invalid date format"):
        calculate_days_between_dates('2023/01/01', '2023-02-15')

def test_calculate_days_between_dates_invalid_date():
    with pytest.raises(ValueError):
        calculate_days_between_dates('2023-13-01', '2023-02-15')