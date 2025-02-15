import logging

def log_multiple(*args, level='info', logger=None):
    """
    Log multiple values in a single statement with flexible logging options.
    
    Args:
        *args: Variable number of arguments to log
        level (str, optional): Logging level. Defaults to 'info'.
            Can be 'debug', 'info', 'warning', 'error', or 'critical'.
        logger (logging.Logger, optional): Custom logger. 
            If not provided, uses the root logger.
    
    Returns:
        None
    
    Raises:
        ValueError: If an invalid logging level is provided
    """
    # Use root logger if no logger is specified
    if logger is None:
        logger = logging.getLogger()
    
    # Convert arguments to strings and join them
    log_message = " ".join(str(arg) for arg in args)
    
    # Select logging method based on level
    log_levels = {
        'debug': logger.debug,
        'info': logger.info,
        'warning': logger.warning,
        'error': logger.error,
        'critical': logger.critical
    }
    
    # Validate and execute logging
    if level.lower() not in log_levels:
        raise ValueError(f"Invalid logging level: {level}. "
                         f"Must be one of {list(log_levels.keys())}")
    
    log_levels[level.lower()](log_message)