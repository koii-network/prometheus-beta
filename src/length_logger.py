import logging

def log_length(item):
    """
    Log the length of a string or array/list.
    
    Args:
        item (str or list): The input to measure length of
    
    Returns:
        int: The length of the input
    
    Raises:
        TypeError: If the input is not a string or list/array
    """
    if not isinstance(item, (str, list)):
        raise TypeError("Input must be a string or list/array")
    
    length = len(item)
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info(f"Length of input: {length}")
    
    return length