import os
import json
import pytest
import time
from src.performance_metrics import log_browser_rendering_metrics

def test_log_browser_rendering_metrics():
    # Remove any existing log files before test
    if os.path.exists('performance_log.json'):
        os.remove('performance_log.json')
    if os.path.exists('performance_error_log.json'):
        os.remove('performance_error_log.json')
    
    # Test successful metric logging
    metrics = log_browser_rendering_metrics()
    
    # Validate metrics structure
    assert isinstance(metrics, dict)
    assert 'timestamp' in metrics
    assert 'total_render_time' in metrics
    
    # Check log file creation
    assert os.path.exists('performance_log.json')
    
    # Verify log file contents
    with open('performance_log.json', 'r') as log_file:
        last_line = log_file.readlines()[-1]
        logged_metrics = json.loads(last_line)
        assert logged_metrics == metrics

def test_performance_metrics_error_handling(monkeypatch):
    # Simulate a logging error
    def mock_json_dump(*args, **kwargs):
        raise IOError("Simulated logging error")
    
    monkeypatch.setattr(json, 'dump', mock_json_dump)
    
    # Remove any existing error log
    if os.path.exists('performance_error_log.json'):
        os.remove('performance_error_log.json')
    
    # Expect an exception to be raised
    with pytest.raises(Exception):
        log_browser_rendering_metrics()
    
    # Check that error was logged
    assert os.path.exists('performance_error_log.json')
    
    # Verify error log contents
    with open('performance_error_log.json', 'r') as error_log:
        last_line = error_log.readlines()[-1]
        error_metrics = json.loads(last_line)
        assert 'error' in error_metrics
        assert 'timestamp' in error_metrics