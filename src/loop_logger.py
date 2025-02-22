import logging

def log_variables_in_loop(iterable, log_level=logging.INFO):
    """
    Log the values of variables inside a loop.
    
    Args:
        iterable (iterable): The iterable to loop through
        log_level (int, optional): Logging level. Defaults to logging.INFO.
    
    Returns:
        list: A list of logged values
    """
    # Configure basic logging if not already configured
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s')
    
    # List to store logged values
    logged_values = []
    
    # Loop through the iterable and log each value
    for index, value in enumerate(iterable):
        log_message = f"Loop iteration {index}: Value = {value}"
        
        # Log based on the specified log level
        if log_level == logging.DEBUG:
            logging.debug(log_message)
        elif log_level == logging.INFO:
            logging.info(log_message)
        elif log_level == logging.WARNING:
            logging.warning(log_message)
        elif log_level == logging.ERROR:
            logging.error(log_message)
        elif log_level == logging.CRITICAL:
            logging.critical(log_message)
        else:
            logging.info(log_message)  # Default to INFO
        
        logged_values.append(value)
    
    return logged_values