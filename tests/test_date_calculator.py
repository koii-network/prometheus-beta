import pytest
from src.date_calculator import calculate_days_between_dates

def test_calculate_days_between_dates_normal_case():
    assert calculate_days_between_dates('2023-01-01', '2023-01-10') == 9

def test_calculate_days_between_dates_same_date():
    assert calculate_days_between_dates('2023-01-01', '2023-01-01') == 0

def test_calculate_days_between_dates_different_years():
    assert calculate_days_between_dates('2022-01-01', '2023-01-01') == 365

def test_calculate_days_between_dates_past_and_future():
    assert calculate_days_between_dates('2020-01-01', '2021-01-01') == 365

def test_calculate_days_between_dates_invalid_format():
    with pytest.raises(ValueError, match="Dates must be in 'YYYY-MM-DD' format"):
        calculate_days_between_dates('2023/01/01', '2023-01-10')

def test_calculate_days_between_dates_invalid_date():
    with pytest.raises(ValueError):
        calculate_days_between_dates('2023-02-30', '2023-01-10')