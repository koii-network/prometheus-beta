import logging

def log_loop_variables(iterable, log_level=logging.INFO):
    """
    Log variable values inside a loop with optional logging level.
    
    Args:
        iterable (iterable): The iterable to loop through and log.
        log_level (int, optional): Logging level. Defaults to logging.INFO.
    
    Returns:
        list: A list of logged values.
    """
    # Ensure logging is configured
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Logger to use
    logger = logging.getLogger(__name__)
    
    # List to store logged values
    logged_values = []
    
    # Loop through the iterable and log each value
    for index, value in enumerate(iterable):
        # Log the current index and value
        logger.log(log_level, f"Loop iteration {index}: value = {value}")
        logged_values.append(value)
    
    return logged_values