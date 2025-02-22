def remove_excess_duplicates(input_string):
    """
    Remove characters that appear more than twice in the input string.
    
    Args:
        input_string (str): The input string to process.
    
    Returns:
        str: A modified string with characters appearing more than twice removed.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Count character frequencies
    char_counts = {}
    for char in input_string:
        char_counts[char] = char_counts.get(char, 0) + 1
    
    # Create the result string, keeping only characters that appear twice or less
    result = ''.join(char for char in input_string if char_counts[char] <= 2)
    
    return result