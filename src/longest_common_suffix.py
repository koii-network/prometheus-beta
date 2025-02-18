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
    
    # Find the shortest string to limit suffix checking
    shortest_str = min(strings, key=len)
    
    # Check from end of the shortest string
    for i in range(1, len(shortest_str) + 1):
        suffix = shortest_str[-i:]
        if all(string.endswith(suffix) for string in strings):
            common_suffix = suffix
        else:
            break
    
    return common_suffix if 'common_suffix' in locals() else ''