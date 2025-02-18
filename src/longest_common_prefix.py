def find_longest_common_prefix(strings):
    """
    Find the longest common prefix among a list of strings.
    
    Args:
        strings (List[str]): A list of strings to find the common prefix for.
    
    Returns:
        str: The longest common prefix. If no common prefix exists, returns an empty string.
    
    Raises:
        TypeError: If input is not a list or contains non-string elements.
    """
    # Check input type
    if not isinstance(strings, list):
        raise TypeError("Input must be a list of strings")
    
    # Handle empty list or list with no strings
    if not strings:
        return ""
    
    # Check that all elements are strings
    if not all(isinstance(s, str) for s in strings):
        raise TypeError("All elements must be strings")
    
    # Handle single string case
    if len(strings) == 1:
        return strings[0]
    
    # Find the shortest string in the list to limit prefix checks
    shortest = min(strings, key=len)
    
    # Iterate through characters of the shortest string
    for i in range(len(shortest)):
        # Check if this character matches in all strings
        if any(string[i] != shortest[i] for string in strings):
            return shortest[:i]
    
    # If we've made it through the entire shortest string, it's the common prefix
    return shortest