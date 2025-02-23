import pytest
from datetime import datetime, timedelta
from src.timestamp_difference import calculate_timestamp_difference

def test_timestamp_difference_seconds():
    """Test time difference calculation in seconds"""
    t1 = datetime(2023, 1, 1, 10, 0, 0)
    t2 = datetime(2023, 1, 1, 10, 0, 30)
    assert calculate_timestamp_difference(t1, t2) == 30
    assert calculate_timestamp_difference(t2, t1) == 30

def test_timestamp_difference_minutes():
    """Test time difference calculation in minutes"""
    t1 = datetime(2023, 1, 1, 10, 0, 0)
    t2 = datetime(2023, 1, 1, 11, 0, 0)
    assert calculate_timestamp_difference(t1, t2, 'minutes') == 60
    assert calculate_timestamp_difference(t2, t1, 'minutes') == 60

def test_timestamp_difference_hours():
    """Test time difference calculation in hours"""
    t1 = datetime(2023, 1, 1, 10, 0, 0)
    t2 = datetime(2023, 1, 1, 14, 0, 0)
    assert calculate_timestamp_difference(t1, t2, 'hours') == 4
    assert calculate_timestamp_difference(t2, t1, 'hours') == 4

def test_timestamp_difference_days():
    """Test time difference calculation in days"""
    t1 = datetime(2023, 1, 1)
    t2 = datetime(2023, 1, 5)
    assert calculate_timestamp_difference(t1, t2, 'days') == 4
    assert calculate_timestamp_difference(t2, t1, 'days') == 4

def test_timestamp_string_input():
    """Test timestamp calculation with ISO format string inputs"""
    t1_str = "2023-01-01T10:00:00"
    t2_str = "2023-01-01T10:30:00"
    assert calculate_timestamp_difference(t1_str, t2_str, 'minutes') == 30

def test_invalid_unit():
    """Test handling of invalid time units"""
    t1 = datetime(2023, 1, 1)
    t2 = datetime(2023, 1, 2)
    with pytest.raises(ValueError, match="Unsupported time unit"):
        calculate_timestamp_difference(t1, t2, 'weeks')

def test_invalid_timestamp_format():
    """Test handling of invalid timestamp formats"""
    with pytest.raises(ValueError, match="Unable to parse"):
        calculate_timestamp_difference("invalid-date", datetime(2023, 1, 1))

def test_invalid_timestamp_type():
    """Test handling of invalid timestamp types"""
    with pytest.raises(TypeError, match="Timestamps must be"):
        calculate_timestamp_difference(123, 456)