import re
import time
from src.time_utils import get_current_time

def test_get_current_time_format():
    """Test the time format matches HH:MM:SS"""
    current_time = get_current_time()
    
    # Check that the time is exactly 8 characters long
    assert len(current_time) == 8, f"Expected 8 characters, got {len(current_time)}"
    
    # Use regex to validate the HH:MM:SS format
    time_pattern = r'^\d{2}:\d{2}:\d{2}$'
    assert re.match(time_pattern, current_time), f"Invalid time format: {current_time}"

def test_get_current_time_accuracy():
    """Test that the time returned is roughly the current time"""
    # Get system time just before and after calling the function
    before_time = time.localtime()
    current_time_str = get_current_time()
    after_time = time.localtime()
    
    # Convert the current_time_str to a time object for comparison
    current_time_obj = time.strptime(current_time_str, "%H:%M:%S")
    
    # Check that the returned time is within the before and after system times
    assert (time.strptime(time.strftime("%H:%M:%S", before_time), "%H:%M:%S") <= 
            current_time_obj <= 
            time.strptime(time.strftime("%H:%M:%S", after_time), "%H:%M:%S")), \
            "Returned time is not within expected range"