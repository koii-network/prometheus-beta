import logging
from typing import Any

def log_multiple_values(*values: Any, level: str = 'info', logger: logging.Logger = None) -> None:
    """
    Log multiple values in a single statement with flexible logging options.

    Args:
        *values: Variable number of values to log
        level: Logging level (default: 'info')
        logger: Optional custom logger (default: root logger)

    Raises:
        ValueError: If an invalid logging level is provided
        TypeError: If logger is not a valid logging.Logger instance
    """
    # Use root logger if no custom logger is provided
    if logger is None:
        logger = logging.getLogger()

    # Validate logger type
    if not isinstance(logger, logging.Logger):
        raise TypeError("Logger must be a valid logging.Logger instance")

    # Normalize the logging level
    level = level.lower()

    # Map string levels to logging methods
    log_methods = {
        'debug': logger.debug,
        'info': logger.info,
        'warning': logger.warning,
        'error': logger.error,
        'critical': logger.critical
    }

    # Validate logging level
    if level not in log_methods:
        raise ValueError(f"Invalid logging level: {level}. Choose from {list(log_methods.keys())}")

    # Convert all values to strings and join
    log_message = ' '.join(str(value) for value in values)

    # Log the message using the specified method
    log_methods[level](log_message)