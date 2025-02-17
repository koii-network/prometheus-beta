import pytest
from src.weekend_counter import count_weekends_in_month

def test_count_weekends_standard_months():
    # Test a few standard months
    assert count_weekends_in_month(2023, 1) == 9  # January 2023
    assert count_weekends_in_month(2023, 2) == 8  # February 2023
    assert count_weekends_in_month(2023, 12) == 10  # December 2023

def test_count_weekends_leap_year():
    # Test a leap year (February)
    assert count_weekends_in_month(2024, 2) == 9  # February 2024

def test_count_weekends_invalid_month():
    # Test invalid month inputs
    with pytest.raises(ValueError):
        count_weekends_in_month(2023, 0)
    with pytest.raises(ValueError):
        count_weekends_in_month(2023, 13)

def test_count_weekends_different_years():
    # Test different years with varying weekend distributions
    assert count_weekends_in_month(2020, 1) == 10  # January 2020
    assert count_weekends_in_month(2021, 1) == 9   # January 2021