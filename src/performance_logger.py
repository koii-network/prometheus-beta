import time
import json
import logging
from typing import Dict, Any, Optional

def log_browser_rendering_metrics(metrics: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Log browser rendering performance metrics.

    This function captures and logs key performance metrics related to browser rendering.
    If no metrics are provided, it will attempt to generate standard performance metrics.

    Args:
        metrics (Optional[Dict[str, Any]], optional): Pre-existing performance metrics dictionary. 
        Defaults to None.

    Returns:
        Dict[str, Any]: A dictionary containing performance metrics.

    Raises:
        ValueError: If the metrics are invalid or cannot be processed.
    """
    # Initialize logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # If no metrics are provided, create a default metrics dictionary
    if metrics is None:
        metrics = {}

    # Validate metrics input
    if not isinstance(metrics, dict):
        raise ValueError("Metrics must be a dictionary")

    # Add timestamp to metrics
    metrics['timestamp'] = time.time()

    # Add common performance-related keys if not already present
    default_metrics = {
        'total_time': metrics.get('total_time', 0),
        'first_contentful_paint': metrics.get('first_contentful_paint', 0),
        'dom_load_time': metrics.get('dom_load_time', 0),
        'page_load_time': metrics.get('page_load_time', 0)
    }
    metrics.update({k: v for k, v in default_metrics.items() if k not in metrics})

    # Log the metrics
    try:
        logger.info(f"Browser Rendering Metrics: {json.dumps(metrics)}")
    except Exception as e:
        logger.error(f"Error logging metrics: {e}")
        raise ValueError(f"Could not log metrics: {e}")

    return metrics