def longest_common_prefix(strings):
    """
    Find the longest common prefix among a list of strings.
    
    Args:
        strings (list): A list of strings to find the common prefix for.
    
    Returns:
        str: The longest common prefix. If no common prefix exists, returns an empty string.
    
    Raises:
        TypeError: If input is not a list.
        ValueError: If list is empty.
    """
    # Check for valid input
    if not isinstance(strings, list):
        raise TypeError("Input must be a list of strings")
    
    if len(strings) == 0:
        raise ValueError("Input list cannot be empty")
    
    # Handle case with single string
    if len(strings) == 1:
        return strings[0]
    
    # Find the shortest string to limit prefix checking
    shortest = min(strings, key=len)
    
    # Check prefix character by character
    for i in range(len(shortest)):
        # If any string doesn't match the current prefix, return prefix up to this point
        if any(string[i] != shortest[i] for string in strings):
            return shortest[:i]
    
    # Return the shortest string if all characters match
    return shortest