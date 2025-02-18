def create_suffix_array(s):
    """
    Create a suffix array for the given string.
    
    A suffix array is a sorted array of all suffixes of a string.
    
    Args:
        s (str): Input string to create suffix array for
    
    Returns:
        list: Sorted array of suffix indices
    
    Raises:
        TypeError: If input is not a string
    """
    # Validate input
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Create list of tuples with (suffix, original index)
    suffixes = [(s[i:], i) for i in range(len(s))]
    
    # Sort suffixes lexicographically and return their original indices
    return [index for suffix, index in sorted(suffixes)]

def search_suffix_array(suffix_array, s, pattern):
    """
    Search for a pattern in a string using suffix array.
    
    Args:
        suffix_array (list): Suffix array of the string
        s (str): Original string
        pattern (str): Pattern to search for
    
    Returns:
        list: Indices where pattern is found in the string
    
    Raises:
        TypeError: If inputs are not of correct type
        ValueError: If pattern is longer than string
    """
    # Validate inputs
    if not isinstance(suffix_array, list):
        raise TypeError("Suffix array must be a list")
    if not isinstance(s, str):
        raise TypeError("Original string must be a string")
    if not isinstance(pattern, str):
        raise TypeError("Pattern must be a string")
    
    if len(pattern) > len(s):
        raise ValueError("Pattern cannot be longer than the original string")
    
    # Find matching indices
    matches = []
    for index in suffix_array:
        # Check if the current suffix starts with the pattern
        if s[index:].startswith(pattern):
            matches.append(index)
    
    return matches