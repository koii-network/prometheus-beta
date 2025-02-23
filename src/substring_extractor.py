def extract_unique_substrings(input_string):
    """
    Extract all unique substrings from the given input string.

    Args:
        input_string (str): The input string to extract substrings from.

    Returns:
        list: A list of unique substrings, sorted in order of appearance.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If input is empty, return empty list
    if not input_string:
        return []
    
    # Use a set to track unique substrings while preserving order
    unique_substrings = []
    seen = set()
    
    # Generate all possible substrings
    for start in range(len(input_string)):
        for end in range(start + 1, len(input_string) + 1):
            substring = input_string[start:end]
            
            # Add to list if not seen before
            if substring not in seen:
                unique_substrings.append(substring)
                seen.add(substring)
    
    return unique_substrings