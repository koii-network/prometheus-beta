def log_variable_type(variable, logger=None):
    """
    Log the type of a given variable.
    
    Args:
        variable: Any Python variable to log the type of
        logger: Optional logger to use. If None, uses the root logger.
    
    Returns:
        str: The type of the variable as a string
    """
    import logging
    
    # Get the type of the variable
    var_type = type(variable).__name__
    
    # Use provided logger or get root logger
    if logger is None:
        logger = logging.getLogger()
    
    # Log the type of the variable
    logger.info(f"{var_type} - {repr(variable)}")
    
    return var_type