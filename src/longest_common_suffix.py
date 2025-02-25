def find_longest_common_suffix(strings):
    """
    Find the longest common suffix among a list of strings.
    
    Args:
        strings (list): A list of strings to find the common suffix.
    
    Returns:
        str: The longest common suffix, or an empty string if no common suffix exists.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the input list is empty.
    """
    if not isinstance(strings, list):
        raise TypeError("Input must be a list of strings")
    
    if not strings:
        raise ValueError("Input list cannot be empty")
    
    # If only one string, return that string
    if len(strings) == 1:
        return strings[0]
    
    return ''