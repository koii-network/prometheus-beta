import pytest
from src.weekend_counter import count_weekends_in_month

def test_count_weekends_in_month():
    # Test a typical month with multiple weekends
    assert count_weekends_in_month(2023, 7) == 10  # July 2023 has 10 weekend days
    
    # Test a month in a leap year
    assert count_weekends_in_month(2024, 2) == 9  # February 2024 has 9 weekend days
    
    # Test the last month of the year
    assert count_weekends_in_month(2023, 12) == 10  # December 2023 has 10 weekend days
    
    # Test the first month of the year
    assert count_weekends_in_month(2023, 1) == 9  # January 2023 has 9 weekend days

def test_invalid_month():
    # Test for invalid month inputs
    with pytest.raises(ValueError):
        count_weekends_in_month(2023, 0)
    
    with pytest.raises(ValueError):
        count_weekends_in_month(2023, 13)

def test_various_years():
    # Test different years to ensure consistency
    assert count_weekends_in_month(2020, 5) == 10  # May 2020 has 10 weekend days
    assert count_weekends_in_month(2022, 8) == 10  # August 2022 has 10 weekend days
    assert count_weekends_in_month(2025, 3) == 9   # March 2025 has 9 weekend days