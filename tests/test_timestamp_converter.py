import pytest
from src.timestamp_converter import convert_timestamp_to_human_readable

def test_valid_timestamp():
    # Test a known timestamp (January 1, 2000)
    assert convert_timestamp_to_human_readable(946684800) == "January 01, 2000"

def test_recent_timestamp():
    # Test a more recent timestamp
    assert convert_timestamp_to_human_readable(1609459200) == "January 01, 2021"

def test_invalid_timestamp_type():
    # Test non-numeric input
    with pytest.raises(TypeError, match="Timestamp must be a number"):
        convert_timestamp_to_human_readable("not a number")

def test_negative_timestamp():
    # Test negative timestamp
    with pytest.raises(ValueError, match="Timestamp cannot be negative"):
        convert_timestamp_to_human_readable(-1000)

def test_large_timestamp():
    # Test extremely large timestamp
    with pytest.raises(ValueError, match="Invalid timestamp"):
        convert_timestamp_to_human_readable(9999999999999)

def test_zero_timestamp():
    # Test zero timestamp (January 1, 1970)
    assert convert_timestamp_to_human_readable(0) == "January 01, 1970"

def test_float_timestamp():
    # Test float timestamp
    assert convert_timestamp_to_human_readable(1609459200.5) == "January 01, 2021"