import pytest
from datetime import datetime
from src.time_utils import get_current_time_formatted

def test_get_current_time_formatted():
    # Get the current time formatting directly from datetime
    expected_format = datetime.now().strftime("%H:%M:%S")
    
    # Call the function
    result = get_current_time_formatted()
    
    # Check that the result matches the expected format
    assert isinstance(result, str), "Result should be a string"
    assert len(result) == 8, "Time string should be 8 characters long (HH:MM:SS)"
    
    # Check format components
    parts = result.split(':')
    assert len(parts) == 3, "Time should have 3 parts separated by ':'"
    
    # Validate hours, minutes, seconds are within valid ranges
    assert 0 <= int(parts[0]) <= 23, "Hours should be between 0 and 23"
    assert 0 <= int(parts[1]) <= 59, "Minutes should be between 0 and 59"
    assert 0 <= int(parts[2]) <= 59, "Seconds should be between 0 and 59"