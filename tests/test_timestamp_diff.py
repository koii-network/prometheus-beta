import pytest
from src.timestamp_diff import calculate_time_difference

def test_calculate_time_difference_same_timestamp():
    result = calculate_time_difference('2023-01-01 10:00:00', '2023-01-01 10:00:00')
    assert result == {'days': 0, 'hours': 0, 'minutes': 0, 'seconds': 0, 'total_seconds': 0}

def test_calculate_time_difference_hours():
    result = calculate_time_difference('2023-01-01 10:00:00', '2023-01-01 12:30:00')
    assert result == {'days': 0, 'hours': 2, 'minutes': 30, 'seconds': 0, 'total_seconds': 9000}

def test_calculate_time_difference_days():
    result = calculate_time_difference('2023-01-01 00:00:00', '2023-01-03 12:30:00')
    assert result == {'days': 2, 'hours': 12, 'minutes': 30, 'seconds': 0, 'total_seconds': 216600}

def test_calculate_time_difference_custom_format():
    result = calculate_time_difference('01/01/2023 10:00:00', '01/01/2023 12:30:00', format='%m/%d/%Y %H:%M:%S')
    assert result == {'days': 0, 'hours': 2, 'minutes': 30, 'seconds': 0, 'total_seconds': 9000}

def test_calculate_time_difference_invalid_format():
    with pytest.raises(ValueError, match="Error parsing timestamps"):
        calculate_time_difference('invalid', 'format')

def test_calculate_time_difference_reverse_order():
    result = calculate_time_difference('2023-01-03 12:30:00', '2023-01-01 00:00:00')
    assert result == {'days': 2, 'hours': 12, 'minutes': 30, 'seconds': 0, 'total_seconds': 216600}