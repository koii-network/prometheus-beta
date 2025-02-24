import logging

def log_object_details(obj):
    """
    Log the keys and values of a given object.

    Args:
        obj (dict): The object/dictionary to log.

    Raises:
        TypeError: If the input is not a dictionary.
        ValueError: If the input dictionary is empty.

    Returns:
        None: Logs the object details but does not return anything.
    """
    # Validate input is a dictionary
    if not isinstance(obj, dict):
        raise TypeError("Input must be a dictionary")
    
    # Check if dictionary is empty
    if not obj:
        raise ValueError("Input dictionary cannot be empty")
    
    # Create a logger
    logger = logging.getLogger(__name__)
    
    # Log the number of items
    logger.info(f"Object contains {len(obj)} key-value pair(s)")
    
    # Log each key-value pair
    for key, value in obj.items():
        logger.info(f"Key: {key}, Value: {value}")