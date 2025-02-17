import pytest
from src.day_of_week import get_day_of_week

def test_valid_dates():
    # Test various known dates
    assert get_day_of_week('2023-06-25') == 'Sunday'
    assert get_day_of_week('2023-06-26') == 'Monday'
    assert get_day_of_week('2023-06-27') == 'Tuesday'
    assert get_day_of_week('2023-06-28') == 'Wednesday'
    assert get_day_of_week('2023-06-29') == 'Thursday'
    assert get_day_of_week('2023-06-30') == 'Friday'
    assert get_day_of_week('2023-07-01') == 'Saturday'

def test_invalid_date_format():
    # Test various invalid date formats
    with pytest.raises(ValueError, match="Invalid date format"):
        get_day_of_week('25-06-2023')  # Wrong order
        get_day_of_week('2023/06/25')  # Wrong separator
        get_day_of_week('2023-6-25')   # Single digit month
        get_day_of_week('abc')         # Invalid input

def test_edge_cases():
    # Test some edge case dates
    assert get_day_of_week('2000-02-29') == 'Tuesday'   # Leap year
    assert get_day_of_week('2100-01-01') == 'Friday'   # Non-leap century year
    assert get_day_of_week('1970-01-01') == 'Thursday' # Unix epoch