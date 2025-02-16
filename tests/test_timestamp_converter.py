import pytest
from datetime import datetime
from src.timestamp_converter import convert_timestamp_to_human_readable

def test_convert_timestamp_valid_integer():
    # Test a known timestamp
    timestamp = 1609459200  # January 1, 2021 00:00:00 UTC
    result = convert_timestamp_to_human_readable(timestamp)
    assert result == "January 01, 2021 at 12:00 AM"

def test_convert_timestamp_valid_float():
    # Test with a float timestamp
    timestamp = 1609459200.5  # January 1, 2021 00:00:00 UTC
    result = convert_timestamp_to_human_readable(timestamp)
    assert result == "January 01, 2021 at 12:00 AM"

def test_convert_timestamp_invalid_input():
    # Test invalid input types
    with pytest.raises(ValueError):
        convert_timestamp_to_human_readable("not a number")
    
    with pytest.raises(ValueError):
        convert_timestamp_to_human_readable(None)

def test_convert_timestamp_out_of_range():
    # Test timestamp that is out of valid range
    with pytest.raises(TypeError):
        convert_timestamp_to_human_readable(9999999999999)  # Extremely large timestamp