def find_longest_common_prefix(strings):
    """
    Find the longest common prefix among a list of strings.
    
    Args:
        strings (list): A list of strings to find the common prefix for.
    
    Returns:
        str: The longest common prefix. Returns an empty string if no common prefix exists.
    
    Raises:
        TypeError: If input is not a list
        ValueError: If the input list is empty
    """
    # Check for invalid inputs
    if not isinstance(strings, list):
        raise TypeError("Input must be a list of strings")
    
    if not strings:
        raise ValueError("Input list cannot be empty")
    
    # Handle single string case
    if len(strings) == 1:
        return strings[0]
    
    # Find the shortest string to limit prefix checking
    shortest = min(strings, key=len)
    
    # Check prefix character by character
    for i in range(len(shortest)):
        # Check if this character matches in all strings
        if any(string[i] != shortest[i] for string in strings):
            return shortest[:i]
    
    # If we've made it through the loop, shortest is the common prefix
    return shortest