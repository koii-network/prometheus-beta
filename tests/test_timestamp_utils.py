import pytest
from src.timestamp_utils import calculate_time_difference

def test_same_timestamp():
    result = calculate_time_difference('2023-01-01 12:00:00', '2023-01-01 12:00:00')
    assert result == {
        'days': 0,
        'hours': 0,
        'minutes': 0,
        'seconds': 0,
        'total_seconds': 0
    }

def test_different_timestamps():
    result = calculate_time_difference('2023-01-01 10:00:00', '2023-01-01 12:30:45')
    assert result == {
        'days': 0,
        'hours': 2,
        'minutes': 30,
        'seconds': 45,
        'total_seconds': 9045
    }

def test_timestamps_on_different_days():
    result = calculate_time_difference('2023-01-01 00:00:00', '2023-01-02 12:30:45')
    assert result == {
        'days': 1,
        'hours': 12,
        'minutes': 30,
        'seconds': 45,
        'total_seconds': 112245
    }

def test_timestamps_reverse_order():
    result = calculate_time_difference('2023-01-02 12:30:45', '2023-01-01 00:00:00')
    assert result == {
        'days': 1,
        'hours': 12,
        'minutes': 30,
        'seconds': 45,
        'total_seconds': 112245
    }

def test_invalid_timestamp_format():
    with pytest.raises(ValueError, match="Invalid timestamp format"):
        calculate_time_difference('2023/01/01 12:00:00', '2023-01-01 12:00:00')

def test_custom_timestamp_format():
    result = calculate_time_difference('01/01/2023 12:00:00', '01/01/2023 13:30:45', format='%m/%d/%Y %H:%M:%S')
    assert result == {
        'days': 0,
        'hours': 1,
        'minutes': 30,
        'seconds': 45,
        'total_seconds': 5445
    }