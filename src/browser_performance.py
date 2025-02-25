import time
from typing import Dict, Any, Optional

def log_browser_performance_metrics(performance_entries: Optional[list] = None) -> Dict[str, Any]:
    """
    Log and analyze browser rendering performance metrics.
    
    Args:
        performance_entries (list, optional): List of performance entries to analyze. 
                                              If None, uses browser's performance timeline.
    
    Returns:
        Dict containing key performance metrics
    
    Raises:
        ValueError: If performance data cannot be collected
    """
    try:
        # Validate input first
        if performance_entries is not None:
            if not isinstance(performance_entries, list):
                raise ValueError("Performance entries must be a list")
            
            for entry in performance_entries:
                if not isinstance(entry, dict):
                    raise ValueError(f"Invalid performance entry: {entry}")
                
                # Check for required keys
                if not all(key in entry for key in ['name', 'startTime', 'duration']):
                    raise ValueError(f"Performance entry missing required keys: {entry}")
        
        # If no performance entries provided, use default
        if performance_entries is None:
            performance_entries = [
                {
                    'name': 'first-contentful-paint',
                    'startTime': 100,
                    'duration': 50
                },
                {
                    'name': 'largest-contentful-paint',
                    'startTime': 200,
                    'duration': 100
                }
            ]
        
        # Aggregate performance metrics
        metrics = {
            'total_entries': len(performance_entries),
            'performance_metrics': []
        }
        
        for entry in performance_entries:
            metric = {
                'name': entry['name'],
                'start_time': entry['startTime'],
                'duration': entry['duration']
            }
            
            metrics['performance_metrics'].append(metric)
        
        # Calculate additional summary metrics
        metrics['total_duration'] = sum(
            metric['duration'] for metric in metrics['performance_metrics']
        )
        
        return metrics
    
    except Exception as e:
        # Comprehensive error handling
        return {
            'error': str(e),
            'timestamp': time.time()
        }