def find_longest_common_suffix(strings):
    """
    Find the longest common suffix among a list of strings.
    
    Args:
        strings (list): A list of strings to find the common suffix for.
    
    Returns:
        str: The longest common suffix. Returns an empty string if no common suffix exists
             or if the input list is empty.
    
    Raises:
        TypeError: If the input is not a list.
        TypeError: If any element in the list is not a string.
    """
    # Validate input
    if not isinstance(strings, list):
        raise TypeError("Input must be a list of strings")
    
    # Handle empty list case
    if not strings:
        return ""
    
    # Validate all elements are strings
    if not all(isinstance(s, str) for s in strings):
        raise TypeError("All elements must be strings")
    
    # Handle single string case
    if len(strings) == 1:
        return strings[0]
    
    # Find the shortest string to limit suffix search
    shortest = min(strings, key=len)
    
    # Iterate from the end, checking successively shorter suffixes
    for i in range(1, len(shortest) + 1):
        suffix = shortest[-i:]
        if all(s.endswith(suffix) for s in strings):
            return suffix
    
    # If no common suffix found
    return ""