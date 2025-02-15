import pytest
from src.timestamp_diff import calculate_timestamp_difference

def test_same_timestamp():
    result = calculate_timestamp_difference('2023-01-01 10:00:00', '2023-01-01 10:00:00')
    assert result == {
        'total_seconds': 0,
        'days': 0,
        'hours': 0,
        'minutes': 0,
        'seconds': 0
    }

def test_one_hour_difference():
    result = calculate_timestamp_difference('2023-01-01 10:00:00', '2023-01-01 11:00:00')
    assert result == {
        'total_seconds': 3600,
        'days': 0,
        'hours': 1,
        'minutes': 0,
        'seconds': 0
    }

def test_multiple_days_difference():
    result = calculate_timestamp_difference('2023-01-01 00:00:00', '2023-01-03 12:30:45')
    assert result == {
        'total_seconds': 134745,
        'days': 2,
        'hours': 12,
        'minutes': 45,
        'seconds': 45
    }

def test_invalid_timestamp_format():
    with pytest.raises(ValueError, match="Error parsing timestamps"):
        calculate_timestamp_difference('2023/01/01 10:00:00', '2023-01-01 11:00:00')

def test_custom_format():
    result = calculate_timestamp_difference('01/01/2023 10:00:00', '01/01/2023 11:00:00', format='%m/%d/%Y %H:%M:%S')
    assert result == {
        'total_seconds': 3600,
        'days': 0,
        'hours': 1,
        'minutes': 0,
        'seconds': 0
    }

def test_reversed_timestamps():
    result = calculate_timestamp_difference('2023-01-01 11:00:00', '2023-01-01 10:00:00')
    assert result == {
        'total_seconds': 3600,
        'days': 0,
        'hours': 1,
        'minutes': 0,
        'seconds': 0
    }