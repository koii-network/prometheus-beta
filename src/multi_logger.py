import logging

def log_multiple(level, *values, logger=None):
    """
    Log multiple values in a single statement with a specified logging level.
    
    :param level: Logging level (e.g., logging.INFO, logging.DEBUG)
    :param values: Variable number of values to log
    :param logger: Optional logger object. If not provided, uses root logger
    """
    # Use root logger if no logger is specified
    if logger is None:
        logger = logging.getLogger()
    
    # Convert all values to strings and join them
    message = ' '.join(str(value) for value in values)
    
    # Log the message at the specified level
    if level == logging.DEBUG:
        logger.debug(message)
    elif level == logging.INFO:
        logger.info(message)
    elif level == logging.WARNING:
        logger.warning(message)
    elif level == logging.ERROR:
        logger.error(message)
    elif level == logging.CRITICAL:
        logger.critical(message)
    else:
        raise ValueError(f"Unsupported logging level: {level}")