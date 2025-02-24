import pytest
from datetime import datetime, timedelta
from src.timestamp_diff import calculate_timestamp_difference

def test_timestamp_difference_seconds():
    """Test time difference calculation in seconds"""
    t1 = datetime(2023, 1, 1, 10, 0, 0)
    t2 = datetime(2023, 1, 1, 10, 0, 30)
    assert calculate_timestamp_difference(t1, t2) == 30.0
    assert calculate_timestamp_difference(t2, t1) == 30.0

def test_timestamp_difference_minutes():
    """Test time difference calculation in minutes"""
    t1 = datetime(2023, 1, 1, 10, 0, 0)
    t2 = datetime(2023, 1, 1, 10, 15, 0)
    assert calculate_timestamp_difference(t1, t2, 'minutes') == 15.0
    assert calculate_timestamp_difference(t2, t1, 'minutes') == 15.0

def test_timestamp_difference_hours():
    """Test time difference calculation in hours"""
    t1 = datetime(2023, 1, 1, 10, 0, 0)
    t2 = datetime(2023, 1, 1, 12, 0, 0)
    assert calculate_timestamp_difference(t1, t2, 'hours') == 2.0
    assert calculate_timestamp_difference(t2, t1, 'hours') == 2.0

def test_timestamp_difference_days():
    """Test time difference calculation in days"""
    t1 = datetime(2023, 1, 1)
    t2 = datetime(2023, 1, 3)
    assert calculate_timestamp_difference(t1, t2, 'days') == 2.0
    assert calculate_timestamp_difference(t2, t1, 'days') == 2.0

def test_timestamp_difference_string_input():
    """Test time difference with ISO format string inputs"""
    t1 = "2023-01-01T10:00:00"
    t2 = "2023-01-01T10:15:00"
    assert calculate_timestamp_difference(t1, t2, 'minutes') == 15.0

def test_invalid_unit():
    """Test handling of invalid time units"""
    t1 = datetime(2023, 1, 1)
    t2 = datetime(2023, 1, 2)
    with pytest.raises(ValueError, match="Unsupported time unit"):
        calculate_timestamp_difference(t1, t2, 'weeks')

def test_invalid_timestamp_format():
    """Test handling of invalid timestamp formats"""
    with pytest.raises(ValueError, match="Invalid timestamp format"):
        calculate_timestamp_difference("invalid_format", datetime.now())

def test_invalid_timestamp_type():
    """Test handling of invalid timestamp types"""
    with pytest.raises(TypeError, match="Timestamps must be datetime or ISO format string"):
        calculate_timestamp_difference(123, 456)

def test_case_insensitive_unit():
    """Test case-insensitive time units"""
    t1 = datetime(2023, 1, 1, 10, 0, 0)
    t2 = datetime(2023, 1, 1, 11, 0, 0)
    assert calculate_timestamp_difference(t1, t2, 'HOURS') == 1.0
    assert calculate_timestamp_difference(t1, t2, 'Hours') == 1.0