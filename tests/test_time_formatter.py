import pytest
from datetime import datetime
import re
from src.time_formatter import get_current_time_formatted

def test_time_format():
    """
    Test that the function returns a correctly formatted time string.
    """
    # Get the current time
    current_time = get_current_time_formatted()
    
    # Check that the string matches HH:MM:SS format
    assert re.match(r'^\d{2}:\d{2}:\d{2}$', current_time), \
        f"Time format is incorrect. Got: {current_time}"

def test_time_format_components():
    """
    Verify that each component of the time is within valid ranges.
    """
    current_time = get_current_time_formatted()
    hours, minutes, seconds = map(int, current_time.split(':'))
    
    # Check ranges
    assert 0 <= hours <= 23, f"Invalid hours: {hours}"
    assert 0 <= minutes <= 59, f"Invalid minutes: {minutes}"
    assert 0 <= seconds <= 59, f"Invalid seconds: {seconds}"

def test_time_matches_datetime():
    """
    Ensure the function returns time consistent with datetime.now().
    """
    # Get time from function and from datetime
    func_time = get_current_time_formatted()
    datetime_time = datetime.now().strftime('%H:%M:%S')
    
    # Allow for a small time difference (less than a second)
    assert func_time == datetime_time, \
        f"Function time {func_time} does not match datetime {datetime_time}"