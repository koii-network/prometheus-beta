import re
from datetime import datetime
import time
from src.time_formatter import get_current_time_formatted

def test_current_time_format():
    """Test that the function returns a valid time string in HH:MM:SS format."""
    current_time = get_current_time_formatted()
    
    # Check the format matches HH:MM:SS
    assert re.match(r'^\d{2}:\d{2}:\d{2}$', current_time), "Time format is incorrect"

def test_time_format_consistency():
    """Verify that the function returns a consistent time format."""
    times = [get_current_time_formatted() for _ in range(3)]
    
    # Each time should match the HH:MM:SS format
    for t in times:
        assert re.match(r'^\d{2}:\d{2}:\d{2}$', t), f"Invalid time format: {t}"

def test_time_precision():
    """Check that the time can change between calls."""
    time1 = get_current_time_formatted()
    time.sleep(1.1)  # Wait a bit to ensure time changes
    time2 = get_current_time_formatted()
    
    assert time1 != time2, "Time did not update between calls"