import pytest
from src.weekend_counter import count_weekends_in_month

def test_count_weekends_in_typical_month():
    # January 2023 has 5 weekend days
    assert count_weekends_in_month(2023, 1) == 10

def test_count_weekends_in_february():
    # February 2023 has 4 weekend days
    assert count_weekends_in_month(2023, 2) == 8

def test_count_weekends_in_leap_year_february():
    # February 2024 (leap year) has different number of days
    assert count_weekends_in_month(2024, 2) == 10

def test_invalid_month_low():
    with pytest.raises(ValueError, match="Month must be between 1 and 12"):
        count_weekends_in_month(2023, 0)

def test_invalid_month_high():
    with pytest.raises(ValueError, match="Month must be between 1 and 12"):
        count_weekends_in_month(2023, 13)

def test_invalid_year():
    with pytest.raises(ValueError, match="Year must be a positive integer"):
        count_weekends_in_month(0, 6)

def test_different_years():
    # Different years with same month can have different weekend counts
    assert count_weekends_in_month(2022, 12) != count_weekends_in_month(2023, 12)

def test_edge_cases():
    # Specific edge case years and months
    assert count_weekends_in_month(2020, 12) == 10  # December 2020
    assert count_weekends_in_month(2021, 1) == 10   # January 2021