import logging

def log_multiple(log_level, *args, logger=None):
    """
    Log multiple values in a single statement with a specified log level.
    
    :param log_level: The logging level (e.g., logging.INFO, logging.ERROR)
    :param args: Variable number of arguments to log
    :param logger: Optional custom logger. If not provided, uses the root logger.
    """
    # Use the provided logger or the root logger
    log = logger or logging.getLogger()
    
    # Convert all arguments to strings and join them
    log_message = ' '.join(str(arg) for arg in args)
    
    # Log the message at the specified level
    if log_level == logging.DEBUG:
        log.debug(log_message)
    elif log_level == logging.INFO:
        log.info(log_message)
    elif log_level == logging.WARNING:
        log.warning(log_message)
    elif log_level == logging.ERROR:
        log.error(log_message)
    elif log_level == logging.CRITICAL:
        log.critical(log_message)
    else:
        raise ValueError(f"Invalid log level: {log_level}")