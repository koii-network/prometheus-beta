def find_longest_common_suffix(strings):
    """
    Find the longest common suffix among a list of strings.
    
    Args:
        strings (list): A list of strings to compare
    
    Returns:
        str: The longest common suffix, or an empty string if no common suffix exists
    
    Raises:
        TypeError: If input is not a list
        ValueError: If the list is empty
    """
    # Validate input
    if not isinstance(strings, list):
        raise TypeError("Input must be a list of strings")
    
    if not strings:
        raise ValueError("Input list cannot be empty")
    
    # Validate all elements are strings
    if not all(isinstance(s, str) for s in strings):
        raise TypeError("All elements must be strings")
    
    # Handle single string case
    if len(strings) == 1:
        return strings[0]
    
    # Find the shortest string to optimize comparison
    shortest = min(strings, key=len)
    
    # Check from the end of the shortest string
    for i in range(1, len(shortest) + 1):
        suffix = shortest[-i:]
        if all(s.endswith(suffix) for s in strings):
            common_suffix = suffix
        else:
            break
    
    return common_suffix if 'common_suffix' in locals() else ''