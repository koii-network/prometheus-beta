import json
import logging

def log_json(logger, json_obj, log_level='info', message=None):
    """
    Log a JSON object with proper formatting and optional custom message.

    Args:
        logger (logging.Logger): The logger to use for logging
        json_obj (dict): The JSON object to log
        log_level (str, optional): Logging level. Defaults to 'info'.
            Supports 'debug', 'info', 'warning', 'error', 'critical'
        message (str, optional): Custom message to prepend to the JSON log. 
            Defaults to None.

    Raises:
        TypeError: If json_obj is not a dictionary
        ValueError: If an invalid log level is provided
    """
    # Validate input
    if not isinstance(json_obj, dict):
        raise TypeError("Input must be a dictionary")

    # Validate log level
    log_levels = {
        'debug': logger.debug,
        'info': logger.info,
        'warning': logger.warning,
        'error': logger.error,
        'critical': logger.critical
    }

    if log_level.lower() not in log_levels:
        raise ValueError(f"Invalid log level. Must be one of {list(log_levels.keys())}")

    # Format JSON with indentation
    formatted_json = json.dumps(json_obj, indent=2)

    # Prepare log message
    log_message = formatted_json if message is None else f"{message}\n{formatted_json}"

    # Log using the specified log level
    log_levels[log_level.lower()](log_message)