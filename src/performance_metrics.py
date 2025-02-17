import json
import time
import os
from typing import Dict, Any

def log_browser_rendering_metrics() -> Dict[str, Any]:
    """
    Collect and log browser rendering performance metrics.
    
    Returns:
        Dict containing various performance metrics.
    
    Raises:
        Exception if logging fails
    """
    # Ensure log directory exists
    os.makedirs('logs', exist_ok=True)
    
    try:
        # Simulate collecting performance metrics
        performance_metrics = {
            'timestamp': time.time(),
            'total_render_time': 0.0,
            'first_contentful_paint': 0.0,
            'time_to_interactive': 0.0,
            'dom_content_loaded': 0.0,
            'memory_usage': 0.0,
            'cpu_usage': 0.0
        }
        
        # Open log file with explicit mode to force potential permission error
        with open('logs/performance_log.json', 'a', opener=lambda path, flags: os.open(path, flags, 0o666)) as log_file:
            log_file.write(json.dumps(performance_metrics) + '\n')
        
        return performance_metrics
    
    except Exception as e:
        # Log the error details
        error_metrics = {
            'error': str(e),
            'timestamp': time.time()
        }
        
        try:
            with open('logs/performance_error_log.json', 'a') as error_log:
                error_log.write(json.dumps(error_metrics) + '\n')
        except Exception:
            # Fallback error logging (optional)
            print(f"Failed to log error: {error_metrics}")
        
        # Re-raise the original exception
        raise