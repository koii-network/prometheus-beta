import pytest
from src.timestamp_difference import calculate_timestamp_difference

def test_calculate_timestamp_difference_same_timestamp():
    result = calculate_timestamp_difference('2023-01-01 10:00:00', '2023-01-01 10:00:00')
    assert result == {
        'days': 0,
        'hours': 0,
        'minutes': 0,
        'seconds': 0,
        'total_seconds': 0
    }

def test_calculate_timestamp_difference_hours():
    result = calculate_timestamp_difference('2023-01-01 10:00:00', '2023-01-01 14:30:00')
    assert result == {
        'days': 0,
        'hours': 4,
        'minutes': 30,
        'seconds': 0,
        'total_seconds': 16200
    }

def test_calculate_timestamp_difference_days():
    result = calculate_timestamp_difference('2023-01-01 10:00:00', '2023-01-03 14:30:00')
    assert result == {
        'days': 2,
        'hours': 4,
        'minutes': 30,
        'seconds': 0,
        'total_seconds': 186600
    }

def test_calculate_timestamp_difference_order_independence():
    result1 = calculate_timestamp_difference('2023-01-03 14:30:00', '2023-01-01 10:00:00')
    result2 = calculate_timestamp_difference('2023-01-01 10:00:00', '2023-01-03 14:30:00')
    assert result1 == result2

def test_calculate_timestamp_difference_invalid_format():
    with pytest.raises(ValueError, match="Invalid timestamp format"):
        calculate_timestamp_difference('2023/01/01 10:00:00', '2023-01-03 14:30:00')

def test_calculate_timestamp_difference_custom_format():
    result = calculate_timestamp_difference('01/01/2023 10:00:00', '01/03/2023 14:30:00', format='%m/%d/%Y %H:%M:%S')
    assert result == {
        'days': 2,
        'hours': 4,
        'minutes': 30,
        'seconds': 0,
        'total_seconds': 186600
    }