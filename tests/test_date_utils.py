import pytest
from src.date_utils import add_days_to_date

def test_add_positive_days():
    """Test adding positive number of days"""
    assert add_days_to_date('2023-01-01', 10) == '2023-01-11'

def test_add_negative_days():
    """Test subtracting days"""
    assert add_days_to_date('2023-01-15', -5) == '2023-01-10'

def test_add_zero_days():
    """Test adding zero days"""
    assert add_days_to_date('2023-06-30', 0) == '2023-06-30'

def test_cross_month_boundary():
    """Test adding days that cross month boundary"""
    assert add_days_to_date('2023-01-31', 1) == '2023-02-01'

def test_cross_year_boundary():
    """Test adding days that cross year boundary"""
    assert add_days_to_date('2023-12-31', 1) == '2024-01-01'

def test_invalid_date_format():
    """Test invalid date format raises ValueError"""
    with pytest.raises(ValueError, match="Invalid input"):
        add_days_to_date('2023/01/01', 10)

def test_invalid_date_string():
    """Test invalid date string raises ValueError"""
    with pytest.raises(ValueError, match="Invalid input"):
        add_days_to_date('not-a-date', 10)

def test_invalid_days_type():
    """Test invalid days type raises ValueError"""
    with pytest.raises(ValueError, match="Invalid input"):
        add_days_to_date('2023-01-01', '10')