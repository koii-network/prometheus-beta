import pytest
from datetime import datetime, timedelta
from src.date_utils import add_days_to_date

def test_add_positive_days():
    """Test adding positive number of days."""
    assert add_days_to_date('2023-01-01', 5) == '2023-01-06'

def test_add_negative_days():
    """Test subtracting days by using negative number."""
    assert add_days_to_date('2023-01-10', -3) == '2023-01-07'

def test_cross_month_boundary():
    """Test adding days that cross month boundary."""
    assert add_days_to_date('2023-01-31', 1) == '2023-02-01'

def test_cross_year_boundary():
    """Test adding days that cross year boundary."""
    assert add_days_to_date('2023-12-31', 1) == '2024-01-01'

def test_invalid_date_format():
    """Test handling of invalid date format."""
    with pytest.raises(ValueError, match="Invalid date format"):
        add_days_to_date('2023/01/01', 5)

def test_zero_days():
    """Test adding zero days returns the same date."""
    assert add_days_to_date('2023-06-15', 0) == '2023-06-15'