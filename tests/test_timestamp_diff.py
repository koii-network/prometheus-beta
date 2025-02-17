import pytest
from src.timestamp_diff import calculate_timestamp_difference

def test_same_timestamp():
    result = calculate_timestamp_difference('2023-01-01 10:00:00', '2023-01-01 10:00:00')
    assert result == {
        'days': 0,
        'hours': 0,
        'minutes': 0,
        'seconds': 0,
        'total_seconds': 0
    }

def test_different_timestamps():
    result = calculate_timestamp_difference('2023-01-01 10:00:00', '2023-01-01 11:30:45')
    assert result == {
        'days': 0,
        'hours': 1,
        'minutes': 30,
        'seconds': 45,
        'total_seconds': 5445
    }

def test_timestamps_across_days():
    result = calculate_timestamp_difference('2023-01-01 22:00:00', '2023-01-02 02:30:15')
    assert result == {
        'days': 0,
        'hours': 4,
        'minutes': 30,
        'seconds': 15,
        'total_seconds': 16215
    }

def test_invalid_timestamp_format():
    with pytest.raises(ValueError, match="Invalid timestamp format"):
        calculate_timestamp_difference('2023/01/01 10:00:00', '2023-01-01 11:00:00')

def test_custom_time_format():
    result = calculate_timestamp_difference('01/01/2023 10:00:00', '01/01/2023 11:30:45', time_format='%m/%d/%Y %H:%M:%S')
    assert result == {
        'days': 0,
        'hours': 1,
        'minutes': 30,
        'seconds': 45,
        'total_seconds': 5445
    }

def test_reversed_timestamps():
    result = calculate_timestamp_difference('2023-01-01 11:30:45', '2023-01-01 10:00:00')
    assert result == {
        'days': 0,
        'hours': 1,
        'minutes': 30,
        'seconds': 45,
        'total_seconds': 5445
    }