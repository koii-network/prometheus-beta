import os
import json
import pytest
import time
from src.performance_metrics import log_browser_rendering_metrics

def test_log_browser_rendering_metrics():
    # Remove any existing log files before test
    if os.path.exists('logs/performance_log.json'):
        os.remove('logs/performance_log.json')
    if os.path.exists('logs/performance_error_log.json'):
        os.remove('logs/performance_error_log.json')
    
    # Test successful metric logging
    metrics = log_browser_rendering_metrics()
    
    # Validate metrics structure
    assert isinstance(metrics, dict)
    assert 'timestamp' in metrics
    assert 'total_render_time' in metrics
    
    # Check log file creation
    assert os.path.exists('logs/performance_log.json')
    
    # Verify log file contents
    with open('logs/performance_log.json', 'r') as log_file:
        last_line = log_file.readlines()[-1]
        logged_metrics = json.loads(last_line)
        assert logged_metrics == metrics

def test_performance_metrics_error_handling(monkeypatch, tmp_path):
    # Simulate a logging error by making the log file not writable
    mock_log_path = tmp_path / 'logs'
    mock_log_path.mkdir()
    mock_performance_log = mock_log_path / 'performance_log.json'
    mock_performance_log.touch(mode=0o444)  # Read-only
    
    # Monkeypatch the log path to use our mock path
    monkeypatch.setattr('src.performance_metrics.os.path.exists', lambda x: True)
    monkeypatch.setattr('src.performance_metrics.os.makedirs', lambda path, exist_ok=True: None)
    
    # Temporarily modify the function to use the mock path
    original_open = open
    def mock_open(*args, **kwargs):
        if 'logs/performance_log.json' in args[0]:
            return original_open(str(mock_performance_log), *args[1:])
        return original_open(*args, **kwargs)
    
    monkeypatch.setattr('builtins.open', mock_open)
    
    # Expect an exception to be raised
    with pytest.raises(PermissionError):
        log_browser_rendering_metrics()