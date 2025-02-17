import pytest
from datetime import datetime
from src.time_formatter import get_current_time_formatted

def test_get_current_time_formatted():
    # Get the formatted time
    formatted_time = get_current_time_formatted()
    
    # Check that the result is a string
    assert isinstance(formatted_time, str), "Result should be a string"
    
    # Check the format matches HH:MM:SS
    assert len(formatted_time) == 8, "Time string should be 8 characters long"
    assert formatted_time[2] == ":" and formatted_time[5] == ":", "Time should use ':' as separators"
    
    # Validate hour part (00-23)
    hour = int(formatted_time[:2])
    assert 0 <= hour <= 23, "Hour should be between 00 and 23"
    
    # Validate minute part (00-59)
    minute = int(formatted_time[3:5])
    assert 0 <= minute <= 59, "Minutes should be between 00 and 59"
    
    # Validate second part (00-59)
    second = int(formatted_time[6:])
    assert 0 <= second <= 59, "Seconds should be between 00 and 59"
    
def test_time_format_matches_datetime():
    # Compare function output with datetime's strftime
    formatted_time = get_current_time_formatted()
    datetime_time = datetime.now().strftime("%H:%M:%S")
    
    assert formatted_time == datetime_time, "Time should match datetime's format"