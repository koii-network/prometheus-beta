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

    # Define log message format and write method
    def write_log_message(msg: str, is_error: bool = True):
        """Write log message to the specified stream."""
        if is_error:
            prefix = f"ERROR: "
        else:
            prefix = f"{log_level}: "
        
        # Write formatted message to the stream
        print(f"{prefix}{msg}", file=log_stream, flush=True)

    # Log the primary message
    write_log_message(message)

    # If an exception is provided, log its details
    if error is not None:
        write_log_message(f"Exception Type: {type(error).__name__}", is_error=False)
        write_log_message(f"Exception Details: {str(error)}", is_error=False)