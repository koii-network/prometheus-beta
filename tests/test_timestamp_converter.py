import pytest
from datetime import datetime
import sys
import os

# Ensure src directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from timestamp_converter import timestamp_to_human_readable

def test_valid_timestamp():
    """Test conversion of a valid timestamp."""
    # Using a specific known timestamp (Jan 1, 2000 00:00:00 UTC)
    timestamp = 946684800
    assert timestamp_to_human_readable(timestamp) == '2000-01-01 00:00:00'

def test_current_timestamp():
    """Test conversion of current timestamp."""
    current_timestamp = datetime.now().timestamp()
    result = timestamp_to_human_readable(current_timestamp)
    # Check if result matches expected format
    assert len(result) == 19
    assert result[4] == '-' and result[7] == '-'
    assert result[10] == ' '
    assert result[13] == ':' and result[16] == ':'

def test_fractional_timestamp():
    """Test conversion of fractional timestamp."""
    timestamp = 1609459200.5  # Jan 1, 2021 00:00:00.5 UTC
    assert timestamp_to_human_readable(timestamp) == '2021-01-01 00:00:00'

def test_invalid_type_raises_error():
    """Test that non-numeric input raises TypeError."""
    with pytest.raises(TypeError):
        timestamp_to_human_readable('not a number')
    with pytest.raises(TypeError):
        timestamp_to_human_readable(None)

def test_negative_timestamp_raises_error():
    """Test that negative timestamp raises ValueError."""
    with pytest.raises(ValueError):
        timestamp_to_human_readable(-1000)

def test_extreme_large_timestamp():
    """Test very large timestamp that might cause overflow."""
    with pytest.raises(ValueError):
        # Use an extremely large timestamp that should raise an error
        timestamp_to_human_readable(2**64)