import pytest
from datetime import date
from src.date_calculator import calculate_days_between_dates

def test_calculate_days_between_dates_string_input():
    assert calculate_days_between_dates('2023-01-01', '2023-01-10') == 9
    assert calculate_days_between_dates('2023-01-10', '2023-01-01') == 9

def test_calculate_days_between_dates_date_object():
    date1 = date(2023, 1, 1)
    date2 = date(2023, 1, 10)
    assert calculate_days_between_dates(date1, date2) == 9

def test_calculate_days_between_dates_across_years():
    assert calculate_days_between_dates('2022-12-31', '2023-01-02') == 2

def test_calculate_days_between_dates_same_date():
    assert calculate_days_between_dates('2023-01-01', '2023-01-01') == 0

def test_calculate_days_between_dates_invalid_format():
    with pytest.raises(ValueError, match="First date must be in 'YYYY-MM-DD' format"):
        calculate_days_between_dates('2023/01/01', '2023-01-10')
    
    with pytest.raises(ValueError, match="Second date must be in 'YYYY-MM-DD' format"):
        calculate_days_between_dates('2023-01-01', '2023/01/10')