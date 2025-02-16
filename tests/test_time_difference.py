import pytest
from src.time_difference import calculate_time_difference

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

def test_timestamps_across_days():
    result = calculate_time_difference('2023-01-01 23:00:00', '2023-01-02 01:30:15')
    assert result == {
        'days': 0,
        'hours': 2,
        'minutes': 30,
        'seconds': 15,
        'total_seconds': 9015
    }

def test_custom_timestamp_format():
    result = calculate_time_difference('01/15/2023 14:20:30', '01/16/2023 15:25:45', format='%m/%d/%Y %H:%M:%S')
    assert result == {
        'days': 1,
        'hours': 1,
        'minutes': 5,
        'seconds': 15,
        'total_seconds': 90315  # Updated to match actual calculation
    }

def test_invalid_timestamp_format():
    with pytest.raises(ValueError, match="Invalid timestamp format"):
        calculate_time_difference('invalid', 'timestamps')

def test_order_independence():
    # Reversing timestamps should give the same result
    result1 = calculate_time_difference('2023-01-01 12:00:00', '2023-01-02 14:30:45')
    result2 = calculate_time_difference('2023-01-02 14:30:45', '2023-01-01 12:00:00')
    assert result1 == result2