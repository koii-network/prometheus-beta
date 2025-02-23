import pytest
from src.weekend_counter import count_weekends_in_month

def test_regular_month():
    """Test a typical month with a standard number of weekends."""
    # January 2023 has 9 weekend days
    assert count_weekends_in_month(2023, 1) == 9

def test_leap_year_february():
    """Test February in a leap year."""
    # February 2024 has 9 weekend days
    assert count_weekends_in_month(2024, 2) == 9

def test_non_leap_year_february():
    """Test February in a non-leap year."""
    # February 2023 has 8 weekend days
    assert count_weekends_in_month(2023, 2) == 8

def test_month_with_31_days():
    """Test a month with 31 days."""
    # July 2023 has 10 weekend days
    assert count_weekends_in_month(2023, 7) == 10

def test_month_with_30_days():
    """Test a month with 30 days."""
    # April 2023 has 8 weekend days
    assert count_weekends_in_month(2023, 4) == 8

def test_invalid_month_low():
    """Test error handling for month below 1."""
    with pytest.raises(ValueError, match="Month must be between 1 and 12"):
        count_weekends_in_month(2023, 0)

def test_invalid_month_high():
    """Test error handling for month above 12."""
    with pytest.raises(ValueError, match="Month must be between 1 and 12"):
        count_weekends_in_month(2023, 13)

def test_different_years():
    """Test weekend counting for different years."""
    # Verify weekend count for different years
    assert count_weekends_in_month(2022, 12) == 10  # December 2022
    assert count_weekends_in_month(2023, 12) == 9   # December 2023