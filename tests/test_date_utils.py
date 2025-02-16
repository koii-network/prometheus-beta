import pytest
from src.date_utils import add_days_to_date

def test_add_positive_days():
    assert add_days_to_date('2023-01-01', 5) == '2023-01-06'

def test_add_negative_days():
    assert add_days_to_date('2023-01-15', -10) == '2023-01-05'

def test_add_zero_days():
    assert add_days_to_date('2023-12-31', 0) == '2023-12-31'

def test_cross_year_positive():
    assert add_days_to_date('2022-12-28', 5) == '2023-01-02'

def test_cross_year_negative():
    assert add_days_to_date('2023-01-03', -5) == '2022-12-29'

def test_invalid_date_format():
    with pytest.raises(ValueError, match="Invalid date format"):
        add_days_to_date('2023/01/01', 5)

def test_invalid_date():
    with pytest.raises(ValueError):
        add_days_to_date('2023-02-30', 5)