import pytest
from src.weekend_counter import count_weekends_in_month

def test_weekends_in_january_2023():
    # January 2023 has 9 weekend days
    assert count_weekends_in_month(2023, 1) == 9

def test_weekends_in_february_2024():
    # February 2024 (leap year) has 9 weekend days
    assert count_weekends_in_month(2024, 2) == 9

def test_weekends_in_december_2022():
    # December 2022 has 10 weekend days
    assert count_weekends_in_month(2022, 12) == 10

def test_invalid_month_low():
    with pytest.raises(ValueError, match="Month must be between 1 and 12"):
        count_weekends_in_month(2023, 0)

def test_invalid_month_high():
    with pytest.raises(ValueError, match="Month must be between 1 and 12"):
        count_weekends_in_month(2023, 13)

def test_invalid_year():
    with pytest.raises(ValueError, match="Year must be a positive integer"):
        count_weekends_in_month(0, 1)
    with pytest.raises(ValueError, match="Year must be a positive integer"):
        count_weekends_in_month(-1, 1)