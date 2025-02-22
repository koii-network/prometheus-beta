def find_longest_common_prefix(strings):
    """
    Find the longest common prefix among a list of strings.
    
    Args:
        strings (list): A list of strings to find the common prefix for.
    
    Returns:
        str: The longest common prefix. If no common prefix exists, returns an empty string.
    
    Raises:
        TypeError: If the input is not a list or contains non-string elements.
    """
    # Check if input is valid
    if not isinstance(strings, list):
        raise TypeError("Input must be a list of strings")
    
    # Handle empty list or list with no strings
    if not strings:
        return ""
    
    # Validate all elements are strings
    if not all(isinstance(s, str) for s in strings):
        raise TypeError("All elements must be strings")
    
    # If only one string, return the entire string
    if len(strings) == 1:
        return strings[0]
    
    # Sort the list to help find the common prefix more efficiently
    sorted_strings = sorted(strings)
    
    # Compare the first and last strings after sorting
    first = sorted_strings[0]
    last = sorted_strings[-1]
    
    # Find the common prefix between the first and last strings
    common_prefix = []
    for i in range(min(len(first), len(last))):
        if first[i] == last[i]:
            common_prefix.append(first[i])
        else:
            break
    
    return "".join(common_prefix)