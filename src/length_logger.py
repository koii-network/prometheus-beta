import logging

def log_length(item):
    """
    Log the length of a given string or array/list.
    
    Args:
        item (str or list or tuple): The item to measure length of
    
    Returns:
        int: The length of the item
    
    Raises:
        TypeError: If the input is not a string, list, or tuple
    """
    # Check if the input is a string, list, or tuple
    if not isinstance(item, (str, list, tuple)):
        raise TypeError("Input must be a string, list, or tuple")
    
    # Get the length of the item
    length = len(item)
    
    # Log the length
    logging.info(f"Length of item: {length}")
    
    return length