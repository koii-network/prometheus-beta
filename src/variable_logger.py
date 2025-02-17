import logging
import sys

def log_variable_values(iterable, log_level=logging.INFO, logger=None):
    """
    Log variable values during iteration.
    
    Args:
        iterable (iterable): The iterable to loop through and log.
        log_level (int, optional): Logging level. Defaults to logging.INFO.
        logger (logging.Logger, optional): Logger to use. Creates a new one if not provided.
    
    Returns:
        list: A list of logged values.
    
    Raises:
        TypeError: If the input is not iterable.
    """
    # Create logger if not provided
    if logger is None:
        logger = logging.getLogger(__name__)
        # Add a handler to sys.stderr if no handlers exist
        if not logger.handlers:
            handler = logging.StreamHandler(sys.stderr)
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.setLevel(logging.INFO)
    
    # Validate input is iterable
    try:
        iterator = iter(iterable)
    except TypeError:
        raise TypeError("Input must be an iterable")
    
    # Store logged values
    logged_values = []
    
    # Iterate and log
    for index, value in enumerate(iterable):
        log_message = f"Iteration {index}: Value = {value}"
        logger.log(log_level, log_message)
        logged_values.append(value)
    
    return logged_values