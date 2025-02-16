import pytest
from datetime import datetime
from src.timestamp_converter import timestamp_to_human_readable_date

def test_valid_timestamp():
    # Test a known timestamp
    timestamp = 1609459200  # January 1, 2021 00:00:00 UTC
    assert timestamp_to_human_readable_date(timestamp) == "January 01, 2021"

def test_current_timestamp():
    # Test current timestamp
    current_timestamp = datetime.now().timestamp()
    result = timestamp_to_human_readable_date(current_timestamp)
    assert isinstance(result, str)
    assert len(result.split()) == 3  # Should be in format "Month Day, Year"

def test_float_timestamp():
    # Test float timestamp
    timestamp = 1609459200.5  # Slightly after midnight
    assert timestamp_to_human_readable_date(timestamp) == "January 01, 2021"

def test_invalid_type():
    # Test invalid input types
    with pytest.raises(TypeError):
        timestamp_to_human_readable_date("not a timestamp")
    
    with pytest.raises(TypeError):
        timestamp_to_human_readable_date(None)

def test_invalid_timestamp():
    # Test extremely large or small timestamps
    with pytest.raises(ValueError):
        timestamp_to_human_readable_date(99999999999999)
    
    with pytest.raises(ValueError):
        timestamp_to_human_readable_date(-99999999999999)