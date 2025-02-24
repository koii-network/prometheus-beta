import logging
from typing import Any

def log_multiple(level: str = 'info', *values: Any, separator: str = ' ') -> None:
    """
    Log multiple values in a single statement with flexible configuration.

    Args:
        level (str, optional): Logging level. Defaults to 'info'.
            Supports 'debug', 'info', 'warning', 'error', 'critical'.
        *values (Any): Variable number of values to log.
        separator (str, optional): Separator between logged values. Defaults to ' '.

    Raises:
        ValueError: If an invalid logging level is provided.
    """
    # Configure logging if not already configured
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    logger = logging.getLogger(__name__)

    # Validate logging level
    level = level.lower()
    log_levels = {
        'debug': logger.debug,
        'info': logger.info,
        'warning': logger.warning,
        'error': logger.error,
        'critical': logger.critical
    }

    if level not in log_levels:
        raise ValueError(f"Invalid logging level: {level}. Choose from {', '.join(log_levels.keys())}")

    # Convert values to strings and join
    log_message = separator.join(str(value) for value in values)

    # Log the message at the specified level
    log_levels[level](log_message)