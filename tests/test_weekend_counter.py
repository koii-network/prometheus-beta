import pytest
from src.weekend_counter import count_weekends_in_month

def test_normal_month():
    # Test a typical month (e.g., May 2023)
    assert count_weekends_in_month(2023, 5) == 10

def test_month_with_4_full_weekends():
    # December 2023 has exactly 4 full weekends
    assert count_weekends_in_month(2023, 12) == 8

def test_leap_year_february():
    # Test a leap year February
    assert count_weekends_in_month(2020, 2) == 8

def test_invalid_month_low():
    # Test invalid month (too low)
    with pytest.raises(ValueError):
        count_weekends_in_month(2023, 0)

def test_invalid_month_high():
    # Test invalid month (too high)
    with pytest.raises(ValueError):
        count_weekends_in_month(2023, 13)

def test_different_years():
    # Test different years have different weekend counts
    assert count_weekends_in_month(2023, 1) == 8
    assert count_weekends_in_month(2024, 1) == 9  # Different due to leap year