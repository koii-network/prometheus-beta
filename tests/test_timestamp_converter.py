import pytest
from src.timestamp_converter import convert_timestamp_to_human_readable

def test_convert_timestamp_to_human_readable_positive_case():
    """Test conversion of a known timestamp to human-readable date."""
    # January 1st, 2023 at 00:00:00 UTC
    timestamp = 1672531200
    assert convert_timestamp_to_human_readable(timestamp) == "January 01, 2023"

def test_convert_timestamp_to_human_readable_float_input():
    """Test conversion with a float timestamp."""
    # March 15th, 2023 at 12:30:45 UTC
    timestamp = 1678883445.5
    assert convert_timestamp_to_human_readable(timestamp) == "March 15, 2023"

def test_convert_timestamp_to_human_readable_invalid_type():
    """Test that TypeError is raised for invalid input types."""
    with pytest.raises(TypeError):
        convert_timestamp_to_human_readable("not a timestamp")
    
    with pytest.raises(TypeError):
        convert_timestamp_to_human_readable(None)

def test_convert_timestamp_to_human_readable_invalid_timestamp():
    """Test that ValueError is raised for invalid timestamp values."""
    with pytest.raises(ValueError):
        convert_timestamp_to_human_readable(float('inf'))
    
    with pytest.raises(ValueError):
        convert_timestamp_to_human_readable(-1e20)  # Extremely large negative value