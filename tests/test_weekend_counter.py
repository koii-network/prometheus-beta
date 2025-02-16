import pytest
from src.weekend_counter import count_weekends_in_month

def test_count_weekends_in_month():
    # Test a month with 4 full weekends
    assert count_weekends_in_month(2023, 7) == 8  # July 2023 has 8 weekend days
    
    # Test a month with a different number of weekends
    assert count_weekends_in_month(2023, 2) == 8  # February 2023 has 8 weekend days
    
    # Test a leap year February
    assert count_weekends_in_month(2024, 2) == 8  # February 2024 (leap year) has 8 weekend days

def test_invalid_month():
    # Test invalid month inputs
    with pytest.raises(ValueError, match="Month must be between 1 and 12"):
        count_weekends_in_month(2023, 0)
    
    with pytest.raises(ValueError, match="Month must be between 1 and 12"):
        count_weekends_in_month(2023, 13)

def test_edge_cases():
    # January with 5 weekends
    assert count_weekends_in_month(2023, 1) == 10  # January 2023 has 10 weekend days
    
    # December with potential 5 weekends
    assert count_weekends_in_month(2023, 12) == 10  # December 2023 has 10 weekend days