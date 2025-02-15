import pytest
from src.weekend_counter import count_weekends_in_month

def test_typical_month():
    # January 2023 has 9 weekend days
    assert count_weekends_in_month(2023, 1) == 9

def test_leap_year_month():
    # February 2024 (leap year) has 8 weekend days
    assert count_weekends_in_month(2024, 2) == 8

def test_different_month():
    # July 2023 has 10 weekend days
    assert count_weekends_in_month(2023, 7) == 10

def test_invalid_month_too_low():
    with pytest.raises(ValueError):
        count_weekends_in_month(2023, 0)

def test_invalid_month_too_high():
    with pytest.raises(ValueError):
        count_weekends_in_month(2023, 13)

def test_specific_known_dates():
    test_cases = [
        (2023, 1, 9),   # January 2023
        (2023, 2, 8),   # February 2023
        (2023, 12, 10), # December 2023
        (2024, 2, 8),   # February 2024 (leap year) - corrected value
    ]
    
    for year, month, expected_weekends in test_cases:
        assert count_weekends_in_month(year, month) == expected_weekends