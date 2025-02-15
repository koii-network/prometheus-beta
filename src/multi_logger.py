import logging

def log_multiple(logger, level, *values, separator=' ', **kwargs):
    """
    Log multiple values in a single statement with flexible configuration.
    
    Args:
        logger (logging.Logger): The logger instance to use.
        level (str): Logging level ('debug', 'info', 'warning', 'error', 'critical').
        *values: Variable number of values to log.
        separator (str, optional): Separator between logged values. Defaults to space.
        **kwargs: Additional keyword arguments to pass to the logging method.
    
    Raises:
        ValueError: If an invalid logging level is provided.
    """
    # Map log levels to logger methods
    log_methods = {
        'debug': logger.debug,
        'info': logger.info,
        'warning': logger.warning,
        'error': logger.error,
        'critical': logger.critical
    }
    
    # Validate log level
    if level.lower() not in log_methods:
        raise ValueError(f"Invalid log level: {level}. Must be one of {list(log_methods.keys())}")
    
    # Convert all values to strings and join
    message = separator.join(str(value) for value in values)
    
    # Call the appropriate logging method
    log_methods[level.lower()](message, **kwargs)