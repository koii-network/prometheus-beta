import pytest
from datetime import datetime
import re
from src.time_formatter import get_current_time_formatted

def test_get_current_time_formatted():
    """
    Test that the function returns a correctly formatted time string.
    """
    # Get the formatted time
    time_str = get_current_time_formatted()
    
    # Check that the string matches HH:MM:SS format
    assert re.match(r'^\d{2}:\d{2}:\d{2}$', time_str), \
        "Time should be in HH:MM:SS format"
    
    # Verify hours are between 00-23
    hours = int(time_str.split(':')[0])
    assert 0 <= hours <= 23, "Hours should be between 00 and 23"

def test_time_format_consistency():
    """
    Verify that the function returns a consistent time format.
    """
    # Get current time via two methods for comparison
    func_time = get_current_time_formatted()
    datetime_time = datetime.now().strftime('%H:%M:%S')
    
    # Check that the lengths match
    assert len(func_time) == 8, "Time string should be 8 characters long"
    
    # Verify the format is consistent with datetime
    assert func_time == datetime_time, "Function time should match datetime format"