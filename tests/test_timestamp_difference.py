import pytest
from datetime import datetime, timedelta
from src.timestamp_difference import calculate_timestamp_difference

def test_timestamp_difference_seconds():
    t1 = datetime(2023, 1, 1, 12, 0, 0)
    t2 = datetime(2023, 1, 1, 12, 0, 30)
    assert calculate_timestamp_difference(t1, t2) == 30
    assert calculate_timestamp_difference(t2, t1) == 30

def test_timestamp_difference_minutes():
    t1 = datetime(2023, 1, 1, 12, 0, 0)
    t2 = datetime(2023, 1, 1, 12, 15, 0)
    assert calculate_timestamp_difference(t1, t2, 'minutes') == 15
    assert calculate_timestamp_difference(t2, t1, 'minutes') == 15

def test_timestamp_difference_hours():
    t1 = datetime(2023, 1, 1, 12, 0, 0)
    t2 = datetime(2023, 1, 1, 15, 0, 0)
    assert calculate_timestamp_difference(t1, t2, 'hours') == 3
    assert calculate_timestamp_difference(t2, t1, 'hours') == 3

def test_timestamp_difference_days():
    t1 = datetime(2023, 1, 1)
    t2 = datetime(2023, 1, 4)
    assert calculate_timestamp_difference(t1, t2, 'days') == 3
    assert calculate_timestamp_difference(t2, t1, 'days') == 3

def test_timestamp_difference_string_input():
    t1 = "2023-01-01T12:00:00"
    t2 = "2023-01-01T12:30:00"
    assert calculate_timestamp_difference(t1, t2) == 1800

def test_invalid_unit():
    t1 = datetime(2023, 1, 1)
    t2 = datetime(2023, 1, 2)
    with pytest.raises(ValueError, match="Invalid unit"):
        calculate_timestamp_difference(t1, t2, 'weeks')

def test_invalid_timestamp_format():
    with pytest.raises(ValueError, match="Invalid format"):
        calculate_timestamp_difference("2023/01/01", datetime(2023, 1, 2))

def test_invalid_timestamp_type():
    with pytest.raises(TypeError, match="Timestamps must be datetime"):
        calculate_timestamp_difference(123, 456)