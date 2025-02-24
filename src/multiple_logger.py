import logging
import typing

def log_multiple_values(log_level: int, *values: typing.Any, logger: logging.Logger = None) -> None:
    """
    Log multiple values in a single statement with flexible logging options.

    Args:
        log_level (int): The logging level (e.g., logging.INFO, logging.DEBUG)
        *values (Any): Variable number of values to log
        logger (logging.Logger, optional): Custom logger. If None, uses root logger.

    Examples:
        >>> log_multiple_values(logging.INFO, "User", "John", "logged in", age=30)
        # Logs: User John logged in {'age': 30}

        >>> custom_logger = logging.getLogger('my_logger')
        >>> log_multiple_values(logging.DEBUG, "Processing", "data", count=5, logger=custom_logger)
        # Logs to custom_logger: Processing data {'count': 5}
    """
    # Use root logger if no custom logger is provided
    target_logger = logger or logging.getLogger()

    # Separate positional and keyword arguments
    str_values = [str(v) for v in values[:-1]] if isinstance(values[-1], dict) else [str(v) for v in values]
    kwargs = values[-1] if isinstance(values[-1], dict) else {}

    # Prepare the log message
    message = " ".join(str_values)
    if kwargs:
        message += f" {str(kwargs)}"

    # Log the message at the specified log level
    target_logger.log(log_level, message)