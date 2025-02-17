import pytest
from src.weekend_counter import count_weekends_in_month

def test_count_weekends_standard_month():
    # Test a month with full 4 weekends (July 2023)
    assert count_weekends_in_month(2023, 7) == 10

def test_count_weekends_february():
    # Test a month with fewer days (February 2023)
    assert count_weekends_in_month(2023, 2) == 8

def test_count_weekends_leap_year():
    # Test a leap year February 
    assert count_weekends_in_month(2024, 2) == 8

def test_invalid_month_low():
    # Test handling of invalid low month
    with pytest.raises(ValueError, match="Month must be between 1 and 12"):
        count_weekends_in_month(2023, 0)

def test_invalid_month_high():
    # Test handling of invalid high month
    with pytest.raises(ValueError, match="Month must be between 1 and 12"):
        count_weekends_in_month(2023, 13)

def test_invalid_year():
    # Test handling of invalid year
    with pytest.raises(ValueError, match="Year must be a positive integer"):
        count_weekends_in_month(0, 5)

def test_various_years_months():
    # Additional test cases for different years and months
    test_cases = [
        (2023, 1, 9),   # January
        (2023, 12, 10), # December
        (2024, 3, 10),   # March in a leap year
    ]
    
    for year, month, expected_weekends in test_cases:
        assert count_weekends_in_month(year, month) == expected_weekends