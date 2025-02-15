import logging

def log_object_details(obj):
    """
    Log the keys and values of an object.
    
    Args:
        obj (dict): The object/dictionary to log.
    
    Raises:
        TypeError: If the input is not a dictionary.
    """
    # Check if input is a dictionary
    if not isinstance(obj, dict):
        raise TypeError("Input must be a dictionary")
    
    # Configure logging if not already configured
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s: %(message)s')
    
    # Log the total number of keys
    logging.info(f"Total number of keys: {len(obj)}")
    
    # Log each key-value pair
    for key, value in obj.items():
        logging.info(f"Key: {key}, Value: {value}")