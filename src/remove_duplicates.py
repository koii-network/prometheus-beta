def remove_duplicate_chars(input_string):
    """
    Remove duplicate characters from a string while preserving the original order.
    
    Args:
        input_string (str): The input string to remove duplicates from.
    
    Returns:
        str: A string with duplicate characters removed, keeping first occurrence.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Check input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Use OrderedDict to preserve order of first occurrence
    from collections import OrderedDict
    
    return ''.join(OrderedDict.fromkeys(input_string))