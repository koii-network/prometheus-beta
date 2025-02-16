def find_most_frequent_char(input_string):
    """
    Find the most frequently occurring character in a string.
    
    Args:
        input_string (str): The input string to analyze
    
    Returns:
        str: The most frequently occurring character
             If multiple characters have the same highest frequency, 
             return the first one encountered
    
    Raises:
        ValueError: If the input string is empty
        TypeError: If input is not a string
    """
    # Validate input
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    if not input_string:
        raise ValueError("Input string cannot be empty")
    
    # Count character frequencies
    char_counts = {}
    for char in input_string:
        char_counts[char] = char_counts.get(char, 0) + 1
    
    # Find the most frequent character
    most_frequent_char = max(char_counts, key=char_counts.get)
    
    return most_frequent_char