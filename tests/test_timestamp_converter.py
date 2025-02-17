import pytest
from src.timestamp_converter import convert_timestamp_to_human_readable

def test_valid_timestamp():
    # Test a known timestamp
    assert convert_timestamp_to_human_readable(1609459200) == "January 01, 2021"

def test_float_timestamp():
    # Test with a float timestamp
    assert convert_timestamp_to_human_readable(1609459200.0) == "January 01, 2021"

def test_invalid_type():
    # Test invalid input types
    with pytest.raises(TypeError):
        convert_timestamp_to_human_readable("not a timestamp")
    
    with pytest.raises(TypeError):
        convert_timestamp_to_human_readable(None)

def test_invalid_timestamp():
    # Test invalid timestamp values
    with pytest.raises(ValueError):
        convert_timestamp_to_human_readable(float('inf'))
    
    with pytest.raises(ValueError):
        convert_timestamp_to_human_readable(-1)  # Negative timestamp