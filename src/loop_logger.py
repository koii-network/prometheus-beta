import logging

def log_loop_values(iterable, log_level=logging.INFO):
    """
    Log variable values inside a loop with a specified logging level.
    
    Args:
        iterable (iterable): The iterable to loop through and log.
        log_level (int, optional): Logging level. Defaults to logging.INFO.
    
    Returns:
        list: A list of logged values.
    
    Raises:
        TypeError: If the input is not iterable.
    """
    # Configure logging if not already configured
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Validate input
    try:
        iter(iterable)
    except TypeError:
        raise TypeError("Input must be an iterable")
    
    # Store logged values
    logged_values = []
    
    # Loop and log
    for index, value in enumerate(iterable, 1):
        log_message = f"Loop iteration {index}: {value}"
        logging.log(log_level, log_message)
        logged_values.append(value)
    
    return logged_values