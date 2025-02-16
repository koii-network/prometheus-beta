def create_suffix_array(text):
    """
    Create a Suffix Array for the given input text.
    
    A Suffix Array is a sorted array of all suffixes of a given string.
    
    Args:
        text (str): The input string to create a suffix array for.
    
    Returns:
        list: A list of integer indices representing the sorted suffixes.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Validate input
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # If text is empty, return an empty list
    if not text:
        return []
    
    # Create list of tuples with (suffix, original index)
    suffixes = [(text[i:], i) for i in range(len(text))]
    
    # Sort suffixes lexicographically and extract original indices
    sorted_suffixes = sorted(suffixes, key=lambda x: x[0])
    
    return [index for _, index in sorted_suffixes]

def find_substring(text, pattern):
    """
    Find all occurrences of a pattern in the text using Suffix Array.
    
    Args:
        text (str): The text to search in.
        pattern (str): The substring to search for.
    
    Returns:
        list: Indices of all occurrences of the pattern in the text.
    
    Raises:
        TypeError: If inputs are not strings.
        ValueError: If pattern is empty.
    """
    # Validate inputs
    if not isinstance(text, str) or not isinstance(pattern, str):
        raise TypeError("Both text and pattern must be strings")
    
    if not pattern:
        raise ValueError("Pattern cannot be an empty string")
    
    # Create suffix array
    suffix_array = create_suffix_array(text)
    
    # Find all occurrences
    occurrences = []
    
    for i, suffix_index in enumerate(suffix_array):
        # Check if current suffix starts with the pattern
        if text[suffix_index:].startswith(pattern):
            occurrences.append(suffix_index)
        
        # Optimization: stop searching if suffix is lexicographically larger than pattern
        if text[suffix_index:suffix_index+len(pattern)] > pattern:
            break
    
    return occurrences