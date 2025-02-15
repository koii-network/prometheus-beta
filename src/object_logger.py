import json
import pprint
import logging

def log_object(obj, log_level='info', logger=None):
    """
    Log an object in a readable, formatted manner.
    
    Args:
        obj: The object to be logged
        log_level (str, optional): Logging level. Defaults to 'info'.
            Options: 'debug', 'info', 'warning', 'error', 'critical'
        logger (logging.Logger, optional): Custom logger. 
            If not provided, uses the root logger.
    
    Returns:
        str: Formatted string representation of the object
    """
    # If no logger is provided, use the root logger
    if logger is None:
        logger = logging.getLogger()
    
    # Validate log level
    log_levels = {
        'debug': logger.debug,
        'info': logger.info,
        'warning': logger.warning,
        'error': logger.error,
        'critical': logger.critical
    }
    
    if log_level.lower() not in log_levels:
        raise ValueError(f"Invalid log level: {log_level}. Must be one of {list(log_levels.keys())}")
    
    # Use pprint for better formatting of complex objects
    formatted_obj = pprint.pformat(obj, indent=2, width=120, compact=False)
    
    # Log the object using the specified log level
    log_levels[log_level.lower()](formatted_obj)
    
    return formatted_obj