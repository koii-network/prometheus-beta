def find_longest_common_suffix(strings):
    """
    Find the longest common suffix among a list of strings.
    
    Args:
        strings (list): A list of strings to find the common suffix
    
    Returns:
        str: The longest common suffix, or an empty string if no common suffix exists
    
    Raises:
        TypeError: If input is not a list
        ValueError: If input list is empty
    """
    # Validate input
    if not isinstance(strings, list):
        raise TypeError("Input must be a list of strings")
    
    if not strings:
        raise ValueError("Input list cannot be empty")
    
    # Check if all elements are strings
    if not all(isinstance(s, str) for s in strings):
        raise TypeError("All elements must be strings")
    
    # If only one string, return that string
    if len(strings) == 1:
        return strings[0]
    
    # Find the shortest string to limit suffix checking
    shortest = min(strings, key=len)
    
    # Check all possible suffixes of the shortest string
    for i in range(len(shortest), 0, -1):
        suffix = shortest[-i:]
        if all(s.endswith(suffix) for s in strings):
            return suffix
    
    # If no common suffix found
    return ""