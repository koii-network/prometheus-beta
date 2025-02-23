import logging
import sys
from typing import Any, Optional, TextIO

def log_custom_error(message: str, 
                     error: Optional[Exception] = None, 
                     log_level: str = 'ERROR', 
                     log_stream: Optional[TextIO] = sys.stderr) -> None:
    """
    Log a custom error message with optional exception details.

    Args:
        message (str): The custom error message to log.
        error (Optional[Exception], optional): The exception object to log details from. Defaults to None.
        log_level (str, optional): The logging level to use. Defaults to 'ERROR'.
            Supported levels: 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'
        log_stream (Optional[TextIO], optional): Stream to log to. Defaults to sys.stderr.

    Raises:
        ValueError: If an invalid log level is provided.
    """
    # Configure logging to output to specified stream
    logging.basicConfig(
        level=logging.ERROR,
        format='%(levelname)s: %(message)s',
        stream=log_stream
    )

    # Validate log level
    log_levels = {
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'WARNING': logging.WARNING,
        'ERROR': logging.ERROR,
        'CRITICAL': logging.CRITICAL
    }

    if log_level not in log_levels:
        raise ValueError(f"Invalid log level: {log_level}. Must be one of {list(log_levels.keys())}")

    # Get the appropriate logging method based on the log level
    log_method = getattr(logging, log_level.lower())

    # Log the primary message
    log_method(message)

    # If an exception is provided, log its details
    if error is not None:
        log_method(f"Exception Type: {type(error).__name__}")
        log_method(f"Exception Details: {str(error)}")