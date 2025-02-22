import pytest
from datetime import datetime
import time
from src.time_formatter import get_current_time_formatted

def test_get_current_time_formatted():
    # Test the format of the returned time string
    time_str = get_current_time_formatted()
    
    # Check that the string matches the HH:MM:SS format
    assert len(time_str) == 8, "Time string should be 8 characters long"
    assert time_str[2] == ":" and time_str[5] == ":", "Colons should be in correct positions"
    
    # Validate hours, minutes, and seconds are within valid ranges
    hours, minutes, seconds = time_str.split(":")
    assert 0 <= int(hours) <= 23, "Hours should be between 0 and 23"
    assert 0 <= int(minutes) <= 59, "Minutes should be between 0 and 59"
    assert 0 <= int(seconds) <= 59, "Seconds should be between 0 and 59"

def test_time_changes():
    # Verify that multiple calls return different times
    time1 = get_current_time_formatted()
    time.sleep(1)  # Wait a second
    time2 = get_current_time_formatted()
    
    assert time1 != time2, "Time should change between calls"