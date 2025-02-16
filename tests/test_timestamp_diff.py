import pytest
from datetime import datetime, timedelta
from src.timestamp_diff import calculate_timestamp_difference

def test_timestamp_difference_seconds():
    # Test with datetime objects
    dt1 = datetime(2023, 1, 1, 10, 0, 0)
    dt2 = datetime(2023, 1, 1, 10, 0, 30)
    assert calculate_timestamp_difference(dt1, dt2) == 30
    
    # Test with ISO format strings
    iso_dt1 = "2023-01-01T10:00:00"
    iso_dt2 = "2023-01-01T10:00:30"
    assert calculate_timestamp_difference(iso_dt1, iso_dt2) == 30

def test_timestamp_difference_minutes():
    dt1 = datetime(2023, 1, 1, 10, 0, 0)
    dt2 = datetime(2023, 1, 1, 10, 15, 0)
    assert calculate_timestamp_difference(dt1, dt2, unit='minutes') == 15

def test_timestamp_difference_hours():
    dt1 = datetime(2023, 1, 1, 10, 0, 0)
    dt2 = datetime(2023, 1, 1, 14, 0, 0)
    assert calculate_timestamp_difference(dt1, dt2, unit='hours') == 4

def test_timestamp_difference_days():
    dt1 = datetime(2023, 1, 1)
    dt2 = datetime(2023, 1, 5)
    assert calculate_timestamp_difference(dt1, dt2, unit='days') == 4

def test_timestamp_difference_order_independence():
    dt1 = datetime(2023, 1, 1, 10, 0, 0)
    dt2 = datetime(2023, 1, 1, 10, 0, 30)
    assert calculate_timestamp_difference(dt1, dt2) == calculate_timestamp_difference(dt2, dt1)

def test_invalid_timestamp_format():
    with pytest.raises(ValueError, match="Invalid timestamp format"):
        calculate_timestamp_difference("invalid", datetime.now())

def test_invalid_unit():
    dt1 = datetime(2023, 1, 1)
    dt2 = datetime(2023, 1, 2)
    with pytest.raises(ValueError, match="Unsupported time unit"):
        calculate_timestamp_difference(dt1, dt2, unit='weeks')