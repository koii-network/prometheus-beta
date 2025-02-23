import pytest
import time
import logging
from src.performance_logger import log_browser_rendering_metrics

def test_log_browser_rendering_metrics_default():
    """Test logging performance metrics with default behavior."""
    metrics = log_browser_rendering_metrics()
    
    # Check basic structure
    assert isinstance(metrics, dict)
    assert 'timestamp' in metrics
    assert isinstance(metrics['timestamp'], float)
    
    # Check default metrics are initialized
    assert 'total_time' in metrics
    assert 'first_contentful_paint' in metrics
    assert 'dom_load_time' in metrics
    assert 'page_load_time' in metrics

def test_log_browser_rendering_metrics_with_custom_metrics():
    """Test logging performance metrics with custom input."""
    custom_metrics = {
        'total_time': 100,
        'first_contentful_paint': 50,
        'custom_metric': 'test'
    }
    
    metrics = log_browser_rendering_metrics(custom_metrics)
    
    # Verify original metrics are preserved
    assert metrics['total_time'] == 100
    assert metrics['first_contentful_paint'] == 50
    assert metrics['custom_metric'] == 'test'
    assert 'timestamp' in metrics

def test_log_browser_rendering_metrics_invalid_input():
    """Test error handling for invalid input."""
    with pytest.raises(ValueError, match="Metrics must be a dictionary"):
        log_browser_rendering_metrics("invalid input")

def test_log_browser_rendering_metrics_timestamp():
    """Test timestamp generation."""
    current_time = time.time()
    metrics = log_browser_rendering_metrics()
    
    # Check timestamp is recent
    assert abs(metrics['timestamp'] - current_time) < 1, "Timestamp should be close to current time"

def test_log_browser_rendering_metrics_overwrite():
    """Test that custom metrics can overwrite default metrics."""
    custom_metrics = {
        'total_time': 200,
        'custom_key': 'custom_value'
    }
    
    metrics = log_browser_rendering_metrics(custom_metrics)
    
    assert metrics['total_time'] == 200
    assert metrics['custom_key'] == 'custom_value'