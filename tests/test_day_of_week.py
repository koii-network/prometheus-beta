import pytest
from src.day_of_week import get_day_of_week

def test_get_day_of_week_known_dates():
    """Test known dates and their corresponding day names."""
    test_cases = [
        ('2023-06-26', 'Monday'),
        ('2023-06-27', 'Tuesday'),
        ('2023-06-28', 'Wednesday'),
        ('2023-06-29', 'Thursday'),
        ('2023-06-30', 'Friday'),
        ('2023-07-01', 'Saturday'),
        ('2023-07-02', 'Sunday')
    ]
    
    for date, expected_day in test_cases:
        assert get_day_of_week(date) == expected_day

def test_get_day_of_week_invalid_format():
    """Test that invalid date formats raise a ValueError."""
    invalid_dates = [
        '26-06-2023',  # Wrong order
        '2023/06/26',  # Wrong separator
        'invalid-date',
        ''
    ]
    
    for invalid_date in invalid_dates:
        with pytest.raises(ValueError, match="Invalid date format"):
            get_day_of_week(invalid_date)

def test_get_day_of_week_leap_year():
    """Test a date in a leap year."""
    assert get_day_of_week('2024-02-29') == 'Thursday'