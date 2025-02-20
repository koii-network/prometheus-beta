import pytest
from src.day_of_week import get_day_of_week

def test_get_day_of_week_valid_dates():
    """Test get_day_of_week with various valid dates"""
    assert get_day_of_week('2023-06-19') == 'Monday'
    assert get_day_of_week('2023-06-20') == 'Tuesday'
    assert get_day_of_week('2023-06-21') == 'Wednesday'
    assert get_day_of_week('2023-06-22') == 'Thursday'
    assert get_day_of_week('2023-06-23') == 'Friday'
    assert get_day_of_week('2023-06-24') == 'Saturday'
    assert get_day_of_week('2023-06-25') == 'Sunday'

def test_get_day_of_week_invalid_format():
    """Test get_day_of_week with invalid date formats"""
    with pytest.raises(ValueError, match="Invalid date format. Please use YYYY-MM-DD format."):
        get_day_of_week('19-06-2023')  # Wrong order
    
    with pytest.raises(ValueError, match="Invalid date format. Please use YYYY-MM-DD format."):
        get_day_of_week('2023/06/19')  # Wrong separator
    
    with pytest.raises(ValueError, match="Invalid date format. Please use YYYY-MM-DD format."):
        get_day_of_week('Invalid Date')

def test_get_day_of_week_nonexistent_date():
    """Test get_day_of_week with nonexistent dates"""
    with pytest.raises(ValueError):
        get_day_of_week('2023-02-30')  # Nonexistent date