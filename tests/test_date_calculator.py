import pytest
from src.date_calculator import calculate_days_between_dates

def test_calculate_days_between_dates_same_date():
    assert calculate_days_between_dates('2023-01-01', '2023-01-01') == 0

def test_calculate_days_between_dates_different_dates():
    assert calculate_days_between_dates('2023-01-01', '2023-01-10') == 9
    assert calculate_days_between_dates('2023-01-10', '2023-01-01') == 9

def test_calculate_days_between_dates_different_years():
    assert calculate_days_between_dates('2022-12-31', '2023-01-01') == 1

def test_calculate_days_between_dates_invalid_format():
    with pytest.raises(ValueError, match="Dates must be in 'YYYY-MM-DD' format"):
        calculate_days_between_dates('01-01-2023', '2023-01-01')
    
    with pytest.raises(ValueError, match="Dates must be in 'YYYY-MM-DD' format"):
        calculate_days_between_dates('2023/01/01', '2023-01-01')