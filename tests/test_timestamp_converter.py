import pytest
from datetime import datetime
from src.timestamp_converter import convert_timestamp_to_human_readable

def test_convert_timestamp_valid_input():
    # Test a known timestamp
    timestamp = 1609459200  # January 1, 2021 00:00:00 UTC
    assert convert_timestamp_to_human_readable(timestamp) == "January 01, 2021"

def test_convert_timestamp_current_time():
    # Test current time timestamp
    current_timestamp = datetime.now().timestamp()
    result = convert_timestamp_to_human_readable(current_timestamp)
    assert isinstance(result, str)
    assert len(result.split()) == 3  # Month Day, Year format

def test_convert_timestamp_float_input():
    # Test with float timestamp
    timestamp = 1609459200.5  # Fractional timestamp
    assert convert_timestamp_to_human_readable(timestamp) == "January 01, 2021"

def test_convert_timestamp_invalid_type():
    # Test with invalid input types
    with pytest.raises(TypeError):
        convert_timestamp_to_human_readable("not a timestamp")
    with pytest.raises(TypeError):
        convert_timestamp_to_human_readable(None)
    with pytest.raises(TypeError):
        convert_timestamp_to_human_readable([1234])

def test_convert_timestamp_negative():
    # Test with negative timestamp
    with pytest.raises(ValueError):
        convert_timestamp_to_human_readable(-1234)