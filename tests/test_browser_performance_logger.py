import pytest
import json
import os
import time
from src.browser_performance_logger import log_browser_rendering_metrics, save_performance_log

def test_log_browser_rendering_metrics_valid_entries():
    performance_entries = [
        {'entryType': 'paint', 'name': 'first-contentful-paint', 'startTime': 100},
        {'entryType': 'largest-contentful-paint', 'startTime': 500},
        {'entryType': 'long-tasks', 'duration': 200},
        {'entryType': 'layout-shift', 'value': 0.1}
    ]
    
    metrics = log_browser_rendering_metrics(performance_entries)
    
    assert metrics['total_entries'] == 4
    assert metrics['rendering_metrics']['first_contentful_paint'] == 100
    assert metrics['rendering_metrics']['largest_contentful_paint'] == 500
    assert metrics['rendering_metrics']['total_blocking_time'] == 200
    assert metrics['rendering_metrics']['cumulative_layout_shift'] == 0.1
    assert 'timestamp' in metrics

def test_log_browser_rendering_metrics_empty_entries():
    with pytest.raises(ValueError, match="No performance entries provided"):
        log_browser_rendering_metrics([])

def test_save_performance_log(tmp_path):
    log_file = os.path.join(tmp_path, 'performance_test_log.json')
    metrics = {
        'rendering_metrics': {
            'first_contentful_paint': 100,
            'largest_contentful_paint': 500
        },
        'timestamp': time.time()
    }
    
    save_performance_log(metrics, log_file)
    
    assert os.path.exists(log_file)
    with open(log_file, 'r') as f:
        saved_metrics = json.loads(f.readline())
        assert saved_metrics['rendering_metrics']['first_contentful_paint'] == 100