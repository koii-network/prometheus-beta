import logging

def log_loop_values(iterable, log_level=logging.INFO):
    """
    Log variable values inside a loop with configurable logging level.
    
    Args:
        iterable (iterable): The iterable to loop through and log
        log_level (int, optional): Logging level. Defaults to logging.INFO
    
    Returns:
        list: A list of logged values
    """
    # Configure logging if not already configured
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s')
    
    # List to store logged values
    logged_values = []
    
    # Loop through the iterable and log each value
    for index, value in enumerate(iterable, 1):
        log_message = f"Loop iteration {index}: Value = {value}"
        logging.log(log_level, log_message)
        logged_values.append(value)
    
    return logged_values