def find_longest_common_suffix(strings):
    """
    Find the longest common suffix among a list of strings.
    
    Args:
        strings (list): A list of strings to compare
    
    Returns:
        str: The longest common suffix, or an empty string if no common suffix exists
    
    Raises:
        TypeError: If the input is not a list or contains non-string elements
    """
    # Validate input 
    if not isinstance(strings, list):
        raise TypeError("Input must be a list of strings")
    
    # Handle empty list or list with no strings
    if not strings or len(strings) == 0:
        return ""
    
    # Validate all elements are strings
    if not all(isinstance(s, str) for s in strings):
        raise TypeError("All elements must be strings")
    
    # Handle single string case
    if len(strings) == 1:
        return strings[0]
    
    # Find the shortest string in the list
    shortest = min(strings, key=len)
    
    # Iterate through possible suffixes from longest to shortest
    for length in range(len(shortest), 0, -1):
        potential_suffix = shortest[-length:]
        if all(s.endswith(potential_suffix) for s in strings):
            return potential_suffix
    
    return ""