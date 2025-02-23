import logging

def log_length(item):
    """
    Log the length of a string or array.
    
    Args:
        item (str or list): The item to log the length of
    
    Returns:
        int: The length of the item
    
    Raises:
        TypeError: If the input is not a string or list
    """
    # Validate input type
    if not isinstance(item, (str, list)):
        raise TypeError("Input must be a string or list")
    
    # Get the length
    length = len(item)
    
    # Log the length
    logging.info(f"Length of item: {length}")
    
    return length