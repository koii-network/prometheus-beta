import json
import time
from typing import Dict, Any

def log_browser_rendering_metrics(performance_entries: list) -> Dict[str, Any]:
    """
    Log and analyze browser rendering performance metrics.
    
    Args:
        performance_entries (list): A list of performance entry dictionaries.
        
    Returns:
        Dict[str, Any]: A summary of performance metrics.
    """
    if not performance_entries:
        raise ValueError("No performance entries provided")
    
    metrics = {
        "total_entries": len(performance_entries),
        "rendering_metrics": {
            "first_contentful_paint": None,
            "largest_contentful_paint": None,
            "total_blocking_time": 0,
            "cumulative_layout_shift": 0
        },
        "timestamp": time.time()
    }
    
    for entry in performance_entries:
        entry_type = entry.get('entryType')
        
        if entry_type == 'paint' and entry.get('name') == 'first-contentful-paint':
            metrics['rendering_metrics']['first_contentful_paint'] = entry.get('startTime', 0)
        
        if entry_type == 'largest-contentful-paint':
            metrics['rendering_metrics']['largest_contentful_paint'] = entry.get('startTime', 0)
        
        if entry_type == 'long-tasks':
            metrics['rendering_metrics']['total_blocking_time'] += entry.get('duration', 0)
        
        if entry_type == 'layout-shift':
            metrics['rendering_metrics']['cumulative_layout_shift'] += entry.get('value', 0)
    
    return metrics

def save_performance_log(metrics: Dict[str, Any], log_file: str = 'performance_log.json') -> None:
    """
    Save performance metrics to a JSON log file.
    
    Args:
        metrics (Dict[str, Any]): Performance metrics to save.
        log_file (str, optional): Path to the log file. Defaults to 'performance_log.json'.
    """
    try:
        with open(log_file, 'a') as f:
            json.dump(metrics, f)
            f.write('\n')
    except IOError as e:
        print(f"Error writing performance log: {e}")