import pytest
from src.date_difference import calculate_days_between_dates

def test_calculate_days_between_dates_same_date():
    assert calculate_days_between_dates('2023-01-01', '2023-01-01') == 0

def test_calculate_days_between_dates_consecutive_days():
    assert calculate_days_between_dates('2023-01-01', '2023-01-02') == 1

def test_calculate_days_between_dates_different_years():
    assert calculate_days_between_dates('2022-12-31', '2023-01-01') == 1

def test_calculate_days_between_dates_many_days_apart():
    assert calculate_days_between_dates('2020-01-01', '2023-01-01') == 1096

def test_calculate_days_between_dates_order_independent():
    assert calculate_days_between_dates('2023-01-02', '2023-01-01') == 1

def test_invalid_date_format_raises_error():
    with pytest.raises(ValueError, match="Invalid date format. Use YYYY-MM-DD"):
        calculate_days_between_dates('2023/01/01', '2023-01-02')

def test_invalid_date_raises_error():
    with pytest.raises(ValueError):
        calculate_days_between_dates('2023-13-01', '2023-01-02')