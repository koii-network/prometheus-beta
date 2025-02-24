import pytest
import calendar
from datetime import date
from src.weekend_counter import count_weekends_in_month

def test_typical_month():
    """Test a typical month with full weekends"""
    # January 2023 has 5 full weekend days
    result = count_weekends_in_month(2023, 1)
    weekend_days = [day for day in range(1, 32) 
                    if date(2023, 1, day).weekday() >= 5]
    print(f"Weekend days in January 2023: {weekend_days}")
    print(f"Number of weekend days: {len(weekend_days)}")
    assert result == len(weekend_days)

def test_month_with_partial_weeks():
    """Test a month with partial weeks at the beginning or end"""
    # February 2023 has 4 weekend days
    assert count_weekends_in_month(2023, 2) == 8

def test_leap_year():
    """Ensure leap year works correctly"""
    # February 2024 has 4 weekend days
    assert count_weekends_in_month(2024, 2) == 8

def test_invalid_month_low():
    """Test handling of month below valid range"""
    with pytest.raises(ValueError, match="Month must be between 1 and 12"):
        count_weekends_in_month(2023, 0)

def test_invalid_month_high():
    """Test handling of month above valid range"""
    with pytest.raises(ValueError, match="Month must be between 1 and 12"):
        count_weekends_in_month(2023, 13)

def test_invalid_year():
    """Test handling of negative year"""
    with pytest.raises(ValueError, match="Year must be a positive integer"):
        count_weekends_in_month(-1, 1)

def test_known_months():
    """Test several known months to verify accuracy"""
    test_cases = [
        (2023, 1, 10),   # January 2023
        (2023, 2, 8),    # February 2023
        (2023, 3, 10),   # March 2023
        (2023, 12, 10)   # December 2023
    ]
    
    for year, month, expected_weekends in test_cases:
        result = count_weekends_in_month(year, month)
        weekend_days = [day for day in range(1, calendar.monthrange(year, month)[1] + 1) 
                        if date(year, month, day).weekday() >= 5]
        print(f"{year}-{month} weekend days: {weekend_days}")
        print(f"Number of weekend days: {len(weekend_days)}")
        assert result == len(weekend_days)