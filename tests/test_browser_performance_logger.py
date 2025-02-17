import pytest
import json
from src.browser_performance_logger import log_browser_rendering_metrics

def test_log_browser_rendering_metrics():
    # Test that the function returns a dictionary
    metrics = log_browser_rendering_metrics()
    assert isinstance(metrics, dict)
    
    # Test that the metrics dictionary has the expected keys
    expected_keys = [
        'first_contentful_paint',
        'largest_contentful_paint', 
        'total_blocking_time',
        'cumulative_layout_shift',
        'time_to_interactive'
    ]
    for key in expected_keys:
        assert key in metrics
    
    # Test numeric metrics are non-negative
    numeric_metrics = [
        'first_contentful_paint',
        'largest_contentful_paint', 
        'total_blocking_time',
        'cumulative_layout_shift',
        'time_to_interactive'
    ]
    for metric in numeric_metrics:
        assert metrics[metric] is None or metrics[metric] >= 0
    
    # Test error handling (this would require mocking in a real-world scenario)
    # For now, just ensure the function doesn't raise unhandled exceptions
    try:
        log_browser_rendering_metrics()
    except Exception as e:
        pytest.fail(f"Function raised an unexpected exception: {e}")