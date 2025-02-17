import pytest
from datetime import datetime, date
from src.date_utils import calculate_days_between

def test_calculate_days_between_same_date():
    assert calculate_days_between('2023-05-15', '2023-05-15') == 0
    assert calculate_days_between(datetime(2023, 5, 15), datetime(2023, 5, 15)) == 0

def test_calculate_days_between_different_dates():
    assert calculate_days_between('2023-01-01', '2023-01-10') == 9
    assert calculate_days_between('2023-12-31', '2024-01-02') == 2

def test_calculate_days_between_reverse_order():
    assert calculate_days_between('2024-01-02', '2023-12-31') == 2

def test_calculate_days_between_datetime_objects():
    date1 = datetime(2023, 1, 1)
    date2 = datetime(2023, 12, 31)
    assert calculate_days_between(date1, date2) == 364

def test_calculate_days_between_date_objects():
    date1 = date(2023, 1, 1)
    date2 = date(2023, 12, 31)
    assert calculate_days_between(date1, date2) == 364

def test_invalid_date_format():
    with pytest.raises(ValueError, match="First date must be in YYYY-MM-DD format"):
        calculate_days_between('01/01/2023', '2023-12-31')
    
    with pytest.raises(ValueError, match="Second date must be in YYYY-MM-DD format"):
        calculate_days_between('2023-01-01', '31/12/2023')