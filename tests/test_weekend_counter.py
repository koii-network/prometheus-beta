import pytest
from src.weekend_counter import count_weekends_in_month

def test_count_weekends_typical_month():
    # January 2023 has 9 weekend days
    assert count_weekends_in_month(2023, 1) == 9

def test_count_weekends_february_leap_year():
    # February 2024 (leap year) 
    assert count_weekends_in_month(2024, 2) == 8

def test_count_weekends_longer_month():
    # July 2023 has 10 weekend days
    assert count_weekends_in_month(2023, 7) == 10

def test_invalid_month_low():
    with pytest.raises(ValueError, match="Month must be between 1 and 12"):
        count_weekends_in_month(2023, 0)

def test_invalid_month_high():
    with pytest.raises(ValueError, match="Month must be between 1 and 12"):
        count_weekends_in_month(2023, 13)

def test_invalid_year():
    with pytest.raises(ValueError, match="Year must be a positive integer"):
        count_weekends_in_month(0, 5)

def test_different_years():
    # Different years can have different weekend counts for the same month
    assert count_weekends_in_month(2020, 12) == 8  # 2020 (leap year)
    assert count_weekends_in_month(2021, 12) == 9  # 2021 (non-leap year)