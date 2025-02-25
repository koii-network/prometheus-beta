def remove_excessive_duplicates(input_string):
    """
    Remove characters from a string that appear more than twice.
    
    Args:
        input_string (str): The input string to process.
    
    Returns:
        str: A modified string with characters appearing more than twice removed.
    """
    # Check for invalid input
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Count character occurrences
    char_count = {}
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Create new string keeping only characters that appear 1-2 times
    result = ''.join(char for char in input_string if char_count[char] <= 2)
    
    return result