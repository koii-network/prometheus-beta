import os
import json
import pytest
from src.browser_performance_logger import BrowserPerformanceLogger

def test_log_performance_metrics():
    """
    Test that log_performance_metrics returns a dictionary with expected keys.
    """
    metrics = BrowserPerformanceLogger.log_performance_metrics()
    
    # Check that metrics is a dictionary
    assert isinstance(metrics, dict)
    
    # Check for expected keys
    expected_keys = ['timestamp', 'rendering_time', 'frame_rate', 'memory_usage', 'cpu_usage']
    for key in expected_keys:
        assert key in metrics

def test_save_performance_log(tmp_path):
    """
    Test saving performance metrics to a log file.
    """
    # Create a temporary log file
    log_file = os.path.join(tmp_path, 'performance_log.json')
    
    # Create sample metrics
    metrics = {
        'timestamp': 1234567890,
        'rendering_time': 0.05,
        'frame_rate': 60,
        'memory_usage': 100.0,
        'cpu_usage': 25.0
    }
    
    # Save the metrics
    BrowserPerformanceLogger.save_performance_log(metrics, log_file)
    
    # Verify the file was created and contains the correct data
    assert os.path.exists(log_file)
    
    # Read the log file and verify contents
    with open(log_file, 'r') as f:
        logged_metrics = json.loads(f.read().strip())
    
    assert logged_metrics == metrics

def test_save_performance_log_multiple_entries(tmp_path):
    """
    Test saving multiple performance metrics to a log file.
    """
    log_file = os.path.join(tmp_path, 'multi_performance_log.json')
    
    metrics1 = {'timestamp': 1234567890, 'rendering_time': 0.05}
    metrics2 = {'timestamp': 1234567891, 'rendering_time': 0.06}
    
    # Save multiple metrics
    BrowserPerformanceLogger.save_performance_log(metrics1, log_file)
    BrowserPerformanceLogger.save_performance_log(metrics2, log_file)
    
    # Read the log file and verify contents
    with open(log_file, 'r') as f:
        lines = f.readlines()
    
    assert len(lines) == 2
    logged_metrics1 = json.loads(lines[0].strip())
    logged_metrics2 = json.loads(lines[1].strip())
    
    assert logged_metrics1 == metrics1
    assert logged_metrics2 == metrics2