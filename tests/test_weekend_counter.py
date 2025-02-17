import pytest
from src.weekend_counter import count_weekends_in_month

def test_count_weekends_in_month():
    # Test a typical month with weekends
    assert count_weekends_in_month(2023, 6) == 10  # June 2023 has 10 weekend days
    assert count_weekends_in_month(2023, 12) == 10  # December 2023 has 10 weekend days
    
    # Test February in a leap year
    assert count_weekends_in_month(2024, 2) == 8  # February 2024 (leap year) has 8 weekend days
    
    # Test full 31-day month
    assert count_weekends_in_month(2023, 7) == 10  # July 2023 has 10 weekend days
    
    # Test full 30-day month
    assert count_weekends_in_month(2023, 9) == 10  # September 2023 has 10 weekend days

def test_invalid_month():
    # Test invalid month
    with pytest.raises(ValueError, match="Month must be between 1 and 12"):
        count_weekends_in_month(2023, 0)
    
    with pytest.raises(ValueError, match="Month must be between 1 and 12"):
        count_weekends_in_month(2023, 13)

def test_invalid_year():
    # Test invalid year
    with pytest.raises(ValueError, match="Year must be a positive integer"):
        count_weekends_in_month(0, 6)
    
    with pytest.raises(ValueError, match="Year must be a positive integer"):
        count_weekends_in_month(-1, 6)