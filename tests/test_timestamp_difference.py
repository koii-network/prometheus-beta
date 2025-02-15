import pytest
from datetime import datetime, timedelta
from src.timestamp_difference import calculate_timestamp_difference

def test_timestamp_difference_seconds():
    timestamp1 = datetime(2023, 1, 1, 12, 0, 0)
    timestamp2 = datetime(2023, 1, 1, 12, 0, 30)
    assert calculate_timestamp_difference(timestamp1, timestamp2) == 30.0

def test_timestamp_difference_minutes():
    timestamp1 = datetime(2023, 1, 1, 12, 0, 0)
    timestamp2 = datetime(2023, 1, 1, 12, 15, 0)
    assert calculate_timestamp_difference(timestamp1, timestamp2, unit='minutes') == 15.0

def test_timestamp_difference_hours():
    timestamp1 = datetime(2023, 1, 1, 12, 0, 0)
    timestamp2 = datetime(2023, 1, 1, 15, 0, 0)
    assert calculate_timestamp_difference(timestamp1, timestamp2, unit='hours') == 3.0

def test_timestamp_difference_days():
    timestamp1 = datetime(2023, 1, 1)
    timestamp2 = datetime(2023, 1, 5)
    assert calculate_timestamp_difference(timestamp1, timestamp2, unit='days') == 4.0

def test_string_timestamps():
    timestamp1 = "2023-01-01T12:00:00"
    timestamp2 = "2023-01-01T12:15:00"
    assert calculate_timestamp_difference(timestamp1, timestamp2, unit='minutes') == 15.0

def test_invalid_timestamp_format():
    with pytest.raises(ValueError):
        calculate_timestamp_difference("invalid-timestamp", datetime.now())

def test_invalid_unit():
    timestamp1 = datetime(2023, 1, 1)
    timestamp2 = datetime(2023, 1, 2)
    with pytest.raises(ValueError):
        calculate_timestamp_difference(timestamp1, timestamp2, unit='weeks')

def test_invalid_timestamp_type():
    with pytest.raises(TypeError):
        calculate_timestamp_difference(123, 456)