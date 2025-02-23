import traceback
import logging
import sys
from typing import Optional, Union, TextIO


def log_stack_trace(
    exception: Optional[Union[Exception, BaseException]] = None, 
    log_level: int = logging.ERROR, 
    logger: Optional[logging.Logger] = None, 
    output_stream: Optional[TextIO] = None
) -> str:
    """
    Log stack trace for an exception or the current exception.

    Args:
        exception (Optional[Exception]): The exception to log. If None, uses the current exception.
        log_level (int): Logging level. Defaults to logging.ERROR.
        logger (Optional[logging.Logger]): Logger to use. If None, uses root logger.
        output_stream (Optional[TextIO]): Optional stream to write stack trace. If None, uses default logging.

    Returns:
        str: The formatted stack trace string.

    Raises:
        ValueError: If no exception is found to trace.
    """
    # Determine the stack trace
    if exception is None:
        # Get current exception if no exception is provided
        exc_info = sys.exc_info()
        if exc_info[0] is None:
            raise ValueError("No exception found to trace.")
        exception = exc_info[1]

    # Convert to string representation
    stack_trace = ''.join(traceback.format_exception(
        type(exception), 
        exception, 
        exception.__traceback__
    ))

    # Determine logging method
    if logger is not None:
        # Log using provided logger
        logger.log(log_level, stack_trace)
    elif output_stream is not None:
        # Write to output stream if provided
        output_stream.write(stack_trace)
    else:
        # Default to root logger
        logging.log(log_level, stack_trace)

    return stack_trace