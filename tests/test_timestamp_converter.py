import pytest
from datetime import datetime
from src.timestamp_converter import convert_timestamp_to_human_readable

def test_convert_timestamp_to_human_readable_standard_case():
    # Test a known timestamp
    timestamp = 1609459200  # January 1, 2021 00:00:00 UTC
    assert convert_timestamp_to_human_readable(timestamp) == "January 01, 2021"

def test_convert_timestamp_to_human_readable_float_timestamp():
    # Test float timestamp
    timestamp = 1625097600.0  # July 1, 2021 00:00:00 UTC
    assert convert_timestamp_to_human_readable(timestamp) == "July 01, 2021"

def test_convert_timestamp_to_human_readable_invalid_type():
    # Test invalid input types
    with pytest.raises(TypeError):
        convert_timestamp_to_human_readable("not a timestamp")
    
    with pytest.raises(TypeError):
        convert_timestamp_to_human_readable(None)

def test_convert_timestamp_to_human_readable_invalid_timestamp():
    # Test extremely large or invalid timestamp
    with pytest.raises(ValueError):
        convert_timestamp_to_human_readable(99999999999999999)

def test_convert_timestamp_to_human_readable_zero_timestamp():
    # Test zero timestamp
    timestamp = 0  # Unix epoch start
    assert convert_timestamp_to_human_readable(timestamp) == "January 01, 1970"