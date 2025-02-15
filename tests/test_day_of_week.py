import pytest
from src.day_of_week import get_day_of_week

def test_get_day_of_week_valid_dates():
    # Test known dates and their expected days
    test_cases = [
        ('2023-06-19', 'Monday'),    # A specific Monday
        ('2023-06-20', 'Tuesday'),   # A specific Tuesday
        ('2023-06-21', 'Wednesday'), # A specific Wednesday
        ('2023-06-22', 'Thursday'),  # A specific Thursday
        ('2023-06-23', 'Friday'),    # A specific Friday
        ('2023-06-24', 'Saturday'),  # A specific Saturday
        ('2023-06-25', 'Sunday')     # A specific Sunday
    ]
    
    for date, expected_day in test_cases:
        assert get_day_of_week(date) == expected_day

def test_get_day_of_week_invalid_format():
    # Test invalid date formats
    invalid_formats = [
        '19-06-2023',        # Wrong order
        '2023/06/19',        # Wrong separator
        '2023-6-19',         # Single digit month
        '2023-06-9',         # Single digit day
        'not a date'         # Completely invalid input
    ]
    
    for invalid_date in invalid_formats:
        with pytest.raises(ValueError, match="Invalid date format"):
            get_day_of_week(invalid_date)

def test_get_day_of_week_edge_cases():
    # Test some edge case dates
    test_cases = [
        ('2000-02-29', 'Thursday'),  # Leap year date
        ('2100-02-28', 'Sunday')     # Non-leap century year
    ]
    
    for date, expected_day in test_cases:
        assert get_day_of_week(date) == expected_day