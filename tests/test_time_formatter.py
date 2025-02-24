"""
Unit tests for time formatting function.
"""

import re
from datetime import datetime
import pytest
from src.time_formatter import get_current_time_formatted

def test_time_format():
    """
    Test that the returned time string matches the expected format HH:MM:SS.
    """
    # Get the formatted time
    formatted_time = get_current_time_formatted()
    
    # Regex pattern to match HH:MM:SS format
    time_pattern = r'^\d{2}:\d{2}:\d{2}$'
    
    # Assert that the formatted time matches the expected pattern
    assert re.match(time_pattern, formatted_time), \
        f"Time format is incorrect. Got: {formatted_time}"

def test_time_accuracy():
    """
    Test that the formatted time is close to the current time.
    """
    # Get current time and formatted time within the same method call
    current_time = datetime.now()
    formatted_time = get_current_time_formatted()
    
    # Parse the formatted time
    formatted_datetime = datetime.strptime(formatted_time, "%H:%M:%S")
    
    # Reconstruct a full datetime with the same time components
    reconstructed_datetime = current_time.replace(
        hour=formatted_datetime.hour, 
        minute=formatted_datetime.minute, 
        second=formatted_datetime.second,
        microsecond=0
    )
    
    # Ensure the times are very close (within 1 second)
    assert abs((current_time - reconstructed_datetime).total_seconds()) < 1, \
        "Formatted time does not match current time"

def test_return_type():
    """
    Verify that the function returns a string.
    """
    assert isinstance(get_current_time_formatted(), str), \
        "Function should return a string"