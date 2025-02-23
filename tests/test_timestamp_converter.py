import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from timestamp_converter import timestamp_to_human_readable

def test_valid_timestamp():
    """Test conversion of a standard timestamp"""
    # January 1, 2000 at midnight UTC
    assert timestamp_to_human_readable(946684800) == 'January 01, 2000'

def test_fractional_timestamp():
    """Test conversion of a fractional timestamp"""
    # Partial second should still work
    assert timestamp_to_human_readable(1609459200.5) == 'January 01, 2021'

def test_current_timestamp():
    """Test conversion of current timestamp"""
    import datetime
    current_timestamp = datetime.datetime.now().timestamp()
    result = timestamp_to_human_readable(current_timestamp)
    assert isinstance(result, str)
    assert len(result) > 0

def test_invalid_type_string():
    """Test that a string input raises a TypeError"""
    with pytest.raises(TypeError, match="Timestamp must be an integer or float"):
        timestamp_to_human_readable("not a timestamp")

def test_invalid_type_none():
    """Test that None input raises a TypeError"""
    with pytest.raises(TypeError, match="Timestamp must be an integer or float"):
        timestamp_to_human_readable(None)

def test_invalid_timestamp():
    """Test extremely large or invalid timestamp"""
    with pytest.raises(ValueError, match="Invalid timestamp: Unable to convert to date"):
        # An extremely large timestamp that can't be converted
        timestamp_to_human_readable(99999999999999999999)

def test_negative_timestamp():
    """Test conversion of a negative timestamp"""
    # December 31, 1969
    assert timestamp_to_human_readable(-86400) == 'December 31, 1969'