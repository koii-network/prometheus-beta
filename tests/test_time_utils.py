import re
from datetime import datetime
import time
import pytest
from src.time_utils import get_current_time

def test_get_current_time_format():
    """Test that the returned time string matches HH:MM:SS format."""
    current_time_str = get_current_time()
    
    # Check that the format matches HH:MM:SS using regex
    assert re.match(r'^\d{2}:\d{2}:\d{2}$', current_time_str), \
        f"Time format is incorrect. Got: {current_time_str}"

def test_get_current_time_accuracy():
    """Test that the returned time is reasonably close to the actual current time."""
    # Get system time before and after function call
    before_time = datetime.now()
    time_str = get_current_time()
    after_time = datetime.now()
    
    # Convert time string to datetime
    time_obj = datetime.strptime(time_str, "%H:%M:%S").time()
    current_datetime = datetime.now()
    
    # Ensure the time is within the range of before and after calls
    assert before_time.time() <= time_obj <= after_time.time(), \
        f"Returned time {time_str} is not within the expected range"

def test_get_current_time_consistency():
    """Verify that consecutive calls return times that progress forward."""
    time1 = get_current_time()
    time.sleep(1)  # Wait a second
    time2 = get_current_time()
    
    # Convert to datetime.time objects for comparison
    time1_obj = datetime.strptime(time1, "%H:%M:%S").time()
    time2_obj = datetime.strptime(time2, "%H:%M:%S").time()
    
    # Ensure time progresses (handles midnight rollover scenario)
    assert time1 != time2, "Consecutive time calls should not be exactly the same"