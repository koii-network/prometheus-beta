import logging

def log_multiple(level='info', *values, logger=None):
    """
    Log multiple values in a single statement with flexible logging options.
    
    :param level: Logging level (default: 'info')
    :param values: Multiple values to log
    :param logger: Optional custom logger (defaults to root logger)
    """
    # If no custom logger is provided, use the root logger
    if logger is None:
        logger = logging.getLogger()
    
    # Convert values to strings and join them
    log_message = ' '.join(str(value) for value in values)
    
    # Map string level to appropriate logging method
    log_levels = {
        'debug': logger.debug,
        'info': logger.info,
        'warning': logger.warning,
        'error': logger.error,
        'critical': logger.critical
    }
    
    # Get the appropriate logging method, default to info if invalid level
    log_method = log_levels.get(level.lower(), logger.info)
    
    # Log the message
    log_method(log_message)