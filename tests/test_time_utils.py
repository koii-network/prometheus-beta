import pytest
from datetime import datetime
from src.time_utils import get_current_time_formatted

def test_get_current_time_formatted():
    # Get the current time from datetime and our function
    current_time = datetime.now().strftime("%H:%M:%S")
    func_time = get_current_time_formatted()
    
    # Check that the returned time matches the expected format
    assert len(func_time) == 8, "Time string should be 8 characters long"
    assert func_time.count(':') == 2, "Time string should contain two colons"
    
    # Verify the time is the current time
    assert func_time == current_time, "Returned time should match current time"

def test_time_format():
    # Additional test to verify the format
    time_str = get_current_time_formatted()
    
    # Split the time string and check each component
    hours, minutes, seconds = time_str.split(':')
    
    # Check that each component is a valid two-digit number
    assert len(hours) == 2 and hours.isdigit(), "Hours should be two digits"
    assert len(minutes) == 2 and minutes.isdigit(), "Minutes should be two digits"
    assert len(seconds) == 2 and seconds.isdigit(), "Seconds should be two digits"
    
    # Check ranges
    assert 0 <= int(hours) <= 23, "Hours should be between 0 and 23"
    assert 0 <= int(minutes) <= 59, "Minutes should be between 0 and 59"
    assert 0 <= int(seconds) <= 59, "Seconds should be between 0 and 59"