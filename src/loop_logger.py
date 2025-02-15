import logging

def log_loop_variables(iterable, log_level=logging.INFO):
    """
    Log variable values for each iteration of a loop.
    
    Args:
        iterable (iterable): The iterable to loop through
        log_level (int, optional): Logging level. Defaults to logging.INFO.
    
    Returns:
        list: A list of logged values
    """
    # Configure logging if not already configured
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s: %(message)s')
    
    # List to store logged values
    logged_values = []
    
    # Iterate through the iterable
    for index, value in enumerate(iterable):
        # Log the index and value
        logging.log(log_level, f"Loop iteration {index}: value = {value}")
        
        # Store the value for potential return or further processing
        logged_values.append(value)
    
    return logged_values