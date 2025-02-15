import pytest
from src.day_of_week import get_day_of_week

def test_valid_dates():
    # Test a few known dates
    assert get_day_of_week('2023-06-14') == 'Wednesday'
    assert get_day_of_week('2023-12-25') == 'Monday'
    assert get_day_of_week('2024-02-29') == 'Thursday'

def test_invalid_date_format():
    # Test invalid date formats
    with pytest.raises(ValueError, match="Invalid date format. Please use YYYY-MM-DD format."):
        get_day_of_week('14-06-2023')  # Wrong order
        get_day_of_week('2023/06/14')  # Wrong separator
        get_day_of_week('2023-6-14')   # Single digit month
        get_day_of_week('invalid')     # Completely wrong format

def test_edge_cases():
    # Test edge case dates
    assert get_day_of_week('0001-01-01') == 'Monday'  # Very early date
    assert get_day_of_week('9999-12-31') == 'Friday'  # Far future date