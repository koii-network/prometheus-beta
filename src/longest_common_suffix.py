def find_longest_common_suffix(strings):
    """
    Find the longest common suffix among a list of strings.
    
    Args:
        strings (list): A list of strings to compare.
    
    Returns:
        str: The longest common suffix. Returns an empty string if no common suffix exists.
    
    Raises:
        TypeError: If input is not a list.
        ValueError: If the list is empty.
    """
    if not isinstance(strings, list):
        raise TypeError("Input must be a list of strings")
    
    if not strings:
        raise ValueError("Input list cannot be empty")
    
    # Convert all strings to lowercase to ensure consistent comparison
    strings = [s.lower() for s in strings]
    
    # If any string is empty, there can be no common suffix
    if any(s == '' for s in strings):
        return ''
    
    # Find the minimum length among all strings
    min_length = min(len(s) for s in strings)
    
    # Check suffixes from the end of the shortest string
    for i in range(1, min_length + 1):
        suffix = strings[0][-i:]
        if all(s.endswith(suffix) for s in strings):
            result = suffix
        else:
            break
    
    return result if 'result' in locals() else ''