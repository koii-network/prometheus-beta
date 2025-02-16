import pytest
from src.date_utils import add_days_to_date

def test_add_positive_days():
    """Test adding positive number of days."""
    assert add_days_to_date('2023-01-01', 5) == '2023-01-06'

def test_add_negative_days():
    """Test subtracting days."""
    assert add_days_to_date('2023-01-15', -10) == '2023-01-05'

def test_add_zero_days():
    """Test adding zero days."""
    assert add_days_to_date('2023-12-31', 0) == '2023-12-31'

def test_cross_month_boundary():
    """Test adding days that cross month boundary."""
    assert add_days_to_date('2023-01-30', 3) == '2023-02-02'

def test_cross_year_boundary():
    """Test adding days that cross year boundary."""
    assert add_days_to_date('2023-12-30', 3) == '2024-01-02'

def test_invalid_date_format():
    """Test handling of invalid date format."""
    with pytest.raises(ValueError, match="Invalid date format"):
        add_days_to_date('2023/01/01', 5)

def test_invalid_date():
    """Test handling of invalid date."""
    with pytest.raises(ValueError):
        add_days_to_date('2023-02-30', 5)