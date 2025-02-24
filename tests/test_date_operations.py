import pytest
from datetime import datetime, timedelta
from src.date_operations import subtract_days

def test_subtract_days_basic():
    """Test basic date subtraction"""
    original_date = datetime(2023, 5, 15)
    result = subtract_days(original_date, 5)
    assert result == datetime(2023, 5, 10)

def test_subtract_days_across_month():
    """Test subtraction crossing month boundary"""
    original_date = datetime(2023, 3, 10)
    result = subtract_days(original_date, 15)
    assert result == datetime(2023, 2, 23)

def test_subtract_days_across_year():
    """Test subtraction crossing year boundary"""
    original_date = datetime(2023, 1, 15)
    result = subtract_days(original_date, 20)
    assert result == datetime(2022, 12, 26)

def test_subtract_zero_days():
    """Test subtracting zero days returns same date"""
    original_date = datetime(2023, 5, 15)
    result = subtract_days(original_date, 0)
    assert result == original_date

def test_negative_days_raises_error():
    """Test that negative days raise a ValueError"""
    original_date = datetime(2023, 5, 15)
    with pytest.raises(ValueError, match="Number of days to subtract must be non-negative"):
        subtract_days(original_date, -5)

def test_large_day_subtraction():
    """Test subtracting a large number of days"""
    original_date = datetime(2023, 5, 15)
    result = subtract_days(original_date, 1000)
    assert result == datetime(2020, 8, 18)  # Corrected to match actual computation