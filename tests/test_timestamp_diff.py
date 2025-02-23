import pytest
from datetime import datetime, timedelta
from src.timestamp_diff import calculate_timestamp_difference

def test_basic_timestamp_difference():
    """Test basic timestamp difference calculation"""
    ts1 = '2023-06-15T10:30:00'
    ts2 = '2023-06-15T11:45:30'
    expected_diff = 4530  # 1 hour and 15 minutes and 30 seconds = 4530 seconds
    
    assert calculate_timestamp_difference(ts1, ts2) == pytest.approx(expected_diff)

def test_reverse_order_timestamps():
    """Test that order of timestamps doesn't matter"""
    ts1 = '2023-06-15T11:45:30'
    ts2 = '2023-06-15T10:30:00'
    expected_diff = 4530  # 1 hour and 15 minutes and 30 seconds = 4530 seconds
    
    assert calculate_timestamp_difference(ts1, ts2) == pytest.approx(expected_diff)

def test_same_timestamp():
    """Test timestamps that are exactly the same"""
    ts = '2023-06-15T10:30:00'
    
    assert calculate_timestamp_difference(ts, ts) == pytest.approx(0)

def test_invalid_timestamp_format():
    """Test handling of invalid timestamp formats"""
    with pytest.raises(ValueError, match="Invalid timestamp format"):
        calculate_timestamp_difference('2023/06/15 10:30:00', '2023-06-15T11:45:30')

def test_different_date_timestamps():
    """Test timestamps on different dates"""
    ts1 = '2023-06-15T10:30:00'
    ts2 = '2023-06-16T10:30:00'
    expected_diff = 86400  # Exactly 24 hours
    
    assert calculate_timestamp_difference(ts1, ts2) == pytest.approx(expected_diff)

def test_microsecond_precision():
    """Test timestamps with microsecond precision"""
    ts1 = '2023-06-15T10:30:00.123456'
    ts2 = '2023-06-15T10:30:01.654321'
    expected_diff = 1.530865  # Difference in seconds
    
    assert calculate_timestamp_difference(ts1, ts2) == pytest.approx(expected_diff)