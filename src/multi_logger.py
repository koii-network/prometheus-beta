import logging
from typing import Any

def log_multiple(level: str, *args: Any, **kwargs) -> None:
    """
    Log multiple values in a single statement with flexible logging levels.

    Args:
        level (str): The logging level ('debug', 'info', 'warning', 'error', 'critical')
        *args: Variable number of positional arguments to log
        **kwargs: Optional keyword arguments to pass to the logging method

    Raises:
        ValueError: If an invalid logging level is provided
    """
    # Configure a default logger if no logger is provided in kwargs
    logger = kwargs.pop('logger', logging.getLogger())

    # Normalize the logging level
    level = level.lower()

    # Map log levels to appropriate logging methods
    log_methods = {
        'debug': logger.debug,
        'info': logger.info,
        'warning': logger.warning,
        'error': logger.error,
        'critical': logger.critical
    }

    # Validate and get the appropriate logging method
    if level not in log_methods:
        raise ValueError(f"Invalid logging level: {level}. Must be one of {list(log_methods.keys())}")

    # Convert all arguments to strings and join them
    log_message = ' '.join(str(arg) for arg in args)

    # Call the appropriate logging method
    log_methods[level](log_message, **kwargs)