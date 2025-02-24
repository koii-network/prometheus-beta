import re
from datetime import datetime
import pytest
from src.time_formatter import get_current_time_formatted

def test_get_current_time_formatted():
    """
    Test that the time formatting function returns a valid time string.
    """
    # Get the formatted time
    formatted_time = get_current_time_formatted()
    
    # Check that the string matches HH:MM:SS format
    assert re.match(r'^\d{2}:\d{2}:\d{2}$', formatted_time), \
        f"Formatted time {formatted_time} does not match HH:MM:SS format"
    
    # Validate hours (00-23)
    hours = int(formatted_time.split(':')[0])
    assert 0 <= hours <= 23, f"Hours {hours} must be between 0 and 23"
    
    # Validate minutes and seconds (00-59)
    minutes = int(formatted_time.split(':')[1])
    seconds = int(formatted_time.split(':')[2])
    assert 0 <= minutes <= 59, f"Minutes {minutes} must be between 0 and 59"
    assert 0 <= seconds <= 59, f"Seconds {seconds} must be between 0 and 59"

def test_time_consistency():
    """
    Verify that the function returns time consistent with datetime.now().
    """
    # Get current time from datetime and from our function
    datetime_now = datetime.now()
    formatted_time = get_current_time_formatted()
    
    # Extract components from datetime
    datetime_hours = datetime_now.strftime('%H')
    datetime_minutes = datetime_now.strftime('%M')
    datetime_seconds = datetime_now.strftime('%S')
    
    # Compare each component
    assert formatted_time.split(':')[0] == datetime_hours, "Hours do not match"
    assert formatted_time.split(':')[1] == datetime_minutes, "Minutes do not match"
    assert formatted_time.split(':')[2] == datetime_seconds, "Seconds do not match"