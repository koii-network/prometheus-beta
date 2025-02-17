import logging

def log_object_details(obj, logger=None):
    """
    Log the keys and values of an object.
    
    Args:
        obj (dict or object): The object to log details for
        logger (logging.Logger, optional): A custom logger. 
                                           If not provided, uses root logger.
    
    Raises:
        TypeError: If the input is not a dictionary or an object with __dict__
    """
    # Use provided logger or root logger
    log = logger or logging.getLogger()
    
    # Handle different input types
    if isinstance(obj, dict):
        items = obj
    elif hasattr(obj, '__dict__'):
        items = obj.__dict__
    else:
        raise TypeError("Input must be a dictionary or an object with __dict__")
    
    # Log object type
    log.info(f"Logging details for {type(obj).__name__}")
    
    # Log each key-value pair
    for key, value in items.items():
        log.info(f"{key}: {value}")
    
    return len(items)  # Return number of items logged