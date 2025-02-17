import json
import logging

def log_object(obj, log_level='info', logger=None):
    """
    Log an object in a readable JSON format.
    
    Args:
        obj (Any): The object to be logged
        log_level (str, optional): Logging level. Defaults to 'info'.
                                   Options are 'debug', 'info', 'warning', 'error', 'critical'
        logger (logging.Logger, optional): Custom logger. If None, uses root logger.
    
    Raises:
        ValueError: If an invalid log level is provided
        TypeError: If obj cannot be serialized to JSON
    """
    # Set up logger
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
        raise ValueError(f"Invalid log level: {log_level}. Choose from {list(log_levels.keys())}")
    
    # Try to convert object to JSON
    try:
        # Use indent for readability, sort_keys for consistent output
        formatted_obj = json.dumps(obj, indent=2, sort_keys=True, default=str)
    except TypeError:
        # If direct JSON conversion fails, use str() directly
        formatted_obj = str(obj)
    
    # Log the object using the specified log level
    log_method = log_levels[log_level.lower()]
    log_method(f"Logged Object:\n{formatted_obj}")
    
    return formatted_obj if isinstance(formatted_obj, str) else json.dumps(formatted_obj)