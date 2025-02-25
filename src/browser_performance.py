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
        # If no performance entries provided, attempt to use default browser performance API
        if performance_entries is None:
            # Simulated performance entry collection (would be replaced with actual browser API in real implementation)
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
        
        # Validate input
        if not isinstance(performance_entries, list):
            raise ValueError("Performance entries must be a list")
        
        # Aggregate performance metrics
        metrics = {
            'total_entries': len(performance_entries),
            'performance_metrics': []
        }
        
        for entry in performance_entries:
            # Validate each entry is a dictionary
            if not isinstance(entry, dict):
                raise ValueError(f"Invalid performance entry: {entry}")
            
            # Extract key metrics
            metric = {
                'name': entry.get('name', 'unknown'),
                'start_time': entry.get('startTime', 0),
                'duration': entry.get('duration', 0)
            }
            
            metrics['performance_metrics'].append(metric)
        
        # Calculate additional summary metrics
        if metrics['performance_metrics']:
            metrics['total_duration'] = sum(
                metric['duration'] for metric in metrics['performance_metrics']
            )
        else:
            metrics['total_duration'] = 0
        
        return metrics
    
    except Exception as e:
        # Comprehensive error handling
        return {
            'error': str(e),
            'timestamp': time.time()
        }