import pytest
from src.day_of_week import get_day_of_week

def test_valid_dates():
    # Test various known dates and their expected day names
    test_cases = [
        ('2023-06-22', 'Thursday'),   # A specific known date
        ('2024-02-14', 'Wednesday'),  # Valentine's Day
        ('2000-01-01', 'Saturday'),   # Millennium start
    ]
    
    for date, expected_day in test_cases:
        assert get_day_of_week(date) == expected_day, f"Failed for date {date}"

def test_invalid_date_format():
    # Test various invalid date formats
    invalid_dates = [
        '22-06-2023',        # Wrong order
        '2023/06/22',        # Wrong separator
        '2023-6-2',          # Single digit month/day
        '2023-13-32',        # Invalid month/day
        '',                  # Empty string
    ]
    
    for invalid_date in invalid_dates:
        with pytest.raises(ValueError, match="Invalid date format"):
            get_day_of_week(invalid_date)

def test_edge_cases():
    # Test edge cases like leap years
    edge_cases = [
        ('2020-02-29', 'Saturday'),   # Leap year date
        ('2023-12-31', 'Sunday'),     # Last day of the year
        ('2024-01-01', 'Monday')      # First day of the year
    ]
    
    for date, expected_day in edge_cases:
        assert get_day_of_week(date) == expected_day, f"Failed for edge case {date}"