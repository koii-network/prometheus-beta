def find_longest_common_prefix(strings):
    """
    Find the longest common prefix among a list of strings.

    Args:
        strings (list): A list of strings to find the common prefix for.

    Returns:
        str: The longest common prefix. Returns an empty string if 
             the input is empty or no common prefix exists.

    Raises:
        TypeError: If the input is not a list or contains non-string elements.
    """
    # Check for empty input
    if not strings:
        return ""
    
    # Validate input is a list of strings
    if not isinstance(strings, list) or not all(isinstance(s, str) for s in strings):
        raise TypeError("Input must be a list of strings")
    
    # Handle case with single string
    if len(strings) == 1:
        return strings[0]
    
    # Find the shortest string to use as basis for prefix comparison
    shortest = min(strings, key=len)
    
    # Check prefix for each possible length of the shortest string
    for i in range(len(shortest)):
        # Check if current prefix is common to all strings
        if any(string[:i+1] != shortest[:i+1] for string in strings):
            return shortest[:i]
    
    # If we've made it through all checks, return the shortest string
    return shortest