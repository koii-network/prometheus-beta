import pytest
from src.weekends import count_weekends_in_month

def test_count_weekends_in_month():
    # Test a month with 4 full weekends (January 2023)
    assert count_weekends_in_month(2023, 1) == 8
    
    # Test a month with 5 full weekends (May 2023)
    assert count_weekends_in_month(2023, 5) == 10
    
    # Test February with leap year
    assert count_weekends_in_month(2024, 2) == 8
    
    # Test February without leap year
    assert count_weekends_in_month(2023, 2) == 8

def test_invalid_month():
    # Test invalid month (out of range)
    with pytest.raises(ValueError, match="Month must be between 1 and 12"):
        count_weekends_in_month(2023, 0)
    
    with pytest.raises(ValueError, match="Month must be between 1 and 12"):
        count_weekends_in_month(2023, 13)

def test_invalid_year():
    # Test invalid year (negative)
    with pytest.raises(ValueError, match="Year must be a positive integer"):
        count_weekends_in_month(-1, 1)
    
    with pytest.raises(ValueError, match="Year must be a positive integer"):
        count_weekends_in_month(0, 1)