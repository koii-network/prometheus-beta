import pytest
from src.get_day_of_week import get_day_of_week

def test_get_day_of_week_valid_dates():
    """Test getting day names for various dates"""
    assert get_day_of_week('2023-07-04') == 'Tuesday'
    assert get_day_of_week('2024-02-29') == 'Thursday'
    assert get_day_of_week('2000-01-01') == 'Saturday'

def test_get_day_of_week_invalid_format():
    """Test that incorrect date formats raise ValueError"""
    with pytest.raises(ValueError, match="Invalid date format. Please use 'YYYY-MM-DD'."):
        get_day_of_week('04-07-2023')
    
    with pytest.raises(ValueError, match="Invalid date format. Please use 'YYYY-MM-DD'."):
        get_day_of_week('2023/07/04')
    
    with pytest.raises(ValueError, match="Invalid date format. Please use 'YYYY-MM-DD'."):
        get_day_of_week('Invalid Date')

def test_get_day_of_week_invalid_date():
    """Test that invalid dates raise ValueError"""
    with pytest.raises(ValueError):
        get_day_of_week('2023-13-32')