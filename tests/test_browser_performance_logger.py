import pytest
import time
import logging
from src.browser_performance_logger import log_browser_rendering_metrics

def test_log_browser_rendering_metrics():
    # Test successful metrics collection
    metrics = log_browser_rendering_metrics()
    
    # Check metric types and basic validation
    assert isinstance(metrics, dict), "Metrics should be a dictionary"
    assert 'timestamp' in metrics, "Timestamp should be present"
    assert 'first_contentful_paint' in metrics, "First Contentful Paint metric should be present"
    assert 'time_to_interactive' in metrics, "Time to Interactive metric should be present"
    assert 'total_blocking_time' in metrics, "Total Blocking Time metric should be present"
    assert 'largest_contentful_paint' in metrics, "Largest Contentful Paint metric should be present"
    assert 'cumulative_layout_shift' in metrics, "Cumulative Layout Shift metric should be present"

def test_metrics_values():
    # Test metric value ranges and types
    metrics = log_browser_rendering_metrics()
    
    assert isinstance(metrics['timestamp'], float), "Timestamp should be a float"
    assert metrics['timestamp'] > 0, "Timestamp should be a positive value"
    
    # Check performance metrics are numeric and positive
    numeric_metrics = [
        'first_contentful_paint', 
        'time_to_interactive', 
        'total_blocking_time', 
        'largest_contentful_paint', 
        'cumulative_layout_shift'
    ]
    
    for metric in numeric_metrics:
        assert isinstance(metrics[metric], (int, float)), f"{metric} should be numeric"
        assert metrics[metric] >= 0, f"{metric} should be non-negative"

def test_logging_behavior(caplog):
    # Test logging behavior
    caplog.set_level(logging.INFO)
    log_browser_rendering_metrics()
    
    # Check that a log message was recorded
    assert len(caplog.records) > 0, "A log message should be generated"
    assert "Browser Performance Metrics" in caplog.text, "Log message should contain performance metrics"