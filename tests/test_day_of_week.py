import pytest
from src.day_of_week import get_day_of_week

def test_get_day_of_week_known_dates():
    # Test a few known dates
    assert get_day_of_week('2023-06-25') == 'Sunday'
    assert get_day_of_week('2023-06-26') == 'Monday'
    assert get_day_of_week('2023-06-27') == 'Tuesday'
    assert get_day_of_week('2023-06-28') == 'Wednesday'
    assert get_day_of_week('2023-06-29') == 'Thursday'
    assert get_day_of_week('2023-06-30') == 'Friday'
    assert get_day_of_week('2023-07-01') == 'Saturday'

def test_get_day_of_week_invalid_format():
    # Test invalid date formats
    with pytest.raises(ValueError, match="Invalid date format"):
        get_day_of_week('25-06-2023')  # Wrong order
    
    with pytest.raises(ValueError, match="Invalid date format"):
        get_day_of_week('2023/06/25')  # Wrong separator
    
    with pytest.raises(ValueError, match="Invalid date format"):
        get_day_of_week('2023-6-5')  # Missing leading zeros

def test_get_day_of_week_edge_cases():
    # Test leap year and other edge cases
    assert get_day_of_week('2020-02-29') == 'Saturday'  # Leap year date
    
    with pytest.raises(ValueError):
        get_day_of_week('')  # Empty string
    
    with pytest.raises(ValueError):
        get_day_of_week(None)  # None input