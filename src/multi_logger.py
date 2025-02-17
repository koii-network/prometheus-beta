import logging

def log_multiple_values(*values, level=logging.INFO, logger=None):
    """
    Log multiple values in a single statement with flexible logging options.
    
    Args:
        *values: Variable number of values to log
        level (int, optional): Logging level. Defaults to logging.INFO.
        logger (logging.Logger, optional): Custom logger. Defaults to root logger.
    
    Returns:
        None
    """
    # Use root logger if no custom logger is provided
    if logger is None:
        logger = logging.getLogger()
    
    # Convert all values to strings and join them
    log_message = " ".join(str(value) for value in values)
    
    # Log the message at the specified level
    logger.log(level, log_message)