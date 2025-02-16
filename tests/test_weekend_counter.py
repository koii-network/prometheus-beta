import pytest
from src.weekend_counter import count_weekends_in_month

def test_count_weekends_standard_month():
    """Test a typical month with full weeks."""
    assert count_weekends_in_month(2023, 7) == 10  # July 2023 has 10 weekend days

def test_count_weekends_leap_year():
    """Test February in a leap year."""
    assert count_weekends_in_month(2024, 2) == 9  # February 2024 has 9 weekend days

def test_count_weekends_different_years():
    """Test weekend count for different years and months."""
    test_cases = [
        (2023, 1, 10),    # January 2023
        (2023, 12, 10),   # December 2023
        (2022, 5, 10),    # May 2022
    ]
    
    for year, month, expected in test_cases:
        assert count_weekends_in_month(year, month) == expected

def test_invalid_month_low():
    """Test that an invalid low month raises a ValueError."""
    with pytest.raises(ValueError, match="Month must be between 1 and 12"):
        count_weekends_in_month(2023, 0)

def test_invalid_month_high():
    """Test that an invalid high month raises a ValueError."""
    with pytest.raises(ValueError, match="Month must be between 1 and 12"):
        count_weekends_in_month(2023, 13)

def test_invalid_year():
    """Test that an invalid year raises a ValueError."""
    with pytest.raises(ValueError, match="Year must be a positive integer"):
        count_weekends_in_month(0, 5)