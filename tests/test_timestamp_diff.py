import pytest
from src.timestamp_diff import calculate_timestamp_difference

def test_timestamp_difference_same_time():
    result = calculate_timestamp_difference('2023-01-01 12:00:00', '2023-01-01 12:00:00')
    assert result['total_seconds'] == 0
    assert result['days'] == 0
    assert result['hours'] == 0
    assert result['minutes'] == 0
    assert result['microseconds'] == 0

def test_timestamp_difference_hours():
    result = calculate_timestamp_difference('2023-01-01 10:00:00', '2023-01-01 14:30:00')
    assert result['total_seconds'] == 4 * 3600 + 30 * 60
    assert result['hours'] == 4.5

def test_timestamp_difference_days():
    result = calculate_timestamp_difference('2023-01-01 00:00:00', '2023-01-03 12:00:00')
    assert result['days'] == 2
    assert result['hours'] == 60

def test_custom_format():
    result = calculate_timestamp_difference('01/01/2023 12:00:00', '01/02/2023 12:00:00', format='%m/%d/%Y %H:%M:%S')
    assert result['total_seconds'] == 24 * 3600

def test_invalid_timestamp_format():
    with pytest.raises(ValueError, match='Error parsing timestamps'):
        calculate_timestamp_difference('2023-01-01', '2023-01-02')

def test_order_independence():
    result1 = calculate_timestamp_difference('2023-01-01 12:00:00', '2023-01-02 12:00:00')
    result2 = calculate_timestamp_difference('2023-01-02 12:00:00', '2023-01-01 12:00:00')
    assert result1 == result2