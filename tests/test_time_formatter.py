import pytest
from datetime import datetime
import re
from src.time_formatter import get_current_time_formatted

def test_get_current_time_formatted():
    """Test that the function returns a time string in the correct format."""
    time_str = get_current_time_formatted()
    
    # Check that the string matches HH:MM:SS format
    assert re.match(r'^\d{2}:\d{2}:\d{2}$', time_str), "Time format should be HH:MM:SS"
    
    # Verify each part is within valid ranges
    hours, minutes, seconds = map(int, time_str.split(':'))
    assert 0 <= hours < 24, "Hours should be between 0 and 23"
    assert 0 <= minutes < 60, "Minutes should be between 0 and 59"
    assert 0 <= seconds < 60, "Seconds should be between 0 and 59"

def test_get_current_time_formatted_returns_current_time():
    """Test that the returned time is very close to the actual current time."""
    formatted_time = get_current_time_formatted()
    current_time = datetime.now().strftime('%H:%M:%S')
    
    # Allow a small time difference of 1 second to account for processing time
    assert formatted_time == current_time or \
           formatted_time == (datetime.now() - timedelta(seconds=1)).strftime('%H:%M:%S'), \
           "Returned time should match current time"