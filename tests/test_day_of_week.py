import pytest
from src.day_of_week import get_day_of_week

def test_day_of_week_valid_dates():
    """Test valid date inputs return correct day names."""
    assert get_day_of_week('2023-06-19') == 'Monday'
    assert get_day_of_week('2023-06-20') == 'Tuesday'
    assert get_day_of_week('2023-06-21') == 'Wednesday'
    assert get_day_of_week('2023-06-22') == 'Thursday'
    assert get_day_of_week('2023-06-23') == 'Friday'
    assert get_day_of_week('2023-06-24') == 'Saturday'
    assert get_day_of_week('2023-06-25') == 'Sunday'

def test_day_of_week_invalid_format():
    """Test that invalid date formats raise a ValueError."""
    with pytest.raises(ValueError, match="Invalid date format"):
        get_day_of_week('19-06-2023')  # Wrong format
    
    with pytest.raises(ValueError, match="Invalid date format"):
        get_day_of_week('2023/06/19')  # Wrong separator
    
    with pytest.raises(ValueError, match="Invalid date format"):
        get_day_of_week('2023-13-32')  # Invalid date

def test_day_of_week_leap_year():
    """Test a leap year date."""
    assert get_day_of_week('2024-02-29') == 'Thursday'