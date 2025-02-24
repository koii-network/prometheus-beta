import pytest
from datetime import datetime
from src.day_name import get_day_name

def test_get_day_name_string_input():
    """Test getting day name from a valid date string."""
    assert get_day_name('2023-06-21') == 'Wednesday'
    assert get_day_name('2023-12-25') == 'Monday'

def test_get_day_name_datetime_input():
    """Test getting day name from a datetime object."""
    date = datetime(2023, 6, 21)
    assert get_day_name(date) == 'Wednesday'

def test_get_day_name_invalid_string():
    """Test that invalid date string raises ValueError."""
    with pytest.raises(ValueError, match="Invalid date format"):
        get_day_name('2023/06/21')
    with pytest.raises(ValueError, match="Invalid date format"):
        get_day_name('invalid-date')

def test_get_day_name_invalid_type():
    """Test that invalid input type raises TypeError."""
    with pytest.raises(TypeError, match="Expected str or datetime"):
        get_day_name(12345)
    with pytest.raises(TypeError, match="Expected str or datetime"):
        get_day_name(None)
    with pytest.raises(TypeError, match="Expected str or datetime"):
        get_day_name([])

def test_get_day_name_edge_cases():
    """Test various edge cases."""
    # First and last day of a leap year
    assert get_day_name('2024-02-29') == 'Thursday'
    
    # Different years and months
    assert get_day_name('2000-01-01') == 'Saturday'
    assert get_day_name('2100-12-31') == 'Friday'