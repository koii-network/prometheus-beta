import pytest
from src.timestamp_converter import convert_timestamp_to_human_readable

def test_valid_timestamp():
    """Test conversion of a standard timestamp."""
    assert convert_timestamp_to_human_readable(1609459200) == "January 01, 2021"

def test_current_timestamp():
    """Test conversion of a current timestamp."""
    from datetime import datetime
    current_timestamp = datetime.now().timestamp()
    result = convert_timestamp_to_human_readable(current_timestamp)
    assert isinstance(result, str)
    assert len(result.split(", ")) == 2

def test_invalid_timestamp_type():
    """Test that TypeError is raised for invalid input types."""
    with pytest.raises(TypeError):
        convert_timestamp_to_human_readable("not a timestamp")
    with pytest.raises(TypeError):
        convert_timestamp_to_human_readable(None)

def test_invalid_timestamp_value():
    """Test that ValueError is raised for invalid timestamp values."""
    with pytest.raises(ValueError):
        convert_timestamp_to_human_readable(float('inf'))
    with pytest.raises(ValueError):
        convert_timestamp_to_human_readable(-1e20)  # Extremely large negative number