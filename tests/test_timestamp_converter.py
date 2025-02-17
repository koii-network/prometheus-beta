import pytest
from src.timestamp_converter import timestamp_to_human_readable

def test_valid_timestamp():
    # Test a known timestamp
    assert timestamp_to_human_readable(1609459200) == "January 01, 2021"

def test_different_timestamp():
    # Another test case
    assert timestamp_to_human_readable(1577836800) == "January 01, 2020"

def test_current_timestamp():
    # Test with a more recent timestamp
    result = timestamp_to_human_readable(1672531200)
    assert result == "January 01, 2023"

def test_invalid_type():
    # Test invalid input types
    with pytest.raises(TypeError):
        timestamp_to_human_readable("not a number")
    
    with pytest.raises(TypeError):
        timestamp_to_human_readable(None)

def test_invalid_timestamp():
    # Test extremely large or invalid timestamp
    with pytest.raises(ValueError):
        timestamp_to_human_readable(99999999999999)  # Unreasonably large timestamp

def test_zero_timestamp():
    # Test timestamp of 0 (Unix epoch start)
    assert timestamp_to_human_readable(0) == "January 01, 1970"