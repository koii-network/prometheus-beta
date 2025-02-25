import logging

def log_object_details(obj):
    """
    Log the keys and values of an object.
    
    Args:
        obj (dict): The object/dictionary to log.
    
    Raises:
        TypeError: If the input is not a dictionary.
    """
    # Validate input is a dictionary
    if not isinstance(obj, dict):
        raise TypeError("Input must be a dictionary")
    
    # Configure logging if not already configured
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s: %(message)s')
    
    # Log object details
    logging.info("Logging object details:")
    for key, value in obj.items():
        logging.info(f"Key: {key}, Value: {value}")
    
    return len(obj)  # Return number of items for potential additional use