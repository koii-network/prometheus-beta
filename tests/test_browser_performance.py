import pytest
import time
from src.browser_performance import log_browser_performance_metrics

def test_log_browser_performance_default():
    """Test default performance metrics logging"""
    result = log_browser_performance_metrics()
    
    assert isinstance(result, dict)
    assert 'total_entries' in result
    assert 'performance_metrics' in result
    assert 'total_duration' in result
    assert result['total_entries'] > 0

def test_log_browser_performance_custom_entries():
    """Test logging with custom performance entries"""
    custom_entries = [
        {
            'name': 'test-paint',
            'startTime': 50,
            'duration': 25
        },
        {
            'name': 'another-paint',
            'startTime': 100,
            'duration': 75
        }
    ]
    
    result = log_browser_performance_metrics(custom_entries)
    
    assert result['total_entries'] == 2
    assert len(result['performance_metrics']) == 2
    assert result['total_duration'] == 100

def test_log_browser_performance_invalid_input():
    """Test error handling for invalid input"""
    result_non_list = log_browser_performance_metrics("not a list")
    assert 'error' in result_non_list
    
    invalid_entries = [
        "not a dictionary",
        {"incomplete": "entry"}
    ]
    
    result_invalid_entries = log_browser_performance_metrics(invalid_entries)
    assert 'error' in result_invalid_entries

def test_log_browser_performance_empty_list():
    """Test behavior with an empty list of performance entries"""
    result = log_browser_performance_metrics([])
    
    assert result['total_entries'] == 0
    assert result['total_duration'] == 0
    assert result['performance_metrics'] == []

def test_log_browser_performance_error_handling():
    """Test error handling returns dictionary with error info"""
    # Invalid entries with missing required keys
    bad_entries = [
        {'name': 'missing-keys'},
        {'startTime': 100}
    ]
    
    result = log_browser_performance_metrics(bad_entries)
    
    assert 'error' in result
    assert 'timestamp' in result
    assert isinstance(result['timestamp'], float)