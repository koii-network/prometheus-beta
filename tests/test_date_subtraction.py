import pytest
from datetime import datetime, timedelta
from src.date_subtraction import subtract_days_from_date

def test_subtract_days_from_date():
    # Test standard date subtraction
    original_date = datetime(2023, 5, 15)
    result = subtract_days_from_date(original_date, 10)
    assert result == datetime(2023, 5, 5)

def test_subtract_days_zero():
    # Test subtracting zero days
    original_date = datetime(2023, 5, 15)
    result = subtract_days_from_date(original_date, 0)
    assert result == original_date

def test_subtract_days_across_month_boundary():
    # Test subtraction across month boundary
    original_date = datetime(2023, 3, 15)
    result = subtract_days_from_date(original_date, 20)
    assert result == datetime(2023, 2, 23)

def test_invalid_input_types():
    # Test invalid input types
    with pytest.raises(TypeError, match="Input date must be a datetime object"):
        subtract_days_from_date("2023-05-15", 10)
    
    with pytest.raises(TypeError, match="Number of days must be an integer"):
        subtract_days_from_date(datetime(2023, 5, 15), "10")

def test_negative_days():
    # Test negative number of days
    with pytest.raises(ValueError, match="Number of days cannot be negative"):
        subtract_days_from_date(datetime(2023, 5, 15), -5)