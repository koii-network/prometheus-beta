import pytest
from datetime import datetime, timedelta
from src.timestamp_diff import calculate_timestamp_difference

def test_timestamp_difference_seconds():
    # Test default seconds unit
    t1 = datetime(2023, 1, 1, 12, 0, 0)
    t2 = datetime(2023, 1, 1, 12, 0, 30)
    assert calculate_timestamp_difference(t1, t2) == 30

def test_timestamp_difference_minutes():
    # Test minutes unit
    t1 = datetime(2023, 1, 1, 12, 0, 0)
    t2 = datetime(2023, 1, 1, 12, 15, 0)
    assert calculate_timestamp_difference(t1, t2, 'minutes') == 15

def test_timestamp_difference_hours():
    # Test hours unit
    t1 = datetime(2023, 1, 1, 12, 0, 0)
    t2 = datetime(2023, 1, 1, 15, 0, 0)
    assert calculate_timestamp_difference(t1, t2, 'hours') == 3

def test_timestamp_difference_days():
    # Test days unit
    t1 = datetime(2023, 1, 1)
    t2 = datetime(2023, 1, 4)
    assert calculate_timestamp_difference(t1, t2, 'days') == 3

def test_timestamp_difference_string_inputs():
    # Test ISO format string inputs
    t1 = "2023-01-01T12:00:00"
    t2 = "2023-01-01T12:15:30"
    assert calculate_timestamp_difference(t1, t2, 'minutes') == 15.5

def test_timestamp_difference_order_independence():
    # Verify order doesn't matter
    t1 = datetime(2023, 1, 1, 12, 0, 0)
    t2 = datetime(2023, 1, 1, 12, 15, 0)
    assert calculate_timestamp_difference(t1, t2, 'minutes') == calculate_timestamp_difference(t2, t1, 'minutes')

def test_invalid_unit():
    # Test invalid time unit
    t1 = datetime(2023, 1, 1)
    t2 = datetime(2023, 1, 2)
    with pytest.raises(ValueError, match="Unsupported time unit"):
        calculate_timestamp_difference(t1, t2, 'weeks')

def test_invalid_timestamp_format():
    # Test invalid timestamp string
    with pytest.raises(ValueError, match="Invalid timestamp format"):
        calculate_timestamp_difference("invalid-date", datetime.now())

def test_invalid_timestamp_type():
    # Test invalid timestamp type
    with pytest.raises(TypeError, match="Timestamps must be datetime objects"):
        calculate_timestamp_difference(123, 456)