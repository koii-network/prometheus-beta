import os
import json
import pytest
import time
from src.browser_performance_logger import log_browser_rendering_metrics

def test_log_browser_rendering_metrics():
    # Clear any existing log files
    if os.path.exists('performance_log.json'):
        os.remove('performance_log.json')
    if os.path.exists('performance_error_log.json'):
        os.remove('performance_error_log.json')
    
    # Call the function
    metrics = log_browser_rendering_metrics()
    
    # Check metrics dictionary
    assert isinstance(metrics, dict), "Should return a dictionary of metrics"
    
    # Verify key metrics exist
    expected_keys = [
        'timestamp', 
        'first_contentful_paint', 
        'largest_contentful_paint', 
        'total_blocking_time', 
        'cumulative_layout_shift', 
        'time_to_interactive'
    ]
    for key in expected_keys:
        assert key in metrics, f"{key} should be in performance metrics"
    
    # Check logging worked
    assert os.path.exists('performance_log.json'), "Performance log file should be created"
    
    # Verify log file contents
    with open('performance_log.json', 'r') as log_file:
        log_entries = log_file.readlines()
        assert len(log_entries) > 0, "Log file should not be empty"
        
        # Try to parse the last log entry
        last_entry = json.loads(log_entries[-1])
        assert isinstance(last_entry, dict), "Log entry should be a valid JSON object"

def test_performance_metrics_types():
    metrics = log_browser_rendering_metrics()
    
    # Type checking for metrics
    assert isinstance(metrics['timestamp'], float), "Timestamp should be a float"
    assert isinstance(metrics['first_contentful_paint'], float), "First Contentful Paint should be a float"
    assert isinstance(metrics['largest_contentful_paint'], float), "Largest Contentful Paint should be a float"
    assert isinstance(metrics['total_blocking_time'], float), "Total Blocking Time should be a float"
    assert isinstance(metrics['cumulative_layout_shift'], float), "Cumulative Layout Shift should be a float"
    assert isinstance(metrics['time_to_interactive'], float), "Time to Interactive should be a float"